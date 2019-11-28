import os
from shutil import copyfile
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


plyfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PLY/"
normalfolderpath = '/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/uNormalData/'
facefolderpath = '/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/uFaceData/'

 # get all files and folders name in the current directory
plyfilenames = getListOfFiles(plyfolderpath) 

for f in plyfilenames:    #loop through all the files and folders
    if ".ply" in f:
        getbasepath = os.path.split(f)
        basename = getbasepath[0]
        foldername = os.path.split(basename)
        normaldestinationpath = normalfolderpath + foldername[1] +'/'+ os.path.split(os.path.splitext(f)[0])[1]+ ".ply"
             
        createfolder = os.path.join(normalfolderpath,foldername[1])
        createFolder(createfolder)
        
        file = open(f, "r+")
       # print(file)
        lines = [line.rstrip() for line in file]
        skipinfo = lines[10:]
        filedata = open(normaldestinationpath, "w")
        pcdinfo = lines[11:]
        filedata.seek(0)
        head = "ply\nformat ascii 1.0\ncomment VCGLIB generated\nelement vertex 2048" + "\nproperty float x\nproperty float y\nproperty float z\nelement face 0\nproperty list uchar int vertex_indices\nend_header\n"
        filedata.write(head)
        
#        for line in pcdinfo:
#            file.write(line+"\n")
        for eachline in skipinfo:
            splitarray = eachline.split(' ')
            normalvalue = splitarray[3:6]
            normalvalue = ','.join(normalvalue)
            #faceid =splitarray[-1]
            
            filedata.write(normalvalue.replace(',',' ') + '\n')
           # f.write(str(normalvalue).replace('[','').replace(']','').replace(',','').replace('\'','')+'\n')
            
        filedata.close()    
        file.close()
        
for f in plyfilenames:    #loop through all the files and folders
    if ".ply" in f:
        getbasepath = os.path.split(f)
        basename = getbasepath[0]
        foldername = os.path.split(basename)
        facedestinationpath = facefolderpath + foldername[1] +'/'+ os.path.split(os.path.splitext(f)[0])[1]+ ".txt"
             
        createfolder = os.path.join(facefolderpath,foldername[1])
        createFolder(createfolder)
        
        file = open(f, "r+")
        
        #print(file)
        lines = [line.rstrip() for line in file]
        skipinfo = lines[10:]
        filedata = open(facedestinationpath, "w")
        
        for eachline in skipinfo:
             splitarray = eachline.split(' ')
             faceid =splitarray[-1]
             filedata.write(faceid.replace(',',' ') + '\n')
         
        filedata.close()    
        file.close()       
        
      


