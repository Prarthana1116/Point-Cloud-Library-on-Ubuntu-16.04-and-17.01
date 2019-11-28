# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from shutil import copyfile
import sys
#from pathlib import Path

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

pcdfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PLYNEW"
plyfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PLY_NoHead/"

pcdfilenames = getListOfFiles(pcdfolderpath)   # get all files and folders name in the current directory
#plyfilenames = getListOfFiles(plyfolderpath) 

for f in pcdfilenames:
    if ".txt" in f:
        getbasepath = os.path.split(f)
        basename = getbasepath[0]
        foldername = os.path.split(basename)
        destinationpath = plyfolderpath + foldername[1] +'/'+ os.path.split(os.path.splitext(f)[0])[1]+ ".txt"
        createfolder = os.path.join(plyfolderpath,foldername[1])
        createFolder(createfolder)
        #aa = os.path.join(getbasepath[0],getbasepath[1])
        copyfile(os.path.join(getbasepath[0],getbasepath[1]),destinationpath)
        
plyfilenames = getListOfFiles(plyfolderpath) 

for file in plyfilenames:
    if ".txt" in file:
        file = open(file, "r+")
        print(file)
        lines = [line.rstrip() for line in file]
        pcdinfo = lines[10:]
        file.seek(0)
        head = ""
        file.write(head)
       
        for line in pcdinfo:
            file.write(line+"\n")
        file.close()    
       
    
        

        
      


