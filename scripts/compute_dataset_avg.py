# Compute the average pixel values of a dataset of images

import numpy as np
from PIL import Image as PILimage
import os
import glob

images_dir = r'insert_working_directory_here'

print(f"Looking in: {images_dir}")
print(f"Folder exists: {os.path.isdir(images_dir)}")

image_files = glob.glob(os.path.join(images_dir, '*.png'))
print(f"Found {len(image_files)} PNG files")

if len(image_files) == 0:
    print("No images found. Check the path.")
else:
    sum_pixels = np.zeros(3, dtype=np.float64)
    count = 0
    CROP_SIZE = 513

    for i, img_file in enumerate(image_files):
        try:
            img = PILimage.open(img_file)
            data = np.array(img, dtype=np.float32)
            w = data.shape[1]
            h = data.shape[0]
            ox = int((w - CROP_SIZE) / 2)
            oy = int((h - CROP_SIZE) / 2)
            data_crop = data[oy:oy + CROP_SIZE, ox:ox + CROP_SIZE]
            
            sum_pixels[0] += np.mean(data_crop[:,:,0])
            sum_pixels[1] += np.mean(data_crop[:,:,1])
            sum_pixels[2] += np.mean(data_crop[:,:,2])
            count += 1
            
            if (i + 1) % 100 == 0:
                print(f"Processed {i + 1} images...")
        except Exception as e:
            print(f"Error on {img_file}: {e}")

    avg = sum_pixels / count / 255.0
    print(f"\nAverage Norm.: [{avg[0]:.4f}, {avg[1]:.4f}, {avg[2]:.4f}]")