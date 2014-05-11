#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 11 17:11:39 2011

@author: hli
"""

usage="""
    $ python arrange_dicoms_to_3d_array folderName/
     
    Note: arrange dicom images in a folder into a 3d np.array
"""


import sys
import os
import dicom
import numpy as np
#import glob
#fileList=glob.glob(pathName)

def all2one(pathName):
    fileList = os.listdir(pathName)
    fileList.sort()
    fullName = os.path.join(pathName, fileList[0])

    # setup a matrix to store data: [shape[0], shape[1], lenOfFile]
    ds=dicom.read_file(fullName)
    store3d=np.zeros([ds.pixel_array.shape[0], ds.pixel_array.shape[1], len(fileList)], dtype=np.uint16)

    for i in range(len(fileList)):
        fullName = os.path.join(pathName, fileList[i])
        ds=dicom.read_file(fullName)
        store3d[:,:,i] = ds.pixel_array
        return store3d
print 'done'

if __name__ == "__main__":
        
    if len(sys.argv) != 2:
        print usage
        sys.exit()

    pathName = sys.argv[1]
    if os.path.exists(pathName):
        print 'path not found'
        sys.exit()
    all2one(pathName)
    print "---done---"

