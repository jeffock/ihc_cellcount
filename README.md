# TO-DO before you start
___
You will need to add a \Data directory in the directory where the code resides.
You will also need to go through all of the files and edit directories to match your own as needed.
You will also need to run auto_import.sh as specified by comments within the file.

# Data
___
First order is to name all of your images IMG_*.jpg
Next, annotate them through MATLAB using the script found in Data/. 

Finally generate your .h5 files using make_dataset.ipynb. 

# Training
___
Begin by running $python train.py krt_train.json krt_val.json 0 0$

# Testing
___
Test with val.ipynb. 

# Specifics
___
Note that this model was trained with KRT14, KRT5, Ki67, and DAPI stains. Each stain will appear slightly differently so the code will not be as effective for stains other than those mentioned. The two keratin stains were trained together while the two nuclei stains were trained together. 

# Credit
___
Original CSRNet repo: [https://github.com/leeyeehoo/CSRNet-pytorch/tree/master] 
___
Original annotation repo: [https://github.com/princenarula222/Crowd_Annotation]


