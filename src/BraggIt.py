# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 14:56:48 2025
@author: user

"""
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import random
import numpy as np
import time  
from tkinter import filedialog
import pandas as pd


def BraggItFrame(parent):
    frame = tk.Frame(parent)
    
    # Constant Setting
    lattice_anguler_alpha = 90
    lattice_anguler_beta = 90
    lattice_anguler_gamma = 90
    Pi = math.pi

    # Trigonometric Calculation
    cos_alpha_star = (
        math.cos(lattice_anguler_beta/180*Pi) * math.cos(lattice_anguler_gamma/180*Pi)
        - math.cos(lattice_anguler_alpha/180*Pi)
    ) / (math.sin(lattice_anguler_beta/180*Pi) * math.sin(lattice_anguler_gamma/180*Pi))
    cos_beta_star = (
        math.cos(lattice_anguler_alpha/180*Pi) * math.cos(lattice_anguler_gamma/180*Pi)
        - math.cos(lattice_anguler_beta/180*Pi)
    ) / (math.sin(lattice_anguler_alpha/180*Pi) * math.sin(lattice_anguler_gamma/180*Pi))
    cos_gamma_star = (
        math.cos(lattice_anguler_alpha/180*Pi) * math.cos(lattice_anguler_beta/180*Pi)
        - math.cos(lattice_anguler_gamma/180*Pi)
    ) / (math.sin(lattice_anguler_alpha/180*Pi) * math.sin(lattice_anguler_beta/180*Pi))

    # Dictionary of field values
    inputs = {}

    fields = [
        ("sample_name", "Sample Name", "Ag (FCC)"),
        ("a1", "Lattice Constant a1 (Å)", "4.07"),
        ("a2", "Lattice Constant a2 (Å)", "4.07"),
        ("a3", "Lattice Constant a3 (Å)", "4.07"),
        ("style", "Lattice Type (1:BCC 2:FCC)", "2"),
        ("wavelength", "Wavelength (Å)", "1.54"),
        ("delta", "Wavelength Uncertainty (±1σ) (%)", "5"),
        ("count", "Number of Simulated Particles", "500")
    ]
    for i, (key, label, default) in enumerate(fields):
        tk.Label(frame, text=label).grid(row=i, column=0, sticky='e')
        e = tk.Entry(frame)
        e.insert(0, default)
        e.grid(row=i, column=1)
        inputs[key] = e

    # Global Variable
    all_count = []

    # Canvas Setup
    figure = plt.Figure(figsize=(6,4))
    ax = figure.add_subplot(111)
    ax.set_title("Diffraction Simulation")
    ax.set_xlabel("2θ (degrees)")
    ax.set_ylabel("Relative Intensity")
    canvas = FigureCanvasTkAgg(figure, master=frame)
    canvas.get_tk_widget().grid(row=0, column=2, rowspan=len(fields), padx=10)

    # Wavelength Range Function
    def wave_lenth_range(lenda, delta):
        sigma = lenda * (delta / 100)
        return np.random.normal(loc=lenda, scale=sigma)

    # Interplanar Spacing Algorithm
    def lattice_distance(h, k, l, a1, a2, a3):
        return 1 / (
            (h/a1)**2 + (k/a2)**2 + (l/a3)**2
            + 2*(h/a1)*(k/a2)*cos_gamma_star
            + 2*(k/a2)*(l/a3)*cos_beta_star
            + 2*(l/a3)*(h/a1)*cos_beta_star
        )**0.5

    # Remove Duplicate Elements
    def delList(L):
        seen = []
        result = []
        for item in L:
            if item not in seen:
                seen.append(item)
                result.append(item)
        return result

    # Diffraction Calculation Function
    def diffraction_calculate(x_ray, a1, a2, a3, style_choose):
        total_peak_message = []
        for n in range(1, 3):
            for h in range(4):
                for k in range(4):
                    for l in range(4):
                        if h+k+l == 0:
                            continue
                        d = lattice_distance(h, k, l, a1, a2, a3)
                        if n * x_ray > 2 * d:
                            continue
                        cond = False
                        if style_choose == 1 and (h+k+l) % 2 == 0:
                            cond = True
                            
                        elif style_choose == 2 and (
                            (h+k in (2,4) or k+l in (2,4) or l+h in (2,4))
                            and (h%2 == k%2 == l%2)
                        ):
                            cond = True
                        elif style_choose == 3 and (h+k+l in (3,6)):
                            cond = True
                        if not cond:
                            continue
                        theta = math.degrees(math.asin(n*x_ray/(2*d)))
                        multiply_factor = 2**(
                            math.ceil(h/(h+1)) + math.ceil(k/(k+1)) + math.ceil(l/(l+1))
                        )
                        intensity = (
                            0.5 + 0.5 * math.cos(math.radians(2*theta))**2
                            / math.sin(math.radians(2*theta)) / math.sin(math.radians(theta))
                        ) * multiply_factor * math.exp(-n/d)
#                        total_peak_message.append((round(2*theta,3), round(intensity,3)))
                        total_peak_message.append((round(2*theta,3), round(intensity,3), (h, k, l)))
                      
#                        print("The diffraction peak of crystal plane (" + str(h) + str(k) + str(l) + ") at order " + str(n) + " appears at:", round(2 * theta, 3), "degrees")

        # Remove duplicates and return list
        return delList(total_peak_message)

    # Simulate button trigger (with animation effect)
    def on_simulate():
        # Read parameters
        a1 = float(inputs["a1"].get())
        a2 = float(inputs["a2"].get())
        a3 = float(inputs["a3"].get())
        style_choose = int(inputs["style"].get())
        lenda = float(inputs["wavelength"].get())
        delta = float(inputs["delta"].get())
        how_many_particles = int(inputs["count"].get())

        # Reset data and timer
        all_count.clear()
        processed = 0
        start_time = time.time()
        chunk_size = 50
        
        print("---------- Expected diffraction peaks (no wavelength error) ----------")
        expected_peaks = diffraction_calculate(lenda, a1, a2, a3, style_choose)
        for ang, inten, hkl in expected_peaks:
            h, k, l = hkl
            print(f"2θ = {ang:.3f}°, (hkl) = ({h} {k} {l}), Intensity = {inten:.2f}")
        print("---------------------------------------------------------------------")


        def run_chunk():
            nonlocal processed
            end = min(processed + chunk_size, how_many_particles)
            for _ in range(processed, end):
                x_ray = wave_lenth_range(lenda, delta)
                peaks = diffraction_calculate(x_ray, a1, a2, a3, style_choose)
                all_count.append(peaks)
            processed = end

            # Expand all_count
            all_count_2 = [p for grp in all_count for p in grp]
            # Calculate intensity distribution (resolution: 0.1°)
            angles = [i/10 for i in range(1800)]
            intensities = [
                sum(p[1] for p in all_count_2 if ang < p[0] <= ang + 0.1)
                for ang in angles
            ]

            

            # Update the chart (line plot only)
            ax.clear()
            sample_title = inputs["sample_name"].get()
            ax.set_title(f"Diffraction Simulation - {sample_title}")
            ax.set_xlabel("2θ (degrees)")
            ax.set_ylabel("Relative Intensity")
            ax.plot(angles, intensities, 'r-', linewidth=0.2)  
            ax.set_xlim(0, 180)
            ax.set_xticks(range(0, 180, 10))  
            # Set Y-axis range
            y_fixed_limit = 1000
            max_intensity = max(intensities)
            if max_intensity <= y_fixed_limit:
                ax.set_ylim(0, y_fixed_limit)
            else:
                ax.set_ylim(0, max_intensity * 1.1)  
            
            
            # Display time and particle count (top right)
            elapsed = time.time() - start_time
            ax.text(
                0.98, 0.98,
                f"Time: {elapsed:.1f}s | Particles: {processed}/{how_many_particles}",
                transform=ax.transAxes,
                ha='right', va='top',
                fontsize=8, backgroundcolor='white'
            )
            canvas.draw()

            if processed < how_many_particles:
                frame.after(100, run_chunk)

        run_chunk()

    def export_plot():
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Save Plot"
        )
        if filename:
            figure.savefig(filename, dpi=300)
            
    def export_binned_data_to_excel():
        if not all_count:
            tk.messagebox.showinfo("Notice", "Please run the simulation first!")
            return

        # Flatten all_count into a single list
        all_count_2 = [p for grp in all_count for p in grp]

        # Reconstruct bins
        angles = [i / 10 for i in range(1800)]  # 0 ~ 180，間距 0.1°
        intensities = [
            sum(inten for (ang_val, inten) in all_count_2 if ang < ang_val <= ang + 0.1)
            for ang in angles
        ]

        # Create DataFrame and export
        df = pd.DataFrame({
            "2θ (degrees)": angles,
            "Intensity": intensities
        })

        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            title="Export Diffraction Data"
        )

        if file_path:
            df.to_excel(file_path, index=False)
            tk.messagebox.showinfo("Success", f"Diffraction data has been saved to:\n{file_path}")



    # Set buttons
    simulate_button = tk.Button(frame, text="Start Simulation", command=on_simulate)
    simulate_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

    button_frame = tk.Frame(frame)
    button_frame.grid(row=len(fields), column=2, pady=5)

    # Export plot button (left)
    export_button = tk.Button(button_frame, text="Export Plot", command=export_plot)
    export_button.pack(side='left', padx=5)

    # Export binned diffraction data button (right)
    export_excel_button = tk.Button(button_frame, text="Export Diffraction Data", command=export_binned_data_to_excel)
    export_excel_button.pack(side='left', padx=5)

    return frame



