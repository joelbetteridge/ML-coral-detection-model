---
Generator: Microsoft Word 15 (filtered)
lang: EN-GB
---

:::: {.WordSection1}
**[TagLab Machine
Learning using DeepLabV3+]{lang="EN-US" style="font-size:20.0pt;font-family:\"Calibri\",sans-serif"}**

[Standard
Operating Procedure]{lang="EN-US" style="font-size:13.0pt;font-family:\"Calibri\",sans-serif;color:#555555"}

*[SOP by
Joel Betteridge]{lang="EN-US" style="font-size:11.0pt;font-family:\"Calibri\",sans-serif"}*

## [Prerequisites]{lang="EN-US"} {#prerequisites style="margin-top:18.0pt;margin-right:0cm;margin-bottom:8.0pt;margin-left:
0cm"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Prior experience with
TagLab required.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Prior experience with
Python beneficial.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Prior experience with
PowerShell beneficial.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Lots and lots of patience.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

## [Important note]{lang="EN-US"} {#important-note style="margin-top:18.0pt;margin-right:0cm;margin-bottom:8.0pt;margin-left:
0cm"}

[Within ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[training.py]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[, line 129, ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[dtype]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[ was originally set to ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[int]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[. NumPy\'s plain ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[int]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[ maps to a 32-bit integer
on Windows, whereas on Linux or Mac it\'s 64-bit, so this line behaves
differently depending on the operating system. When training a large dataset,
this causes corrupted arithmetic from overflowed, sometimes negative, confusion
matrix entries. I have changed this, but when TagLab is next updated, this fix
may be reset and need to be reapplied.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

## [Important note 2]{lang="EN-US"} {#important-note-2 style="margin-top:18.0pt;margin-right:0cm;margin-bottom:8.0pt;margin-left:
0cm"}

[Many of these scripts are already in
TagLab-main on the super computer, check before re-downloading, you may be able
to just paste the prompt in cmd. You can find all the scripts I used within
Intern Projects \\ Joel , including scripts for pixel-wise statistics and
disagreement maps.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 1 --- Make a project folder and add your existing projects]{lang="EN-US"} {#step-1-make-a-project-folder-and-add-your-existing-projects style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

**[IMPORTANT --- save and copy all files
locally (otherwise you must wait hours for OneDrive sync later).]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

[Create a project folder, e.g. ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[acer_taglab_training]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[. Within this folder,
create two other folders: ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[data-raw]{lang="EN-US" style="font-family:Consolas;
color:black;background:#EFEFEF"}[ and ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[training]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[. Within ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[data-raw]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[ you will add your existing
projects.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[For a previously completed project,
find the corresponding .json and .jpg file and copy them both locally into
their site folder within data-raw. For example:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[D:/acer_taglab_training/data-raw/ac_T1/COPY_AC_T1.json]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

[D:/acer_taglab_training/data-raw/ac_T1/COPY_AC_T1.jpg]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

[Repeat this for each completed
project, like this:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[![](GitSOP_files/image001.gif){#Picture 1 width="166" height="223"}]{lang="EN-US"}

*[Example:
each site\'s project files copied locally into data-raw]{lang="EN-US" style="font-size:9.0pt;font-family:\"Calibri\",sans-serif;color:#555555"}*

# [Step 2 --- Open one of the projects]{lang="EN-US"} {#step-2-open-one-of-the-projects style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[Open TagLab and open a project from a
site folder within data-raw.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[If TagLab can\'t find the orthomosaic,
it will ask you to locate it again, choose the corresponding .jpg file in the
site folder.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 3 --- Look at the Labels panel]{lang="EN-US"} {#step-3-look-at-the-labels-panel style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[On the right-hand side you\'ll have
your classes. For example, yours might look something like:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[👁 Staghorn]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[👁 Porites]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[👁 Montipora]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[👁 Algae]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[👁 Rubble]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[We want only \'Staghorn\' available.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

**[Click Project → Labels
Dictionary Editor]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

[Create a new label, \'Staghorn\', with a
set RGB (e.g. 255,0,0). **You must use the same RGB code for \'Staghorn\' in
every project, as TagLab recognizes different colours as different classes when
creating a training dataset.**]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Highlight all the previously
identified Staghorn and apply it all to the new \'Staghorn\' label.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 4 --- Turn OFF unwanted classes]{lang="EN-US"} {#step-4-turn-off-unwanted-classes style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

**[Click the eye icon beside every class
except Staghorn. Only Staghorn should be visible when we export the training
data.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

[You want:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[👁 Staghorn]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Porites]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Montipora]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Algae]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Rubble]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[If you accidentally leave Porites
visible, for example, TagLab will treat it as another training class, even if
only 0% of it is highlighted.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 5 --- Export a training dataset]{lang="EN-US"} {#step-5-export-a-training-dataset style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

**[Train → Export New Training
Dataset]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

**[For dataset folder]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**[, enter the \'training\'
folder you created earlier. Within this folder you need a folder for each site,
and within each site, a folder for each working area. For example:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[D:/acer_taglab_training/training/AC_T1/working_area_1]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

**[For Working area]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**[, select an area where the
labels are excellent. Expect to split the entire site into 3--5 smaller working
areas. The areas chosen should differ in the type of annotations; the aim is
high variability, so the model learns in all environments. Some areas should
contain high/low coral density, some with strange angles, some with the target
coral close to other species, some with low resolution, etc.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Example working area:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[![](GitSOP_files/image002.gif){#Picture 1695644859 width="451" height="275"}]{lang="EN-US"}

*[Example
working area, selected for variability in annotation conditions]{lang="EN-US" style="font-size:9.0pt;font-family:\"Calibri\",sans-serif;color:#555555"}*

**[For dataset split]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**[: uniform vertical]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

**[Target scale]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**[ is 0.9 or 1 --- be
consistent each time.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

**[Click export]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

[The working_area_1 folder should now
contain three folders and one file: test, training, validation, and
target-pixel-size. Do a sanity check by entering the folders and comparing the
\'images\' and \'labels\' folders. Each .jpg in \'images\' should have a corresponding
.jpg in the \'labels\' folder, and the labels version should have the Staghorn
highlighted in red (or your RGB of choice).]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

**[SAVE THE PROJECT]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

**[Repeat for other working areas and
sites, including lots of variability. Aim for 20--25 training data sets
(including working areas), the more, the better.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

# [Step 6 --- Renaming files with PowerShell]{lang="EN-US"} {#step-6-renaming-files-with-powershell style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[Your existing data should currently
look like this:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[training]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[├──
ac_T1]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│  
├── working_area_1]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│   │  
├── training]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│   │  
│   ├── images]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│   │  
│   └── labels]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│   │  
├── validation]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│   │  
│   ├── images]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│   │  
│   └── labels]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│   │  
└── test]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│  
│       ├── images]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│  
│       └── labels]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│   │]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│  
├── working_area_2]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│  
└── \...]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[├──
mi_dushi_I_T3]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│  
├── working_area_1]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│  
├── working_area_2]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│  
└── \...]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[│]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[└──
other sites\...]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[ ]{lang="EN-US"}

[We want one complete folder,
containing all sites and working areas, with only 3 folders: \'training\',
\'validation\' and \'test\'. However, if we were to copy all images into one folder
as-is, file names would overwrite each other.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Create a new folder within \'training\'
called ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[Staghorn_v1]{lang="EN-US" style="font-family:Consolas;color:black;
background:#EFEFEF"}[.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Inside \'training\', shift + right-click
the white space and choose \'Open PowerShell window here\'.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Paste the merge script in /scripts/image_merger
into PowerShell and accept any permission prompts.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 7 --- Check the final report]{lang="EN-US"} {#step-7-check-the-final-report style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[Check the final report of the script.
You want to see something like this:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[MERGE COMPLETE]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[Image/label pairs
copied: 28743]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[Missing labels: 0]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[Duplicate names: 0]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[Copy errors: 0]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[ ]{lang="EN-US"}

[You can also do a sanity check of the
folders and check a few file names to make sure the script worked properly.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 8 --- Fixing RGBA issues]{lang="EN-US"} {#step-8-fixing-rgba-issues style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[If you attempted to train the network
now, it would crash during \'Computing average\', as it would likely hit an image
with 4 channels (RGBA) rather than 3 (RGB). This is due to a gap in the working
area of the orthomosaic area. This gap can come from the boundaries of the
orthomosaic itself, or from empty space within it.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[To fix this, we\'ll convert all RGBA
images into RGB images by changing the alpha channel (A) into black,  matching
the background, and avoiding white, since white is a bleaching indicator.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[First, save the script ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[fix_channel_mismatch.py]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[ in /scripts.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Open a command prompt and run:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[python
fix_channel_mismatch.py
\"D:\Taglab_training\training-data\Staghorn_v1\"]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

[If the list of images is as expected,
re-run with \--fix added to convert them:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[python
fix_channel_mismatch.py
\"D:\Taglab_training\training-data\Staghorn_v1\" \--fix]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

# [Step 9 --- Creating a crash traceback with TagLab]{lang="EN-US"} {#step-9-creating-a-crash-traceback-with-taglab style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[It would be great if training your
network worked first time. However, if it crashes while using the standard
Start TagLab shortcut, the command window closes before you get a chance to
read the error message. From now on, we\'ll open TagLab manually through cmd,
alongside a crash log .txt file.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Open a command prompt and enter:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[cd C:\TagLab-main]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

[python TagLab.py
\> crash_log.txt 2\>&1]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

[This runs TagLab and saves everything
it prints into a file called crash_log.txt in the same folder.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 10 --- Train your network]{lang="EN-US"} {#step-10-train-your-network style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[Open TagLab via Step 9, and open a
project with the correct labelling: only Staghorn (255,0,0).]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

**[Click Train → Train Your Network]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Network name: Staghorn_v1]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Dataset folder: choose the
combined training folder]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Classes to recognize: \*]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Training: Preset 1]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Optimizer: Adam]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Number of epochs: \*\*]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Learning rate: 0.00005]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[L2 Regularization: 0.0005]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Batch size: \*\*\*]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

::: {style="border:none;border-left:solid #AAAAAA 1.5pt;padding:0cm 0cm 0cm 8.0pt;
margin-left:10.0pt;margin-right:0cm"}
*[\* Under
\'Classes to recognize\', only Staghorn and Background should be present, with a
realistic percentage attribution shown --- e.g. 95% background, 5% Staghorn.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif;color:#555555"}*

*[\*\* As a first
test run, I recommend around 10 epochs. After a successful run, you can re-run
with around 60 epochs.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif;color:#555555"}*

*[\*\*\* Batch
size is set to 4 by default. You can try this first, but may need to change it
later.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif;color:#555555"}*
:::

**[Click Train]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}**

# [Step 11 --- Check it reaches \'Training\']{lang="EN-US"} {#step-11-check-it-reaches-training style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[It\'s important not to leave for a dive
at this point, crashes will most likely happen during data setup. You won\'t be
able to see the terminal, as output is being sent to crash_log.txt. However, if
it crashes, the cmd window will close. If you encounter a crash, open
crash_log.txt and troubleshoot appropriately.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Data setup takes around 5 minutes
before \'Training --- Iteration 1/n\' starts. As a rough guide, 100,000 iterations
takes around 18 hours.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 12 --- Sanity check of crash_log.txt]{lang="EN-US"} {#step-12-sanity-check-of-crash_log.txt style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[After around 2,000 iterations, open
another cmd window and paste this:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[powershell
Get-Content C:\TagLab-main\crash_log.txt -Tail 2000]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

[Check for:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[No error messages]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[All values are finite and
real --- you should have no \'nan\' values]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Normal noise --- iteration
values should be bouncing around, not stuck]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[If things look good, it\'s time to
relax!]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Here is the paper on DeepLabV3+, if
you\'re interested in what\'s happening now: ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[[[Encoder-Decoder with Atrous Separable
Convolution for Semantic Image Segmentation]{style="font-family:\"Calibri\",sans-serif"}](https://openaccess.thecvf.com/content_ECCV_2018/papers/Liang-Chieh_Chen_Encoder-Decoder_with_Atrous_ECCV_2018_paper.pdf)]{lang="EN-US"}

# [Step 13 --- Second sanity check of crash_log.txt]{lang="EN-US"} {#step-13-second-sanity-check-of-crash_log.txt style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[The next day, once training is more
than halfway through (if it has completed, move on to Step 14), run another
sanity check of crash_log.txt (see previous step).]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[If things are good, keep waiting. If
you\'ve run into an error message, troubleshoot accordingly. If you observe a
\'nan\' cascade, the batch size may be too small.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[With batch size 4 and around a 95/5
class imbalance:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Some batches might be
mostly background (nearly zero Staghorn pixels)]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[The next batch might be
Staghorn-heavy]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[This creates wildly
inconsistent gradient estimates between batches]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[•[     ]{style="font:7.0pt \"Times New Roman\""}]{lang="EN-US"}[Focal Tversky loss is
sensitive to these fluctuations and can explode into nan]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[You can edit the sanity check command
to show the last 10,000 (or more) lines, to find where the \'nan\' cascade
started.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[If the model was still actively
learning (batch loss still decreasing substantially), cancel this training run
and retry from Step 10 with batch size 8, then 16 if needed. If the \'nan\'
cascade began after the model had stopped learning (bouncing around a similar
batch loss), you can extract the best model and test it.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Note: I created a 98% accurate (Cohen's
Kappa) model for staghorn with only 19/40 epochs before nan cascade.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 14 --- Extraction or completion]{lang="EN-US"} {#step-14-extraction-or-completion style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[If your model needs extracting,
proceed with this step. If your model completed, skip to Step 17.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

## [Extraction]{lang="EN-US"} {#extraction style="margin-top:18.0pt;margin-right:0cm;margin-bottom:8.0pt;margin-left:
0cm"}

[Open ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[TagLab-main]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[ → ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[models]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[. You should find your
model as a .net file (e.g. Stag_v1.net), along with a .txt file of the
validation metrics (e.g. Stag_v1-val-metrics.txt). Here is an example of what
those metrics look like:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[CONFUSION MATRIX:]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[2341318047  32361563]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[  28710916 118386178]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[NORMALIZED CONFUSION
MATRIX:]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[0.986  0.014]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[0.195  0.805]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[ACCURACY      : 0.976]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[Jaccard Score : 0.000]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[ ]{lang="EN-US"}

[As our training did not reach
completion, we must manually compute the \'Average Norm\' values (the per-channel
mean pixel values from the training images) and add the .net file into the
config.json file within TagLab-main.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 15 --- Computing \'Average Norm\']{lang="EN-US"} {#step-15-computing-average-norm style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[Open cmd.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Save the script: ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}[compute_dataset_avg.py]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}[ within TagLab-main ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Run it:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[cd C:\TagLab-main]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

[python
compute_dataset_avg.py]{lang="EN-US" style="font-family:Consolas;color:black;background:#EFEFEF"}

# [Step 16 --- Add your .net model into config.json]{lang="EN-US"} {#step-16-add-your-.net-model-into-config.json style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[Open config.json with Notepad++.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Add your model within the file, for
example:]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[{]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[    \"Classifier
Name\": \"Staghorn\",]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[   
\"Weights\": \"Stag_v1.net\",]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[    \"Num.
Classes\": 2,]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[   
\"Classes\": {]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[       
\"Background\": 0,]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[       
\"Staghorn\": 1]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[    },]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[    \"Scale\":
0.9,]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[    \"Average
Norm.\": \[]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[        0.445,]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[        0.4441,]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[        0.4351]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[    \]]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[},]{lang="EN-US" style="font-size:8.5pt;font-family:Consolas;color:black"}

[ ]{lang="EN-US"}

# [Step 17 --- Test your first model]{lang="EN-US"} {#step-17-test-your-first-model style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[Open TagLab along with a new
orthomosaic that the model was not trained on. Using a trained ortho will show
unrealistically perfect results as it was trained on those (although it does
boost your ego). ]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Click \'Fully automatic semantic
segmentation\'.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Use the boundary box and preview to
explore different areas of the orthomosaic. If you\'re happy with the model\'s
accuracy, clicking \'Apply\' will run the model on the entire orthomosaic. This
takes around 40 minutes.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

# [Step 18 --- The results and human editing]{lang="EN-US"} {#step-18-the-results-and-human-editing style="margin-top:20.0pt;margin-right:0cm;margin-bottom:10.0pt;margin-left:
0cm"}

[Observe the results and note areas of
weakness in the model. This is the type of content you want to add to the
training set to improve its accuracy.\
\
When editing the AI annotations, I recommend using positive/negative clicks
segmentation. If the area is large, you should 'cut region' to improve processing
efficiency.\
\
Once you are happy, save in-line with the TagLab SOP.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[If the model is ready to be retrained
(\>3 new sites have been completed, follow my other SOP: 'Enhancing the
model'.]{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}

[Stag_v2 is pending '\_']{lang="EN-US" style="font-family:\"Calibri\",sans-serif"}
::::
