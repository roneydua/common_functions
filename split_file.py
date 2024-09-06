#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   split_file.py
@Time    :   2024/08/23 13:54:40
@Author  :   Roney D. Silva
@Contact :   roneyddasilva@gmail.com
'''

import os

import h5py
import numpy as np

f = h5py.File('phd_data.hdf5','r')

ff = f['mounted_acc/acc_4/20240808/allan_variance']

if os.path.exists('allan_analysis'):
    os.removedirs('allan_analysis')
os.mkdir("allan_analysis")

def make_groups_and_dataset(ff,current_path):
    for i in ff.keys():
        if type(ff[i]) is h5py.Group:
            os.mkdir(current_path+"/"+i)
            make_groups_and_dataset(ff=ff[i], current_path=current_path + "/" + i)
        elif type(ff[i]) is h5py.Dataset:
            np.savetxt(current_path + "/" + i, ff[i])

make_groups_and_dataset(ff,'allan_analysis')

