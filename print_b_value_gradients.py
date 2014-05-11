#!/usr/bin/env python

usage = """
usage:
    python print_B_value_gradients.py folder_name
    
note:
    Read b value and gradients from a dicom data folder
"""

import sys
import os
import gdcm

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print usage
        sys.exit()

    folder = sys.argv[1]
    print '--> folder name:', folder
    #fileList = os.popen('ls').readlines()
    fileList = os.listdir( folder )
    fileList.sort()
    for file in fileList:
        print file,
        file = folder + file
        r = gdcm.Reader()
        r.SetFileName( file )
        
        try:
            r.Read()
        except:
            print 'errorfail to read:', file
        
        ds = r.GetFile().GetDataSet()
        csa_t1 = gdcm.CSAHeader()
        t1 = csa_t1.GetCSAImageHeaderInfoTag()
       
        if ds.FindDataElement( t1 ):
            csa_t1.LoadFromDataElement( ds.GetDataElement( t1 ) )

        bvalues = csa_t1.GetCSAElementByName( "B_value" ) # WARNING: it is case sensitive !
        diffgraddir = csa_t1.GetCSAElementByName( "DiffusionGradientDirection" ) # WARNING: it is case sensitive !
        print bvalues, diffgraddir
