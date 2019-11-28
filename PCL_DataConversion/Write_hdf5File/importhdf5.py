#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:26:38 2018

@author: misumi
"""
import h5py
#filename = '/home/misumi/Desktop/pointnet2-master/data/modelnet40_ply_hdf5_2048/ply_data_test0.h5'
filename = '/home/misumi/Desktop/pointnet-master/data/modelnet40_ply_hdf5_2048/ply_data_test1.h5'
f = h5py.File(filename, 'r')

# List all groups
print("Keys: %s" % f.keys())
a_group_key = list(f.keys())[0]
b_group_key = list(f.keys())[1]
c_group_key = list(f.keys())[2]
d_group_key = list(f.keys())[3]

# Get the data
data = list(f[a_group_key])
faceid = list(f[b_group_key])
label = list(f[c_group_key])
normal = list(f[d_group_key])

