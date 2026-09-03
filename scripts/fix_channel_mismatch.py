# Channel mismatch scanner/fixer for TagLab datasets

"""
Scans your merged dataset folder (e.g. Staghorn_v1) for images or labels
that aren't plain 3-channel RGB (e.g. RGBA tiles with an alpha channel).
This mismatch crashes TagLab's computeAverage() step during training with:

    ValueError: operands could not be broadcast together with shapes
    (513,513,3) (513,513,4) (513,513,3)

Usage:
    Report only (safe, makes no changes):
        python fix_channel_mismatch.py "D:\Taglab_training\training-data\Staghorn_v1"

    Report AND convert bad files to RGB in place:
        python fix_channel_mismatch.py "D:\Taglab_training\training-data\Staghorn_v1" --fix

"""

import os
import argparse
from PIL import Image


def scan_folder(folder_path):
    """Return list of (filepath, mode) for every file whose PIL mode isn't RGB."""
    issues = []
    if not os.path.isdir(folder_path):
        return issues
    for fname in sorted(os.listdir(folder_path)):
        fpath = os.path.join(folder_path, fname)
        if not os.path.isfile(fpath):
            continue
        try:
            with Image.open(fpath) as im:
                if im.mode != "RGB":
                    issues.append((fpath, im.mode))
        except Exception as e:
            issues.append((fpath, f"UNREADABLE ({e})"))
    return issues


def fix_image(fpath, mode):
    """Convert an image file to RGB in place."""
    with Image.open(fpath) as im:
        if mode.startswith("RGBA") or mode == "LA":
            # Flatten onto BLACK background (avoids white bias for coral bleaching)
            bg = Image.new("RGB", im.size, (0, 0, 0))
            bg.paste(im, mask=im.split()[-1])
            bg.save(fpath)
        else:
            im.convert("RGB").save(fpath)


def main():
    parser = argparse.ArgumentParser(description="Find/fix channel mismatches in a TagLab dataset")
    parser.add_argument("root_dir", help="Path to your merged dataset folder (e.g. Staghorn_v1)")
    parser.add_argument("--fix", action="store_true", help="Convert bad files to RGB in place")
    args = parser.parse_args()

    all_issues = []
    for split in ("training", "validation", "test"):
        for kind in ("images", "labels"):
            folder = os.path.join(args.root_dir, split, kind)
            for fpath, mode in scan_folder(folder):
                all_issues.append((split, kind, fpath, mode))

    if not all_issues:
        print("No channel mismatches found. Every file is plain RGB.")
        return

    print(f"Found {len(all_issues)} problem file(s):\n")
    for split, kind, fpath, mode in all_issues:
        print(f"  [{split}/{kind}]  mode={mode:12s}  {fpath}")

    if args.fix:
        print("\nConverting problem files to RGB...")
        fixed, failed = 0, 0
        for split, kind, fpath, mode in all_issues:
            if mode.startswith("UNREADABLE"):
                print(f"  SKIPPED (unreadable, needs manual check): {fpath}")
                failed += 1
                continue
            try:
                fix_image(fpath, mode)
                fixed += 1
            except Exception as e:
                print(f"  FAILED to fix {fpath}: {e}")
                failed += 1
        print(f"\nDone. Fixed {fixed}, failed {failed}.")
    else:
        print("\nRun again with --fix to convert these files to RGB in place.")


if __name__ == "__main__":
    main()