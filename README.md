# count-nucleus
This is a code for counting cells based on fluorescence nuclear staining.

QUICK BACKGROUND: I am a wet-lab scientist and I just learned programming not so long ago, so the code will be simple. I expect that this will help others as it is helping me.

GOAL: This code will count nuclear staining (e.g. DAPI) based on SHAPE and AREA. So it will give you the total number of cells that are present in your microscopy figure. Well, in fact it is very easy to count by eye, however, I developed this for two further purposes: 1) Compare the number of infected and not infected cells by a pathogen (e.g. virus); 2) Compare the expression of certain proteins that could be upregulated/downregulated/translocated as the progression of the infection goes; 3) Use a large ammount of images for each experimental group to improve the accuracy of my analysis.

WARNING: Is VERY important to check the code before using it! The parameters are adjusted to my microscopy figures that I took using a certain exposure level and high black balance, so parameters will require adjustment. I still have to check if it works with different image resolutions!

EXPECTED ERRORS: I used an endothelial cell model, those cells are very flat and their nucleus have a tendency to be far away from each other. However, I still have some pictures that two or more nucleus are packed, and the code will give only one cell. So, other cell types that clump together and the contours are not very well delimited for a single nucleus, that will give a erroneous counting. This is a working in progress and I will appreciate any contributions.

If you are reading this, THANK YOU! I am looking forward to interact with you!
