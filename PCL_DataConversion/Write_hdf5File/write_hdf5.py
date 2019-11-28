#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:07:06 2018

@author: misumi
"""

import h5py
import numpy as np
from plyfile import PlyData, PlyElement

filename1 = [line.rstrip() for line in open("/home/misumi/Desktop/Write_hdf5File/data/train1.txt", 'r')]
#filename2 = [line.rstrip() for line in open("/home/misumi/Desktop/Write_hdf5File/data/test2.txt", 'r')]
#filename3 = [line.rstrip() for line in open("/home/misumi/Desktop/Write_hdf5File/data/test3.txt", 'r')]
#filename4 = [line.rstrip() for line in open("/home/misumi/Desktop/Write_hdf5File/data/test4.txt", 'r')]
#filename5 = [line.rstrip() for line in open("/home/misumi/Desktop/Write_hdf5File/data/test5.txt", 'r')]

f1 = h5py.File("/home/misumi/Desktop/Write_hdf5File/hdf5_data/data_testtest1.h5", 'w')
#f2 = h5py.File("/home/misumi/Desktop/Write_hdf5File/hdf5_data/data_test2.h5", 'w')
#f3 = h5py.File("/home/misumi/Desktop/Write_hdf5File/hdf5_data/data_test3.h5", 'w')
#f4 = h5py.File("/home/misumi/Desktop/Write_hdf5File/hdf5_data/data_test4.h5", 'w')
#f5 = h5py.File("/home/misumi/Desktop/Write_hdf5File/hdf5_data/data_test5.h5", 'w')
#f = h5py.File("/home/misumi/Desktop/pointnet-master_misumi/misuminet5_ply_hdf5_2048/data_testing0.h5", 'w')

a_data1 = np.zeros((len(filename1), 2048, 3))
#a_data2 = np.zeros((len(filename2), 2048, 3))
#a_data3 = np.zeros((len(filename3), 2048, 3))
#a_data4 = np.zeros((len(filename4), 2048, 3))
#a_data5 = np.zeros((len(filename5), 2048, 3))
#a_pid = np.zeros((len(filenames), 2048), dtype = np.uint8)	

for i in range(0, len(filename1)):
	plydata = PlyData.read("/home/misumi/Desktop/Write_hdf5File/data/" + filename1[i])
	#piddata = [line.rstrip() for line in open("./points_label/" + filenames[i] + ".seg", 'r')]
	for j in range(0, 2048):
		a_data1[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
		#a_pid[i,j] = piddata[j]

data = f1.create_dataset("data1", data = a_data1)

#for i in range(0, len(filename2)):
#	plydata = PlyData.read("/home/misumi/Desktop/Write_hdf5File/data/" + filename2[i])
#	#piddata = [line.rstrip() for line in open("./points_label/" + filenames[i] + ".seg", 'r')]
#	for j in range(0, 2048):
#		a_data2[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
#		#a_pid[i,j] = piddata[j]
#
#data = f2.create_dataset("data2", data = a_data2)
#
#for i in range(0, len(filename3)):
#	plydata = PlyData.read("/home/misumi/Desktop/Write_hdf5File/data/" + filename3[i])
#	#piddata = [line.rstrip() for line in open("./points_label/" + filenames[i] + ".seg", 'r')]
#	for j in range(0, 2048):
#		a_data3[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
#		#a_pid[i,j] = piddata[j]
#
#data = f3.create_dataset("data2", data = a_data2)
#
#for i in range(0, len(filename4)):
#	plydata = PlyData.read("/home/misumi/Desktop/Write_hdf5File/data/" + filename4[i])
#	#piddata = [line.rstrip() for line in open("./points_label/" + filenames[i] + ".seg", 'r')]
#	for j in range(0, 2048):
#		a_data4[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
#		#a_pid[i,j] = piddata[j]
#
#data = f4.create_dataset("data2", data = a_data2)
#
#for i in range(0, len(filename5)):
#	plydata = PlyData.read("/home/misumi/Desktop/Write_hdf5File/data/" + filename5[i])
#	#piddata = [line.rstrip() for line in open("./points_label/" + filenames[i] + ".seg", 'r')]
#	for j in range(0, 2048):
#		a_data5[i, j] = [plydata['vertex']['x'][j], plydata['vertex']['y'][j], plydata['vertex']['z'][j]]
#		#a_pid[i,j] = piddata[j]
#
#data = f5.create_dataset("data2", data = a_data2)

#pid = f.create_dataset("pid", data = a_pid)