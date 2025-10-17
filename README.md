# Radius of Gyration Analysis after MD Simulation in GROMACS

This repo contains the python code for radius of gyration analysis using matplotlib after MD simulation in GROMACS. The protein of interest is [3FYR](https://www.rcsb.org/structure/3FYR).
Overview of 3FYR: Crystal structure of the sporulation histidine kinase inhibitor Sda from *Bacillus subtilis*

## Preparing 3FYR for simulation
1. Retained only chain A using the PyMol software
2. The 3FYE contained the MSE(Selenomethionine) which is not a standard residue. It was converted to MET(Methionine) using VIM editor and then processed using the tleap module of AMBER.
3. MD simulation of 1 ns was run using the GROMACS program.
