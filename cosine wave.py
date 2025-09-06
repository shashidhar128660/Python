# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 21:32:47 2025

@author: shashidhar
"""

import numpy as np
import matplotlib.pyplot as plt

def cosine_wave(A, f, phi, t):
    """
    Generates a cosine wave signal.

    Parameters:
        A (float): Amplitude of the cosine wave
        f (float): Frequency of the cosine wave in Hz
        phi (float): Phase shift in radians
        t (numpy.ndarray): Time vector

    Returns:
        numpy.ndarray: Cosine wave signal
    """
    return A * np.cos(2 * np.pi * f * t + phi)

# Example usage
A = 2.0        # Amplitude
f = 5.0        # Frequency in Hz
phi = np.pi/4  # Phase shift (45 degrees in radians)
t = np.linspace(0, 1, 1000)  # Time vector from 0 to 1 sec with 1000 samples

# Generate cosine wave
signal = cosine_wave(A, f, phi, t)

# Plot the cosine wave
plt.plot(t, signal, label="Cosine Wave", color='orange')
plt.title("Cosine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
