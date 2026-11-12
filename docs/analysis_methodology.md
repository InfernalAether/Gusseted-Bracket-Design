# Gusseted Bracket — Analysis Methodology

## 1. Project Objective

The objective of this project is to design a gusseted aluminum mounting bracket and evaluate its structural response under an applied vertical load.

The project combines parametric CAD modeling, material selection, analytical stress calculations, Python-based numerical analysis, and engineering documentation.

## 2. Material Properties

The bracket uses 6061-T6 aluminum.

| Property        |      Value |
| --------------- | ---------: |
| Young's Modulus |     69 GPa |
| Yield Strength  |    275 MPa |
| Poisson's Ratio |       0.33 |
| Density         | 2700 kg/m³ |

## 3. Bracket Geometry

The bracket consists of a vertical mounting plate, a horizontal base plate, and a central triangular gusset.

| Parameter                | Dimension |
| ------------------------ | --------: |
| Base plate length        |    120 mm |
| Base plate width         |     60 mm |
| Base plate thickness     |      6 mm |
| Vertical plate height    |    100 mm |
| Overall bracket height   |    106 mm |
| Vertical plate thickness |      6 mm |
| Gusset nominal height    |     50 mm |
| Gusset nominal reach     |     50 mm |
| Mounting holes           | 6 × Ø8 mm |

## 4. Loading Conditions

A downward static load of 500 N is applied at the far end of the horizontal base plate.

For the initial analytical model, the bracket is simplified as a cantilever beam fixed at the mounting wall.

The load is assumed to act 120 mm from the fixed support.

## 5. Analytical Method

The horizontal base plate is approximated as a rectangular cantilever beam.

### Second Moment of Area

I = (b × h³) / 12

Where:

- b = 0.060 m
- h = 0.006 m

### Bending Moment

M = F × L

### Maximum Bending Stress

σ = M × c / I

Where c = h / 2.

### Maximum Tip Deflection

δ = (F × L³) / (3 × E × I)

### Average Shear Stress

τ = F / A

Where A is the rectangular cross-sectional area.

### Factor of Safety

FoS = σ_yield / σ_bending

## 6. Python Implementation

Python was used to automate the structural calculations and evaluate the bracket under different applied loads.

The analysis includes:

- Bending stress calculations
- Tip deflection calculations
- Average and maximum shear stress estimates
- Factor of safety calculations
- Load-dependent stress and deflection plots
- Unit tests for calculation functions and input validation

NumPy and Matplotlib were used for numerical calculations and visualization. Python's unittest framework was used to verify the analysis functions.

## 7. Model Assumptions and Limitations

This analysis uses a simplified cantilever beam approximation.

The model assumes:

- Linear elastic material behavior
- Static loading
- A rigidly fixed support
- A rectangular, uniform base plate cross-section
- A point load applied at the end of the base plate

The analytical model does not fully account for:

- Load sharing through the gusset
- Stress concentrations around mounting holes
- Local plate bending
- Bolt and wall compliance
- Three-dimensional stress distributions

The calculated stresses and deflections should therefore be interpreted as simplified analytical estimates rather than a complete prediction of the actual bracket's structural behavior.

No full three-dimensional finite element analysis was performed.

## 8. Analysis Results

Under the 500 N design load, the simplified analytical model produced:

| Result                         |      Value |
| ------------------------------ | ---------: |
| Bending moment                 |     60 N·m |
| Maximum bending stress         | 166.67 MPa |
| Maximum tip deflection         |    3.86 mm |
| Average shear stress           |   1.39 MPa |
| Maximum shear stress estimate  |   2.08 MPa |
| Bending-based factor of safety |       1.65 |

These results describe the simplified beam model and should not be interpreted as validated performance of the complete gusseted bracket.

## 9. Conclusion

The project demonstrates the use of parametric CAD, material properties, analytical structural calculations, Python programming, data visualization, and automated testing in a mechanical engineering design workflow.

Future improvements could include a more detailed structural model that accounts for gusset load sharing, mounting-hole effects, and three-dimensional stress distributions.
