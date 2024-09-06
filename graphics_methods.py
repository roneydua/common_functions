#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   graphics_methods.py
@Time    :   2024/08/27 14:37:24
@Author  :   Roney D. Silva
@Contact :   roneyddasilva@gmail.com
'''
import matplotlib.pyplot as plt

meter_per_second_squared = "\\unit{\\meter\\per\\second\\squared}"
time_in_second = "\\unit{\\second}"
time_in_hour = "\\unit{\\hour}"

def set_xlabel_time(_ax:plt.axes,unit:str):
    if unit == 'second':
        _ax.set_xlabel(r'Tempo $[\unit{\second}]$')
    elif unit == 'millisecond':
        _ax.set_xlabel(r'Tempo $[\unit{\mili\second}]$')
    elif unit == "hour":
        _ax.set_xlabel(r"Tempo $[\unit{\hour}]$")


def set_ylabel_loop(_ax:plt.axes,names=['x','y','z'],unit=''):
    for i in range(len(names)):
        if unit != '':
            _unit = "["+unit+"]"
        _ax[i].set_ylabel(names[i]+unit)
