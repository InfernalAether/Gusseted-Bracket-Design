# Parametric Gusseted Bracket Design & Structural Analysis

## Project Overview

This project involves the CAD design and simplified structural analysis of a gusseted mounting bracket made from 6061-T6 aluminum.

The bracket was modeled in SolidWorks and analyzed using Python to estimate its bending stress, shear stress, deflection, and factor of safety under an applied static load.

## Design Specifications

- Material: 6061-T6 Aluminum
- Base plate: 120 mm × 60 mm × 6 mm
- Vertical plate: 60 mm × 100 mm × 6 mm
- Overall height: 106 mm
- Gusset profile: 50 mm × 50 mm nominal
- Mounting holes: 6 × Ø8 mm
- Mass: 229.70 g

## Structural Analysis

### Analysis Overview

A simplified analytical beam model was developed in Python to evaluate the bracket's response to a downward applied load.

### Material Properties

| Property        |            Value |
| --------------- | ---------------: |
| Material        | 6061-T6 Aluminum |
| Young's Modulus |           69 GPa |
| Yield Strength  |          275 MPa |
| Density         |       2700 kg/m³ |

### Loading Conditions

- Applied load: 500 N downward
- Load distance: 120 mm
- Base plate width: 60 mm
- Base plate thickness: 6 mm

### Analytical Results

| Parameter                |     Result |
| ------------------------ | ---------: |
| Maximum Bending Moment   |     60 N·m |
| Maximum Bending Stress   | 166.67 MPa |
| Maximum Deflection       |    3.86 mm |
| Average Shear Stress     |   1.39 MPa |
| Maximum Shear Stress     |   2.08 MPa |
| Maximum Von Mises Stress | 166.67 MPa |
| Factor of Safety         |       1.65 |

### Stress Analysis Visualizations

The Python analysis generates four plots to illustrate the bracket's predicted structural response:

1. Bending Stress vs. Applied Load
2. Bracket Deflection vs. Applied Load
3. Factor of Safety vs. Applied Load
4. Von Mises Stress Distribution Through Plate Thickness

The generated plots are stored in the `results/` directory.

### Engineering Assumptions and Limitations

- The base plate is approximated as a rectangular cantilever beam.
- The load is assumed to act at the free end, 120 mm from the fixed support.
- The model assumes linear-elastic material behavior.
- The gusset, mounting holes, fillets, and local stress concentrations are not explicitly modeled in the analytical calculations.
- The model does not account for bolt flexibility, contact behavior, or actual load sharing between the gusset and plates.
- This analysis is not a substitute for a three-dimensional finite element analysis (FEA).

The results provide an initial analytical estimate of structural behavior under the specified loading conditions. They should not be interpreted as validated design allowables.

## Tools Used

- SolidWorks — 3D modeling and engineering drawing
- Python — Structural calculations and visualization
- NumPy — Numerical calculations
- Matplotlib — Engineering plots
- Git — Version control
