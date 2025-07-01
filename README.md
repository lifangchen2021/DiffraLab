# DiffaLab
![DiffraLab Mascot](images/DiffraLab1.png)

A Python educational platform (DiffraLab) integrating BraggIt (Monte Carlo powder diffraction), ResoFox (instrumental resolution calculator), and G-Fitter (multi-peak Gaussian fitting) for neutron and X-ray diffraction simulation and analysis in physics education.

---

## ✨ Features

✅ **BraggIt:** Simulate powder diffraction patterns for different crystal structures and wavelength uncertainties using Monte Carlo methods.  
✅ **ResoFox:** Calculate instrumental resolution functions of neutron diffractometers based on Caglioti’s analytical model.  
✅ **G-Fitter:** Perform multi-peak Gaussian fitting on experimental or simulated diffraction data, extracting FWHM and peak centers.  
✅ **GUI-based** for direct operation without programming background, suitable for classroom demonstration and lab training.  
✅ Developed for physics and materials science education.

---

## 🎯 Target Users

- Undergraduate and graduate students in Physics, Materials Science, or related fields.
- Courses including:
  - Solid State Physics
  - Modern Physics Laboratory
  - Diffraction and Instrumental Analysis

---

## 🚀 Installation

### Requirements
- Python 3.9+
- Recommended: Windows 10/11 or Linux

### Install and Run

```bash
git clone https://github.com/lifangchen2021/DiffraLab.git
cd DiffraLab

# Install dependencies
pip install -r requirements.txt

# Run the GUI
python src/DiffraLab.py
```
---

## 📂 Folder Structure
```
DiffraLab/
├── docs/           # Tutorial and supporting documents
│   └── 教程_Exploring Diffraction and Instrumental Resolution with DiffraLab_中文_v2.docx
├── images/         # Mascot and GUI screenshots
│   └── DiffraLab1.png
├── src/            # Main Python source files
│   ├── DiffraLab.py
│   ├── BraggIt.py
│   ├── ResoFox_v1_frame.py
│   ├── GFitter.py
│   └── main_png.py
├── LICENSE
├── README.md
└── requirements.txt
```
---
## 🖥️ Quick Usage and Demonstration

Below are brief operation steps with screenshots to help you get started quickly:

### 1️⃣ BraggIt - Powder Diffraction Simulation

- Simulates powder diffraction patterns with customizable lattice parameters and wavelengths.
- Utilizes **Monte Carlo methods to generate diffraction patterns for cubic crystal systems (e.g., FCC, BCC)**.
- Supports input of different particle numbers and calculation times, with **animated visualization of the diffraction pattern generation process**, helping students understand virtual experiments and diffraction statistics.
- **Enables export of diffraction plots and 2θ-intensity data in Excel format**, allowing students to calculate peak resolution and perform Gaussian fitting analysis.
- Visualizes diffraction peaks and relative intensities to facilitate learning of Bragg's Law and the principles of powder diffraction.

![BraggIt](images/BraggIt_demo.png)

---

### 2️⃣ ResoFox - Instrumental Resolution Calculator

- Calculates the instrumental resolution function of neutron diffractometers based on the **Caglioti model**.
- Allows adjustment of collimator divergence and monochromator parameters to **visualize FWHM variations** under different conditions.
- **Supports exporting plots for comparison of results under different parameter settings**, helping students analyze how instrument configurations affect resolution.
- The console prints **detailed theoretical calculation data**, including relative neutron intensities, theoretical diffraction angles, FWHM, and resolution values for each setting, allowing in-depth analysis and validation.
- For a **more detailed tutorial and validation results**, please refer to the following repository: [https://github.com/lifangchen2021/ResoFox](https://github.com/lifangchen2021/ResoFox)

![ResoFox](images/ResoFox_demo.png)

---

### 3️⃣ G-Fitter - Multi-peak Gaussian Fitting

- Performs **multi-peak Gaussian fitting on simulated or experimental diffraction data**.
- Extracts peak positions and FWHM values for analysis and reporting.
- By clicking the **"Select File" button**, users can select the Excel file exported from BraggIt and **directly perform Gaussian fitting on the simulated diffraction results**.

![GFitter](images/GFitter_demo.png)


---
## 📘 Documentation
A complete tutorial is available:

📄 [中文教程：Exploring Diffraction and Instrumental Resolution with DiffraLab](docs/教程_Exploring Diffraction and Instrumental Resolution with DiffraLab_中文_v2.docx)

This tutorial guides instructors and students on using DiffraLab effectively in class or lab courses.

---

## 📝 Citation
If you use DiffraLab in your teaching, publication, or project, please cite:

Chen, L. F. (2025). DiffraLab: An Educational Platform for Neutron and X-ray Diffraction Simulation. GitHub. [https://github.com/lifangchen2021/DiffraLab](https://github.com/lifangchen2021/DiffaLab)

---

## 📜 License
Distributed under the MIT License. See LICENSE for details.

---

## 🤝 Contributions
Contributions to extend the tool, add educational modules, or support additional diffraction analysis are welcome. Please open an issue or pull request if you wish to contribute.

---

## ❤️ Acknowledgment
Developed to support physics and materials science education, helping students visually understand diffraction and instrumental resolution.

---







