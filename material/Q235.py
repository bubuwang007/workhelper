
class Q235:
    """kg N m s"""

    type = "solid"
    density = 7850
    elastic_modulus = 2.06e11
    poissons_ratio = 0.3
    alpha = 1.2e-5

    yield_strength = 215
    ultimate_tensile_strength = 370

    def equivalent_density(self, area, multi, light_weight):
        return self.density * multi + light_weight / area