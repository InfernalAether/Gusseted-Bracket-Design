"""
Gusseted Bracket — Structural Analysis
Project 3: Mechanical Engineering Portfolio

Initial analytical model using a 500 N downward load.
"""

import numpy as np

# MATERIAL PROPERTIES

material = "6061-T6 Aluminum"

youngs_modulus = 69_000e6  # Pa
yield_strength = 275e6  # Pa
density = 2700  # kg/m^3

# BRACKET GEOMETRY

base_length = 120e-3  # m
base_thickness = 6e-3  # m

vertical_plate_height = 100e-3  # m
overall_height = 106e-3  # m
vertical_thickness = 6e-3  # m

gusset_height = 50e-3  # m
gusset_reach = 50e-3  # m

# LOADING CONDITIONS

applied_load = 500  # N, downward

load_distance = base_length

# BASE PLATE CROSS-SECTION

base_width = 60e-3  # m

second_moment_area = (base_width * base_thickness**3) / 12

max_bending_moment = applied_load * load_distance


def calculate_bending_stress(
    applied_load, load_distance, base_thickness, second_moment_area
):
    if applied_load < 0:
        raise ValueError("Applied load cannot be negative.")

    if load_distance <= 0:
        raise ValueError("Load distance must be positive.")

    if base_thickness <= 0 or second_moment_area <= 0:
        raise ValueError("Cross-section properties must be positive.")

    bending_moment = applied_load * load_distance

    bending_stress = (bending_moment * (base_thickness / 2)) / second_moment_area

    return bending_stress


max_bending_stress = calculate_bending_stress(
    applied_load, load_distance, base_thickness, second_moment_area
)

test_load = 750

test_bending_stress = calculate_bending_stress(
    test_load, load_distance, base_thickness, second_moment_area
)


def calculate_deflection(
    applied_load, load_distance, youngs_modulus, second_moment_area
):
    deflection = (applied_load * load_distance**3) / (
        3 * youngs_modulus * second_moment_area
    )

    return deflection


max_deflection = calculate_deflection(
    applied_load, load_distance, youngs_modulus, second_moment_area
)

test_deflection = calculate_deflection(
    test_load, load_distance, youngs_modulus, second_moment_area
)

# SHEAR STRESS ANALYSIS

cross_section_area = base_width * base_thickness
average_shear_stress = applied_load / cross_section_area
max_shear_stress = (3 / 2) * average_shear_stress

# VON MISES STRESS DISTRIBUTION

section_positions = np.linspace(-base_thickness / 2, base_thickness / 2, 1001)

bending_stress_distribution = (
    max_bending_moment * section_positions / second_moment_area
)

shear_stress_distribution = (
    1.5 * average_shear_stress * (1 - (2 * section_positions / base_thickness) ** 2)
)

von_mises_distribution = np.sqrt(
    bending_stress_distribution**2 + 3 * shear_stress_distribution**2
)

von_mises_stress = np.max(von_mises_distribution)

# FACTOR OF SAFETY


def calculate_factor_of_safety(yield_strength, bending_stress):
    if bending_stress <= 0:
        return float("inf")

    return yield_strength / bending_stress


factor_of_safety = calculate_factor_of_safety(yield_strength, max_bending_stress)


def calculate_combined_factor_of_safety(yield_strength, von_mises_stress):
    if von_mises_stress <= 0:
        return float("inf")

    return yield_strength / von_mises_stress


combined_factor_of_safety = calculate_combined_factor_of_safety(
    yield_strength, von_mises_stress
)

# DISPLAY INPUT SUMMARY

if __name__ == "__main__":
    print("GUSSETED BRACKET — STRUCTURAL ANALYSIS")
    print("--------------------------------------")
    print(f"Material: {material}")
    print(f"Young's Modulus: {youngs_modulus / 1e9:.1f} GPa")
    print(f"Yield Strength: {yield_strength / 1e6:.0f} MPa")
    print(f"Applied Load: {applied_load} N")
    print(f"Load Distance: {load_distance * 1000:.0f} mm")
    print("\nSTRUCTURAL ANALYSIS RESULTS")
    print("----------------------------")
    print(f"Second Moment of Area: {second_moment_area:.3e} m^4")
    print(f"Maximum Bending Moment: {max_bending_moment:.2f} N·m")
    print(f"Maximum Bending Stress: {max_bending_stress / 1e6:.2f} MPa")
    print(f"Stress at {test_load} N: {test_bending_stress / 1e6:.2f} MPa")
    print(f"Maximum Deflection: {max_deflection * 1000:.2f} mm")
    print(f"Deflection at {test_load} N: {test_deflection * 1000:.2f} mm")
    print(f"Cross-Section Area: {cross_section_area * 1e6:.2f} mm^2")
    print(f"Average Shear Stress: {average_shear_stress / 1e6:.2f} MPa")
    print(f"Maximum Shear Stress: {max_shear_stress / 1e6:.2f} MPa")
    print(f"Von Mises Stress: {von_mises_stress / 1e6:.2f} MPa")
    print(f"Factor of Safety: {factor_of_safety:.2f}")
    print(f"Combined Factor of Safety: {combined_factor_of_safety:.2f}")
