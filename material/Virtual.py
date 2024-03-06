class Virtual:
    type = "virtual"
    density = 0
    alpha = 0
    elastic_modulus = 2e15
    poissons_ratio = 0.3
    ultimate_tensile_strength = 1e15
    yield_strength = 1e15

    def equivalent_density(self, *args):
        return 0