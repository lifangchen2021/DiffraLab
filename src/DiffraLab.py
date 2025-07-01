# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 11:01:38 2025

@author: user
"""

import tkinter as tk
from tkinter import ttk
from BraggIt import BraggItFrame
from ResoFox_v1_frame import create_resofox_frame
from GFitter import create_gfitter_frame  

class DiffraLabApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DiffraLab - Neutron Diffraction Lab Suite")
        self.geometry("1200x1000")

        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)

        # Tab 1 : BraggIt
        tab1 = BraggItFrame(notebook)
        tab1.pack(fill="both", expand=True)
        notebook.add(tab1, text="Bragg It!")

        #Tab 2 : ResoFox
        tab2 = ttk.Frame(notebook)
        create_resofox_frame(tab2)  
        notebook.add(tab2, text="ResoFox")
        
        # Tab 3 : G_Fitter
        tab3 = ttk.Frame(notebook)
        create_gfitter_frame(tab3)
        notebook.add(tab3, text="G-Fitter")


if __name__ == "__main__":
    app = DiffraLabApp()
    app.mainloop()
