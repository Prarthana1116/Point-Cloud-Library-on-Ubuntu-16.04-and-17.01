#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  11 13:23:16 2018

@author: ubuntu
"""
import os
from pathlib import Path

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


objfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/OBJ"
pcdfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/PCD"
#objfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/test/OBJ"
#pcdfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/test/PCD"

#meshexecpath = "/home/misumi/pcl/release/bin/pcl_mesh2pcd"

filenames = getListOfFiles(objfolderpath)   # get all files and folders name in the current directory

for f in filenames:    #loop through all the files and folders
    if ".obj" in f:
        getbasepath = os.path.split(f)
        basename = getbasepath[0]
        foldername = os.path.split(basename)

        createfolder = os.path.join(pcdfolderpath,foldername[1])

        outfilename = os.path.join(createfolder,Path(f).name.split('.')[0] + ".pcd")
        print(outfilename)
        createFolder(createfolder)

        print("pcl_mesh_sampling "+f +" " + outfilename +" -n_samples 2048 -leaf_size 0.001 -write_normals -no_vis_result")

        os.system("pcl_mesh_sampling "+f +" " + outfilename +" -n_samples 2048 -leaf_size 0.001 -write_normals -no_vis_result")

        print("pcl_mesh_sampling "+f +" " + outfilename +" -n_samples 2048 -leaf_size 0.001 -write_normals -no_vis_result")


        


