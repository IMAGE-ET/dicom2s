#!/usr/bin/env python
# -*- coding: utf-8 -*-
# dicomInfo.py

usage="""
usage:
    python dicomInfo.py folderName/
    
note:
    print Dicom Info to screen
"""

import os
import sys
import dicom

def printDsBasic(ds):
    print '\n--- --- New Series Info: --- ---'
    print " Series Number               ", ds[0x0020, 0x0011].value
    print " Series Description          ", ds[0x0008, 0x103e].value  #  LO: 't2_tse_SA_512'
    print " [GradientMode]              ", ds[0x0019, 0x100f].value      #SH: 'Normal'

    print "\n Pixel Spacing               ", ds[0x0028, 0x0030].value
    print " Slice Thickness             ", ds[0x0018, 0x0050].value
    print " Spacing Between Slices      ", ds[0x0018, 0x0088].value

    print "\n Acquisition Matrix          ", ds[0x0018, 0x1310].value
    print " Rows                        ", ds[0x0028, 0x0010].value
    print " Columns                     ", ds[0x0028, 0x0011].value
    print " Fild of View                ", ds[0x0051, 0x100c].value     
    print "\n [PositivePCSDirections]     ", ds[0x0051, 0x1013].value      #SH: '+LPH'
#print " Patient Position            ", ds[0x0018, 0x5100].value       CS: 'HFS'

    print "\n Image Type                  ", ds[0x0008, 0x0008].value  #  CS: ['ORIGINAL', 'PRIMARY', 'M', 'ND', 'NORM']

    print "\n Manufacturer                ", ds[0x0008, 0x0070].value  #  LO: 'SIEMENS'
    print " Institution Name            ", ds[0x0008, 0x0080].value  #  LO: 'HOPITAL NEURO-CARDIOLOGIQUE LYON'
    print " Institution Address         ", ds[0x0008, 0x0081].value  #  ST: 'Avenue Doyen Lepine 14,BRON,LYON,FR,69500'

    print "\n Patient's Name              ", ds[0x0010, 0x0010].value  #  PN: '61-10'
    print " Patient's Sex               ", ds[0x0010, 0x0040].value  #  CS: 'F'
    print " Patient's Age               ", ds[0x0010, 0x1010].value  #  AS: '026Y'

    print "\n Scanning Sequence           ", ds[0x0018, 0x0020].value  #  CS: 'SE'
    print " Sequence Variant            ", ds[0x0018, 0x0021].value  #  CS: ['SK', 'SP', 'OSP']
    print " MR Acquisition Type         ", ds[0x0018, 0x0023].value  #  CS: '2D'
    print " Sequence Name               ", ds[0x0018, 0x0024].value  #  SH: '*tse2d1_13'
    print " Repetition Time             ", ds[0x0018, 0x0080].value  #  DS: '5270'
    print " Echo Time                   ", ds[0x0018, 0x0081].value  #  DS: '102'
    print " Magnetic Field Strength     ", ds[0x0018, 0x0087].value  #  DS: '1.5'

    print "\n Image Position (Patient)    ", ds[0x0020, 0x0032].value  #  DS: ['-140.17887394514', '-71.444345677834', '103.32542656514']
    print " Image Orientation (Patient) ", ds[0x0020, 0x0037].value  #  DS: ['0.96819733646427', '-0.2501877648158', '-4.622649e-009', '0.06885999451951', '0.26648012853844', '-0.9613774712614']
    print " Slice Location              ", ds[0x0020, 0x1041].value  #  DS: '-71.778530079241'

#    print "\n [CSA Image Header Type]     ", ds[0x0029, 0x1008].value  #  CS: 'IMAGE NUM 4'
#    print " [CSA Image Header Version]  ", ds[0x0029, 0x1009].value  #  LO: '20100202'
#    print " [CSA Image Header Info]     ", ds[0x0029, 0x1010].value  #  OB: Array of 9388 bytes
#    print " [CSA Series Header Type]    ", ds[0x0029, 0x1018].value  #  CS: 'MR'
#    print " [CSA Series Header Version] ", ds[0x0029, 0x1019].value  #  LO: '20100202'
#    print " [CSA Series Header Info]    ", ds[0x0029, 0x1020].value  #  OB: Array of 70156 bytes

    print "\n Requested Procedure Description ", ds[0x0032, 0x1060].value  #  LO: 'Cardio_coeur DIFFUSION'
#    print " Study Comments                  ", ds[0x0032, 0x4000].value  #  LT: 'NOYADE'
    print " [CSA Image Header Type]         ", ds[0x0051, 0x1008].value  #  CS: 'IMAGE NUM 4'
    print " [CSA Image Header Version ??]   ", ds[0x0051, 0x1009].value  #  LO: '1.0'
    print " [Unknown]                       ", ds[0x0051, 0x100a].value  #  LO: 'TA 02:12'
#    print " Pixel Data                      ", ds[0x7fe0, 0x0010].value  #  OW: Array of 458752 bytes
def printDs(pathName):
    fileList = os.listdir(pathName)
    fileList.sort()
    
    gradientMode = []  # used to note the changes
    seriesNumber = []  # used to note the changes
    for fileName in fileList: 
        fullName = os.path.join(pathName, fileName)
        ds = dicom.read_file(fullName)
        
        #  another series ?!
        if seriesNumber != ds[0x0020, 0x0011].value:
            seriesNumber = ds[0x0020, 0x0011].value
            
            printDsBasic(ds)
            gradientMode = ds[0x0019, 0x100f].value
            if gradientMode != 'Normal':
                print "\n [NumberOfImagesInMosaic]    ", ds[0x0019, 0x100a].value
            
        # print b value and gradient
        if gradientMode != 'Normal':
            bValue = ds[0x0019, 0x100c].value
            if bValue == 0:
                print '\n', fileName, '>>',
                print "[B_value]", bValue
            else:
                print fileName, '>>',
                print "[B_value]", bValue,
                print " [DiffusionGradientDirection]", ds[0x0019, 0x100e].value 


if __name__ == "__main__":
        
    if len(sys.argv) != 2:
        print usage
        sys.exit()

    pathName = sys.argv[1]
    printDs(pathName)           
    print "---done---"

#print " Acquisition Number          ", ds[0x0020, 0x0012].value
#print " Instance Number             ", ds[0x0020, 0x0013].value

#print " Smallest Image Pixel Value  ", ds[0x0028, 0x0106].value  
#print " Largest Image Pixel Value   ", ds[0x0028, 0x0107].value 
#print " Bits Allocated              ", ds[0x0028, 0x0100].value
#print " Bits Stored                 ", ds[0x0028, 0x0101].value
#                                     ,                         
#print " Number of Averages          ", ds[0x0018, 0x0083].value       DS: '1' 
#print " Echo Number(s)              ", ds[0x0018, 0x0086].value       IS: '1' 
