# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 12:04:08 2025

@author: Paravathi
"""

import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    signal = np.heaviside(n, 1)  
    plt.plot(n, signal, label="Unit Step Signal")
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()
    return signal

def unit_impulse(n):
    signal = np.zeros_like(n)
    signal[n == 0] = 1
    plt.stem(n, signal, basefmt=" ")  
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

def ramp_signal(n):
    signal = np.maximum(n, 0) 
    plt.plot(n, signal, label="Ramp Signal")
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()
    return signal
n = np.arange(-10, 11)  

unit_step(n)
unit_impulse(n)
ramp_signal(n)