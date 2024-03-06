class Cable_1670:

    type = "cable"
    density = 7850
    alpha = 1.2e-5
    elastic_modulus = 1.9e11
    poissons_ratio = 0.3
    ultimate_tensile_strength = 1670

    @property
    def yield_strength(self):
        """fy"""
        return self.ultimate_tensile_strength * 0.8

    def ultimate_N(self, A):
        """KN"""
        return round(self.ultimate_tensile_strength * A / 1000)

    def yield_N(self, A):
        """KN"""
        return round(self.yield_strength * A / 1000)
    
    def equivalent_density(self, area, multi, length, kg_per_m, light_weight, anchor_weight):
        return multi*((kg_per_m+light_weight)*length+anchor_weight)/area/length
   
class Cable_1770:

    type = "cable"
    density = 7850
    alpha = 1.2e-5
    elastic_modulus = 1.9e11
    poissons_ratio = 0.3
    ultimate_tensile_strength = 1770

    @property
    def yield_strength(self):
        """fy"""
        return self.ultimate_tensile_strength * 0.8

    def ultimate_N(self, A):
        """KN"""
        return round(self.ultimate_tensile_strength * A / 1000)

    def yield_N(self, A):
        """KN"""
        return round(self.yield_strength * A / 1000)
    
    def equivalent_density(self, area, multi, length, kg_per_m, light_weight, anchor_weight):
        return multi*((kg_per_m+light_weight)*length+anchor_weight)/area/length

class Cable_1280:
    type = "cable"
    density = 7850
    alpha = 1.2e-5
    elastic_modulus = 1.2e11
    poissons_ratio = 0.3
    ultimate_tensile_strength = 1280

    @property
    def yield_strength(self):
        """fy"""
        return self.ultimate_tensile_strength * 0.8
    
    def ultimate_N(self, A):
        """KN"""
        return round(self.ultimate_tensile_strength * A / 1000)
    
    def yield_N(self, A):
        """KN"""
        return round(self.yield_strength * A / 1000)
    
    def equivalent_density(self, area, multi, light_weight):
        return self.density * multi + light_weight / area

