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
git clone https://github.com/<your_username>/DiffraLab.git
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

- Simulate powder diffraction patterns with different lattice parameters and wavelengths.
- Visualize diffraction peaks and relative intensities for learning Bragg's Law.

![BraggIt](images/BraggIt_demo.png)

---

### 2️⃣ ResoFox - Instrumental Resolution Calculator

- Compute the instrumental resolution function of a neutron diffractometer based on the Caglioti model.
- Adjust collimator divergence and monochromator parameters to visualize FWHM changes.

![ResoFox](images/ResoFox_demo.png)

---

### 3️⃣ G-Fitter - Multi-peak Gaussian Fitting

- Perform multi-peak Gaussian fitting on simulated or experimental diffraction data.
- Extract peak positions and FWHM for analysis and reporting.

![GFitter](images/GFitter_demo.png)


---
## 📘 Documentation
A complete tutorial is available:

📄 [中文教程：Exploring Diffraction and Instrumental Resolution with DiffraLab](docs/教程_Exploring Diffraction and Instrumental Resolution with DiffraLab_中文_v2.docx)

This tutorial guides instructors and students on using DiffraLab effectively in class or lab courses.

---

## 📝 Citation
If you use DiffraLab in your teaching, publication, or project, please cite:

Chen, L. F. (2025). DiffraLab: An Educational Platform for Neutron and X-ray Diffraction Simulation. GitHub. https://github.com/lifangchen2021/DiffraLab

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







