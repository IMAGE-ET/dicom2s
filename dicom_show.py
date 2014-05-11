#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 09:46:01 2011

@author: hli
"""

usage = """
    Visualize 2d dicom image

    Usage: $ python dicom_show.py dicom_filename
"""

import pylab
import dicom
import os
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print usage
        sys.exit()

    fileName = sys.argv[1]
    ds=dicom.read_file(fileName)
    pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
    pylab.show()
