import os
#from shutil import copyfile
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


normalfolderpath = '/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PLY'
datafolderpath = '/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PLYNEW/'

 # get all files and folders name in the current directory
textfilenames = getListOfFiles(normalfolderpath) 

for f in textfilenames:    #loop through all the files and folders
    if ".ply" in f:
        getbasepath = os.path.split(f)
        basename = getbasepath[0]
        foldername = os.path.split(basename)
        datadestinationpath = datafolderpath + foldername[1] +'/'+ os.path.split(os.path.splitext(f)[0])[1]+ ".txt"
             
        createfolder = os.path.join(datafolderpath,foldername[1])
        createFolder(createfolder)
        
        file = open(f, "r+")
       # print(file)
        lines = [line.rstrip() for line in file]
       # skipinfo = lines[10:]
        filedata = open(datadestinationpath, "w")
       # head = "ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex 2048" + "\nproperty float x\nproperty float y\nproperty float z\nelement face 0\nproperty list uchar int vertex_indices\nend_header\n"
        
        for i in lines[:0]:
            filedata.write(i + '\n')
        
        for i in lines[0:]:
            firstline = i.split(' ')[0:6]
            firstline = ','.join(firstline)
           # file.seek(0)
           
            filedata.write(firstline.replace(',',' ') + '\n')
          
        filedata.close()    
        file.close()
           
    