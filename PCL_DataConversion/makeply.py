import os
from shutil import copyfile
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

pcdfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PCD"
plyfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PLY/"

pcdfilenames = getListOfFiles(pcdfolderpath)   # get all files and folders name in the current directory
#plyfilenames = getListOfFiles(plyfolderpath) 

for f in pcdfilenames:    #loop through all the files and folders
    if ".pcd" in f:
        getbasepath = os.path.split(f)
        basename = getbasepath[0]
        foldername = os.path.split(basename)
        destinationpath = plyfolderpath + foldername[1] +'/'+ os.path.split(os.path.splitext(f)[0])[1]+ ".ply"
        createfolder = os.path.join(plyfolderpath,foldername[1])
        createFolder(createfolder)
        #aa = os.path.join(getbasepath[0],getbasepath[1])
        copyfile(os.path.join(getbasepath[0],getbasepath[1]),destinationpath)
        
plyfilenames = getListOfFiles(plyfolderpath) 

for file in plyfilenames:
    if ".ply" in file:
        file = open(file, "r+")
        print(file)
        lines = [line.rstrip() for line in file]
        pcdinfo = lines[11:]
        file.seek(0)
        head = "ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex 2048" + "\nproperty float x\nproperty float y\nproperty float z\nelement face 0\nproperty list uchar int vertex_indices\nend_header\n"
        file.write(head)
        for line in pcdinfo:
            file.write(line+"\n")
        file.close()    
    
        

        
      


