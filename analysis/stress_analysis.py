"""
Gusseted Bracket — Stress Analysis
Project 3: Mechanical Engineering Portfolio

Bending stress response under varying applied loads.
"""

import matplotlib.pyplot as plt
import numpy as np

# MATERIAL AND GEOMETRY

youngs_modulus = 69_000e6  # Pa
base_length = 120e-3  # m
base_width = 60e-3  # m
base_thickness = 6e-3  # m

# CROSS SECTION PROPERTIES

second_moment_area = (base_width * base_thickness**3) / 12

# APPLIED LOAD RANGE

load_values = np.linspace(0, 1000, 100)

# BENDING STRESS CALCULATION

bending_moments = load_values * base_length
bending_stresses = (bending_moments * (base_thickness / 2)) / second_moment_area

# DEFLECTION CALCULATION

deflections = (load_values * base_length**3) / (3 * youngs_modulus * second_moment_area)
deflections_mm = deflections * 1000

# FACTOR OF SAFETY CALCULATION

yield_strength = 275e6  # Pa

factor_of_safety_values = yield_strength / bending_stresses
factor_of_safety_values[0] = np.inf

# CONVERT TO MPa

bending_stresses_mpa = bending_stresses / 1e6

# PLOT

plt.figure(figsize=(9, 6))
plt.plot(load_values, bending_stresses_mpa, label="Bending Stress", linewidth=2)

yield_strength = 275  # MPa
plt.axhline(y=yield_strength, linestyle="--", label="Material Yield Strength")

plt.xlabel("Applied Load (N)")
plt.ylabel("Bending Stress (MPa)")
plt.title("Bending Stress vs. Applied Load")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("results/bending_stress_vs_load.png", dpi=300, bbox_inches="tight")

plt.show()


# CREATE DEFLECTION PLOT

plt.figure(figsize=(9, 6))

plt.plot(load_values, deflections_mm, label="Tip Deflection", linewidth=2)

plt.axvline(x=500, linestyle="--", label="Design Load (500 N)")

plt.xlabel("Applied Load (N)")
plt.ylabel("Deflection (mm)")
plt.title("Bracket Deflection vs. Applied Load")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("results/deflection_vs_load.png", dpi=300, bbox_inches="tight")

plt.show()


# CREATE FACTOR OF SAFETY PLOT

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

plt.savefig("results/factor_of_safety_vs_load.png", dpi=300, bbox_inches="tight")

plt.show()
