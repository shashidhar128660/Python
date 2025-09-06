# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 21:34:34 2025

@author: shashidhar
"""

import numpy as np

def exponential_signal(A, a, t):
    """
    Generates an exponential signal.
    
    Parameters:
        A (float): Amplitude (scaling factor).
        a (float): Exponential rate constant.
        t (array-like): Time vector.
    
    Returns:
        np.ndarray: Exponential signal A * e^(a*t).
    """
    t = np.array(t)
    return A * np.exp(a * t)

# Example usage
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    A = 1.0        # Amplitude
    a = 1.0        # Exponential rate constant
    t = np.linspace(0, 5, 1000)  # Time vector from 0 to 5 sec with 1000 samples

    # Generate exponential signal
    signal = exponential_signal(A, a, t)

    # Plot the exponential signal
    plt.plot(t, signal, label="Exponential Signal", color='blue')
    plt.title("Exponential Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

