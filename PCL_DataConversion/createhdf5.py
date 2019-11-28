#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 15:59:10 2018

@author: misumi
"""

import h5py
import numpy as np
from plyfile import PlyData, PlyElement
import csv
import random

datapath = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/"
filelist_ply = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/filelist_ply.txt"
filenames_ply = [line.rstrip() for line in open(filelist_ply, 'r')]
filelabel = "/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/uLabel.txt"

ftrain = h5py.File("/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/data_training1.h5", 'w')
ftest = h5py.File("/home/misumi/Desktop/PCLDevelopment_ConversionTool/Data/MisumiData/Cantilever/data_testing1.h5", 'w')

dictionary=[] 
with open(filelabel, 'rt') as labelfile: 
    reader = csv.reader(labelfile,delimiter=":") 
    for row in reader:           
        Dict = {} 
        Dict['Name']=row[0].strip()
        Dict['Label']=row[1].strip()      
        dictionary.append(Dict)

def GetFileLabel(filename): 
    data=[item for item in dictionary if item['Name']==str(filename)] 
    if len(data)>0: 
         return str(data[0]['Label'])     
     
def shufflevalue():
    listvalue = [i for i in range(len(filenames_ply))]
    random.shuffle(listvalue)
    return listvalue



shufflevalues = shufflevalue()
trainvalue =  shufflevalues[:6000] 
testvalue = shufflevalues[6000:]    


data_data = np.zeros((len(trainvalue), 2048, 3))
face_data = np.zeros((len(trainvalue), 2048), dtype = np.uint8)	 #np.zeros((2048, 1), dtype = np.uint8)
label_data = np.zeros((len(trainvalue), 1), dtype = np.uint8)
normal_data = np.zeros((len(trainvalue), 2048, 3))

data_data_test = np.zeros((len(testvalue), 2048, 3))
face_data_test = np.zeros((len(testvalue), 2048), dtype = np.uint8)	 #np.zeros((2048, 1), dtype = np.uint8)
label_data_test = np.zeros((len(testvalue), 1), dtype = np.uint8)
normal_data_test = np.zeros((len(testvalue), 2048, 3))

train_k=0
test_k=0   
for i in range(0, len(filenames_ply)):
    if i in trainvalue:
        plydata = PlyData.read(datapath +"uData/" + filenames_ply[i] + ".ply")
        faceiddata = [line.rstrip() for line in open(datapath+"uFaceData/" + filenames_ply[i] + ".txt", 'r')]
        normaldata = PlyData.read(datapath +"uNormalData/" + filenames_ply[i] + ".ply")
        filenameValue = filenames_ply[i].split('/')[1]
        labelValue = GetFileLabel(filenameValue)
        
        for j in range(0, 2048):
            data_data[train_k, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
            face_data[train_k,j] = faceiddata[j]
            label_data[train_k] = labelValue
            normal_data[train_k,j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
        train_k=train_k+1
    else:
        plydata = PlyData.read(datapath +"uData/" + filenames_ply[i] + ".ply")
        faceiddata = [line.rstrip() for line in open(datapath+"uFaceData/" + filenames_ply[i] + ".txt", 'r')]
        normaldata = PlyData.read(datapath +"uNormalData/" + filenames_ply[i] + ".ply")
        filenameValue = filenames_ply[i].split('/')[1]
        labelValue = GetFileLabel(filenameValue)
        
        for j in range(0, 2048):
            data_data_test[test_k, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
            face_data_test[test_k,j] = faceiddata[j]
            label_data_test[test_k] = labelValue
            normal_data_test[test_k,j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
        test_k=test_k+1



train_data = ftrain.create_dataset("data", data = data_data)
train_face = ftrain.create_dataset("face", data = face_data)
train_label = ftrain.create_dataset("label", data = label_data)
train_normal = ftrain.create_dataset("normal", data = normal_data)

ftrain.close()

test_data = ftest.create_dataset("data", data = data_data_test)
test_face = ftest.create_dataset("face", data = face_data_test)
test_label = ftest.create_dataset("label", data = label_data_test)
test_normal = ftest.create_dataset("normal", data = normal_data_test)

ftest.close()