# NiFTy
NiFTy is a python based image generation program

# How to install
Installation is very simple

Just run ``pip install niftygen2``

PIP INSTALLATION DETAILS
Version: 2.1.0
Stability: Minimal Testing (Stable)

Version: 2.0.1
Stability: Tested (Stable)

Version 1.0.0
Stability: Tested (Unstable)

# Initial Setup
STEP 1
-
Create a folder for each layer

STEP 2
-
Add all of the images that may be used for that layer

STEP 3
-
Create a .py file to run your program

# How to use
STEP 4
-
Import nifty

STEP 5
-
Set layers and add paths to folders and results folder

STEP 6
-
Finish your program and run

# Usage
``nifty.set_layers(layers)``: Set the amount of layers generated

``nifty.set_directory(layer, path)``: Set the path to the folder for a layer

``nifty.save_to(path)``: Set the path to the folder where results are saved

``nifty.generate(code)``: Generate image based on code

**NEW 2.1.0 FEATURES**

``nifty.mass_generate(start_code, end_code)``: Generate all images within specified range

``nifty.view(code)``: View generated image from given code

``nifty.possibilities()``: View amount of possible unique images

*Example in sample.py*

# Notices
- v2.1.0 has had minimal testing (USE AFTER TESTING YOUR PROGRAM)
