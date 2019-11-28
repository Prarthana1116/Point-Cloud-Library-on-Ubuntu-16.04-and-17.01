#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:51:03 2018

@author: misumi
"""

from struct import unpack
import math
import os
from pathlib import Path
from shutil import copyfile

try:
    import numpy as np
except ImportError:
    print('numpy is required to enable STL transformation.')

class _STLFile(object):
    name = None
    transformation = None

    def __init__(self, filename, name=None, transformation=None):
        self.filename = filename
        if name is not None:
            self.name = name
        if transformation is not None:
            self.transformation = transformation

    def transform_vert(self, vert):
        tra = np.array(self.transformation)
        vert = np.array([[vert[0]],
                         [vert[1]],
                         [vert[2]],
                         [1]])
        vert = tra.dot(vert)
        return np.array(vert).flatten()[:-1]

    def __iter__(self):
        itr = self.read_vectors()
        while True:
            n = next(itr)
            verts = [next(itr), next(itr), next(itr)]
            if self.transformation is not None:
                verts = [self.transform_vert(v) for v in verts]
            yield n, verts[0], verts[1], verts[2]

    def read_vectors(self):
        raise NotImplementedError()

    def to_obj(self, obj, name=None, offset=0):
        obj.write('g default\n')
        vert_str = 'v {0:6f} {1:6f} {2:6f}\n'
        count = 0
        for face in self:
            obj.write(vert_str.format(*face[1]))
            obj.write(vert_str.format(*face[2]))
            obj.write(vert_str.format(*face[3]))
            count += 3
        name = name or self.name or 'default'
        obj.write('s 1\ng %s\n' % name)
        for i in range(offset, offset + count, 3):
            obj.write('f %s %s %s\n' % (i+1, i+2, i+3))
        return count

    def to_ascii(self, stlfile, name=None):
        name = name or self.name or 'default'
        stlfile.write('solid %s\n' % name)
        for face in self:
            stlfile.write('facet normal {:6f} {:6f} {:6f}\n'.format(*face[0]))
            stlfile.write('outer loop\n')
            stlfile.write('vertex {:6f} {:6f} {:6f}\n'.format(*face[1]))
            stlfile.write('vertex {:6f} {:6f} {:6f}\n'.format(*face[2]))
            stlfile.write('vertex {:6f} {:6f} {:6f}\n'.format(*face[3]))
            stlfile.write('endloop\n')
            stlfile.write('endfacet\n')
        stlfile.write('endsolid %s\n' % name)


class AsciiSTLFile(_STLFile):
    name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)export PATH=~/anaconda3/bin:$PATH

        if self.name is None:
            self.name = self.read_name()

    def read_name(self):
        with open(self.filename) as stlfile:
            line = next(stlfile)
            name = line.split(' ', 1)[1]
        return name

    def read_vectors(self):
        with open(self.filename) as stlfile:
            name = self.read_name()
            if self.name is None:
                self.name = name
            line = next(stlfile).strip()
            while line.startswith('facet normal'):
                # facet normal # # #
                yield [float(n) for n in line.split()[-3:]]
                next(stlfile) # outer loop
                for ___ in range(3): # vertex # # # (x3)
                    verts = next(stlfile).strip().split()[-3:]
                    yield [float(v) for v in verts]
                next(stlfile) # endloop
                next(stlfile) # endfacetoutputfilename
                line = next(stlfile).strip()


class BinarySTLFile(_STLFile):
    def read_vectors(self):
        with open(self.filename, 'rb') as stlfile:
            stlfile.seek(80)
            length = unpack('<I', stlfile.read(4))[0]

            for ___ in range(length):
                 # Normal, V1, V2, V3
                yield unpack('3f', stlfile.read(12))
                yield unpack('3f', stlfile.read(12))
                yield unpack('3f', stlfile.read(12))
                yield unpack('3f', stlfile.read(12))
                stlfile.seek(2, 1)

def open_stl(filename, *args, **kwargs):
    try:
        with open(filename) as stlfile:
            word = stlfile.readline(5)
            if word == 'solid':
                return AsciiSTLFile(filename, *args, **kwargs)
    except UnicodeDecodeError:
        pass
    return BinarySTLFile(filename, *args, **kwargs)

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

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
     
#Prarthana Modification
def stl_objConversion():    
    # http://www.lfd.uci.edu/~gohlke/code/transformations.py.html
    import transformations as t_

    inputpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/STL"
    outputpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/OBJ"
    listofinputfiles = getListOfFiles(inputpath)

    
    for f in listofinputfiles:
#        for file in f:
        if ".STL" in f:
            _ftemp = f.replace(" ", "")
            getbasepath = os.path.split(_ftemp)
            basename = getbasepath[0]
            foldername = os.path.split(basename)
            
            createfolder = os.path.join(outputpath,foldername[1])

            outputfilename = os.path.join(createfolder,Path(_ftemp).name.split('.')[0] + ".obj")
            print(outputfilename)
            createFolder(createfolder)
            stl = open_stl(f)
         
            with open(outputfilename, 'w') as obj:
                tra = t_.compose_matrix(
                    scale=[0.5, 0.5, 0.5],
                    translate=[-2, 1, 2],
                    angles=[math.pi/4, 0, math.pi/5])
                print(tra)
                stl.transformation = tra
                stl.to_obj(obj)
                
def obj_pcdConversion():
    
    objfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/OBJ"
    pcdfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PCD"
    
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
    
            os.system("pcl_mesh_sampling "+f +" " + outfilename +" -n_lsamples 2048 -leaf_size 0.001 -write_normals -no_vis_result")
    
            print("pcl_mesh_sampling "+f +" " + outfilename +" -n_samples 2048 -leaf_size 0.001 -write_normals -no_vis_result")
    
def pcd_plyConversion():
    
    pcdfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PCD"
    plyfolderpath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/PLY/"
    
    pcdfilenames = getListOfFiles(pcdfolderpath)   # get all files and folders name in the current directory
       
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
    
if __name__ == '__main__':
    stl_objConversion()
    obj_pcdConversion()
    pcd_plyConversion()
    