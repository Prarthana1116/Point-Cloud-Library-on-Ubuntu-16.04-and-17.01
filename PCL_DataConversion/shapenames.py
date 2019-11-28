import os
from shutil import copyfile
from pathlib import Path

#def createFolder(directory):
#    try:
#        if not os.path.exists(directory):
#            os.makedirs(directory)
#    except OSError:
#        print('Error: Creating directory. ' + directory)

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
    plyfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/uData/"

    filenames = getListOfFiles(plyfolderpath)   # get all files and folders name in the current directory
    filelist = open(plyfolderpath +"/" + "shapenames.txt", "w+")
    namelist = []

    for f in filenames:    #loop through all the files and folders
        if ".ply" in f:
            getbasepath = os.path.split(f)
            basename = getbasepath[0]
            foldername = os.path.split(basename)
            
            #filelist.write(str(foldername[1])+"/"+str(getbasepath[1]) + os.linesep)
            if str(foldername[1]) not in namelist:
                #filelist.write(str(foldername[1])+"/"+str(getbasepath[1]) + os.linesep)
                filelist.write(str(foldername[1]) + os.linesep)
                namelist.append(str(foldername[1])+"/"+str(getbasepath[1]))

if __name__=="__main__":
    main()
          