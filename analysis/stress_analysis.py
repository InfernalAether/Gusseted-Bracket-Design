"""
Gusseted Bracket — Stress Analysis
Project 3: Mechanical Engineering Portfolio

Stress, deflection, and factor-of-safety visualizations.
"""

import matplotlib.pyplot as plt
import numpy as np

from analysis import bracket_analysis as bracket

# APPLIED LOAD RANGE

load_values = np.linspace(0, 1000, 100)

# BENDING STRESS CALCULATION

bending_moments = load_values * bracket.load_distance

bending_stresses = (
    bending_moments * (bracket.base_thickness / 2)
) / bracket.second_moment_area

bending_stresses_mpa = bending_stresses / 1e6

# DEFLECTION CALCULATION

deflections = (load_values * bracket.load_distance**3) / (
    3 * bracket.youngs_modulus * bracket.second_moment_area
)

deflections_mm = deflections * 1000

# FACTOR OF SAFETY CALCULATION

factor_of_safety_values = bracket.yield_strength / bending_stresses

factor_of_safety_values[0] = np.inf

# BENDING STRESS PLOT

plt.figure(figsize=(9, 6))

plt.plot(load_values, bending_stresses_mpa, label="Bending Stress", linewidth=2)

plt.axhline(
    y=bracket.yield_strength / 1e6, linestyle="--", label="Material Yield Strength"
)

plt.xlabel("Applied Load (N)")
plt.ylabel("Bending Stress (MPa)")
plt.title("Bending Stress vs. Applied Load")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("results/bending_stress_vs_load.png", dpi=300)
plt.show()

# DEFLECTION PLOT

plt.figure(figsize=(9, 6))

plt.plot(load_values, deflections_mm, label="Tip Deflection", linewidth=2)

plt.axvline(x=500, linestyle="--", label="Design Load (500 N)")

plt.xlabel("Applied Load (N)")
plt.ylabel("Deflection (mm)")
plt.title("Bracket Deflection vs. Applied Load")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("results/deflection_vs_load.png", dpi=300)
plt.show()

# FACTOR OF SAFETY PLOT

plt.figure(figsize=(9, 6))

plt.plot(load_values, factor_of_safety_values, label="Factor of Safety", linewidth=2)

plt.axhline(y=1.0, linestyle="--", label="Yield Threshold (FoS = 1)")
plt.axvline(x=500, linestyle=":", label="Design Load (500 N)")

plt.xlabel("Applied Load (N)")
plt.ylabel("Factor of Safety")
plt.title("Factor of Safety vs. Applied Load")
plt.ylim(0, 5)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("results/factor_of_safety_vs_load.png", dpi=300)
plt.show()


# VON MISES STRESS DISTRIBUTION

section_positions = np.linspace(
    -bracket.base_thickness / 2, bracket.base_thickness / 2, 1001
)

bending_stress_distribution = (
    bracket.max_bending_moment * section_positions / bracket.second_moment_area
)

average_shear_stress = bracket.applied_load / (
    bracket.base_width * bracket.base_thickness
)

shear_stress_distribution = (
    1.5
    * average_shear_stress
    * (1 - (2 * section_positions / bracket.base_thickness) ** 2)
)

von_mises_distribution = np.sqrt(
    bending_stress_distribution**2 + 3 * shear_stress_distribution**2
)

von_mises_mpa = von_mises_distribution / 1e6

# PLOT VON MISES STRESS

plt.figure(figsize=(9, 6))

plt.plot(section_positions * 1000, von_mises_mpa, label="Von Mises Stress", linewidth=2)

plt.xlabel("Position Through Plate Thickness (mm)")
plt.ylabel("Von Mises Stress (MPa)")
plt.title("Von Mises Stress Distribution Through Plate Thickness")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("results/von_mises_stress_distribution.png", dpi=300)
plt.show()
