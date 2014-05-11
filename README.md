dicom2s
=======

Quick and dirty tools in Python for manipulating DICOM images.

Arrange dicom images in a folder into a 3d np.array (note the `/` after `folerName`):
`$ python arrange_dicoms_to_3d_array.py folderName/`

Print Dicom Info to screen:
`$ python dicomInfo.py folderName/`

Visualize 2d dicom image:
`$ python dicom_show.py dicom_filename`

Read b value and gradients from a dicom data folder:
`$ python print_B_value_gradients.py folderName/`

