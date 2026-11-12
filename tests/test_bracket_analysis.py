"""
Gusseted Bracket — Unit Tests
Project 3: Mechanical Engineering Portfolio
"""

import unittest

from analysis import bracket_analysis


class TestBracketAnalysis(unittest.TestCase):
    def test_second_moment_of_area(self):
        self.assertAlmostEqual(bracket_analysis.second_moment_area, 1.08e-9, places=15)

    def test_maximum_bending_moment(self):
        self.assertAlmostEqual(bracket_analysis.max_bending_moment, 60.0, places=2)

    def test_maximum_bending_stress(self):
        self.assertAlmostEqual(
            bracket_analysis.max_bending_stress / 1e6, 166.67, places=2
        )

    def test_maximum_deflection(self):
        self.assertAlmostEqual(bracket_analysis.max_deflection * 1000, 3.86, places=2)

    def test_average_shear_stress(self):
        self.assertAlmostEqual(
            bracket_analysis.average_shear_stress / 1e6, 1.3889, places=3
        )

    def test_maximum_shear_stress(self):
        self.assertAlmostEqual(
            bracket_analysis.max_shear_stress / 1e6, 2.0833, places=3
        )

    def test_factor_of_safety(self):
        self.assertAlmostEqual(bracket_analysis.factor_of_safety, 1.65, places=2)

    def test_combined_factor_of_safety(self):
        self.assertAlmostEqual(
            bracket_analysis.combined_factor_of_safety, 1.65, places=2
        )

    def test_reusable_bending_stress(self):
        stress = bracket_analysis.calculate_bending_stress(
            750,
            bracket_analysis.load_distance,
            bracket_analysis.base_thickness,
            bracket_analysis.second_moment_area,
        )

        self.assertAlmostEqual(stress / 1e6, 250.0, places=2)

    def test_reusable_deflection(self):
        deflection = bracket_analysis.calculate_deflection(
            750,
            bracket_analysis.load_distance,
            bracket_analysis.youngs_modulus,
            bracket_analysis.second_moment_area,
        )

        self.assertAlmostEqual(deflection * 1000, 5.80, places=2)

    def test_reusable_factor_of_safety(self):
        stress = bracket_analysis.calculate_bending_stress(
            750,
            bracket_analysis.load_distance,
            bracket_analysis.base_thickness,
            bracket_analysis.second_moment_area,
        )

        safety_factor = bracket_analysis.calculate_factor_of_safety(
            bracket_analysis.yield_strength, stress
        )

        self.assertAlmostEqual(safety_factor, 1.10, places=2)

    def test_negative_load_rejected(self):
        with self.assertRaises(ValueError):
            bracket_analysis.calculate_bending_stress(
                -500,
                bracket_analysis.load_distance,
                bracket_analysis.base_thickness,
                bracket_analysis.second_moment_area,
            )


if __name__ == "__main__":
    unittest.main()
