[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

# Results:
___
Annotated cell count: 48
___
>![original heatmap](https://github.com/jeffock/ihc_cellcount/blob/temp/README%20Screenshots/originalh5.png)
___
Predicted cell count: 47
___
>![model heatmap](https://github.com/jeffock/ihc_cellcount/blob/temp/README%20Screenshots/predictedh5.png)
___
Original image: cytokeratin 14 (KRT14) stain
___
>![original image](https://github.com/jeffock/ihc_cellcount/blob/temp/README%20Screenshots/originaljpg.png)
___

The MAE for the this model was 29.70, which isn't bad for the limited amount of data available to me, but could be better, it is also to be said that keratin stains can be much more difficult for NN to count due to the rampant background (it may also be explained by the fact that some cell counts were in the hundreds, making MAE=30 more reasonable compared to the context of the example given above). The nuclei stains such as DAPI and Ki67 will likely perform better, it is just taking me a while to annotate.

# TO-DO before you start:
___
You will need to add a \Data directory in the directory where the code resides.
You will also need to run auto_import.sh as specified by comments within the file.

Note on packages, this model uses CUDA supported PyTorch, make sure you have the correct packages for this if you have an Nvidia GPU. 

# Data:
___
The file tree that I used for my data is included.
Once you have your data in images, annotate them in MATLAB with the provided .m script in the keratin/ and nuclei/ directories.
Run make_dataset.ipynb to generate the needed .h5 files. 

I will be adding my own data and annotations, once I finish annotating all of them, as zipped files. 

# Training:
___
First ensure that the .json files contain the correct file paths.
To train run `python train.py krt_train.json krt_test.json 0 0`

# Testing:
___
Run val.ipynb to test.

# Specifics:
___
Note that this model was trained with KRT14, KRT5, Ki67, and DAPI stains. Each stain will appear slightly differently so the code will not be as effective for stains other than those mentioned. The two keratin stains were trained together while the two nuclei stains were trained together. 

# Credit:
___
Original CSRNet repo: [https://github.com/leeyeehoo/CSRNet-pytorch/tree/master] 
___
Original annotation repo: [https://github.com/princenarula222/Crowd_Annotation]


