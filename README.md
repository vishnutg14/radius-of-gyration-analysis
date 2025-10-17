# Radius of Gyration Analysis after MD Simulation in GROMACS

This repo contains the Python code for radius of gyration analysis using matplotlib after MD simulation in GROMACS. The protein of interest is [3FYR](https://www.rcsb.org/structure/3FYR).
Overview of 3FYR: Crystal structure of the sporulation histidine kinase inhibitor Sda from *Bacillus subtilis*

## Preparing 3FYR for simulation
1. Retained only chain A using the PyMol software
2. The 3FYE contained the MSE(Selenomethionine) which is not a standard residue. It was converted to MET(Methionine) using the VIM editor and then processed using the tleap module of AMBER.
3. An MD simulation of 1 ns was run using the GROMACS program.

## Installation
1. Clone the repository
```
git clone https://github.com/vishnutg14/radius-of-gyration-analysis.git
```

2. Installing requirements
```
pip install -r requirements.txt
```

To use the script for your gyration analysis, change the `filename` variable in the `gyrate.py` to one of your `gyrate.xvg` file names and let the script do its magic!
