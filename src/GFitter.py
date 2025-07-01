# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 09:29:22 2025

@author: user
"""

#%%
# G_Fitter_frame.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy.ndimage import gaussian_filter1d
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def create_gfitter_frame(parent):
    # Global variables
    global file_path, x_data, y_data, peak_results, status_label, distance_entry, ax, canvas

    file_path = None
    x_data = None
    y_data = None
    peak_results = []

    # Outer frame for layout
    frame = tk.Frame(parent)
    frame.pack(fill='both', expand=True)

    # Left panel
    control_frame = tk.Frame(frame)
    control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    tk.Button(control_frame, text="Select File", command=choose_file).pack(pady=5)
    tk.Button(control_frame, text="Start Fitting", command=fit_and_plot).pack(pady=5)

    tk.Label(control_frame, text="Minimum Peak Distance (distance):").pack(pady=2)
    distance_entry = tk.Entry(control_frame)
    distance_entry.insert(0, "20")
    distance_entry.pack(pady=2)

    status_label = tk.Label(control_frame, text="No file selected", wraplength=180, justify='left')
    status_label.pack(pady=10)

    # Right panel for plot
    plot_frame = tk.Frame(frame)
    plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    
    

    fig = Figure(figsize=(7, 5))
    ax = fig.add_subplot(111)
#    fig, ax = plt.subplots(figsize=(7, 5))
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    return frame

def choose_file():
    global file_path, x_data, y_data
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        status_label.config(text=f"File selected: {file_path.split('/')[-1]}")
        df = pd.read_excel(file_path, skiprows=1)
        x_data = df.iloc[:, 0].to_numpy()
        y_data = df.iloc[:, 1].to_numpy()
    else:
        status_label.config(text="No file selected")

def gaussian(x, a, mu, sigma):
    return a * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def fit_and_plot():
    global peak_results
    if x_data is None or y_data is None:
        status_label.config(text="Please select a file first")
        return

    try:
        peak_distance = int(distance_entry.get())
    except ValueError:
        status_label.config(text="Please enter a valid integer for peak distance")
        return

    peak_results = []
    y_smooth = gaussian_filter1d(y_data, sigma=3)
    peaks, _ = find_peaks(y_smooth, height=max(y_smooth) * 0.01, distance=peak_distance)

    ax.clear()
    ax.plot(x_data, y_data, label='Raw Data', color='gray', alpha=0.5)

    for peak in peaks:
        N = 10
        left = max(0, peak - N)
        right = min(len(x_data), peak + N)
        x_fit = x_data[left:right]
        y_fit = y_data[left:right]

        a0 = y_data[peak]
        mu0 = x_data[peak]
        sigma0 = (x_fit[-1] - x_fit[0]) / 6
        try:
            popt, _ = curve_fit(gaussian, x_fit, y_fit, p0=[a0, mu0, sigma0])
            a, mu, sigma = popt
            peak_results.append((a, mu, sigma))
            x_dense = np.linspace(x_fit[0], x_fit[-1], 200)
            ax.plot(x_dense, gaussian(x_dense, *popt), label=f"2θ={mu:.2f}, σ={sigma:.2f}")
        except:
            print(f"Fitting failed at index {peak}")

    ax.scatter(x_data[peaks], y_data[peaks], color='red', zorder=10, label="Detected Peaks")
    ax.set_title("Multi-peak Gaussian Fitting")
    ax.set_xlabel("2θ (degree)")
    ax.set_ylabel("Intensity")
    ax.legend()
    ax.grid(True)
    canvas.draw()

    print("\nGaussian Fitting Results:")
    print("Peak | Intensity |  2θ |  σ |  FWHM")
    print("--------------------------------------------------")
    for i, (a, mu, sigma) in enumerate(peak_results):
        fwhm = 2.3548 * sigma
        print(f"{i+1:^5} | {a:7.2f} | {mu:7.2f} | {sigma:7.3f} | {fwhm:7.3f}")
