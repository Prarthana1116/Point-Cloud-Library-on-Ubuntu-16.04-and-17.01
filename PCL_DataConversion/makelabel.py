#Misumi 18.11.15

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
            allFiles.append(entry)
                
    return allFiles       

def main():
    labelfolderpath = '/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PLY/'
    labeldestinationpath = labelfolderpath +"uLabel.txt"
    #filenames = getListOfFiles(labelfolderpath)   # get all files and folders name in the current directory
    listOffolder = os.listdir(labelfolderpath)
    filelist = open(labeldestinationpath, "w+")

    label = 0
    for fname in listOffolder:
        if os.path.isdir(os.path.join(labelfolderpath,fname)):
            files = getListOfFiles(os.path.join(labelfolderpath,fname))
            for name in files:
                name = name.split(".")
                filelist.write(name[0]+" : "+ str(label)+os.linesep)
        label = label+1
    
    filelist.close()
               
        
if __name__=="__main__":
    main()
           
      


