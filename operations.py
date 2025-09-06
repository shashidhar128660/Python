# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 12:05:23 2025

@author: Paravathi
"""

import numpy as np

def time_shift(signal, k):
    return np.roll(signal, k)

def time_scale(signal, k):
    n = len(signal)
    scaled_signal = np.interp(np.linspace(0, n-1, int(n/k)), np.arange(n), signal)
    return scaled_signal

def signal_addition(signal1, signal2):

    if len(signal1) != len(signal2):
        raise ValueError("Signals must have the same length")
    return signal1 + signal2

def signal_multiplication(signal1, signal2):
    if len(signal1) != len(signal2):
        raise ValueError("Signals must have the same length")
    return signal1 * signal2

# Example usage:
if __name__ == "_main_":    
    t = np.linspace(0, 10, 1000) 
    signal1 = np.sin(t)  
    signal2 = np.cos(t)

    shifted_signal = time_shift(signal1, 100)
    scaled_signal = time_scale(signal1, 2)
    added_signal = signal_addition(signal1, signal2)
    multiplied_signal = signal_multiplication(signal1, signal2)

   
    print("Shifted Signal: ", shifted_signal[:10]) 
    print("Scaled Signal: ", scaled_signal[:10])  
    print("Added Signal: ", added_signal[:10])  
    print("Multiplied Signal: ", multiplied_signal[:10])