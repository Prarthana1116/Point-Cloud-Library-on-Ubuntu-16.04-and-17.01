#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:23:16 2018

@author: ubuntu
"""
import os
#from pathlib import Path

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

def main():        
    plyfolderpath = "/home/misumi/Desktop/Write_hdf5File/data/Taper/test"

    filenames = getListOfFiles(plyfolderpath)   # get all files and folders name in the current directory
    filelist = open("test5.txt", "w+")

    for f in filenames:    #loop through all the files and folders
        if ".ply" in f:
            getbasepath = os.path.split(f)
            basename = getbasepath[0]
            foldername = os.path.split(basename)
        
        filelist.write(str(foldername[1])+"/"+str(getbasepath[1]) + os.linesep)
        #filelist.write(str(foldername[1]) + os.linesep)
                  
if __name__=="__main__":
    main()
