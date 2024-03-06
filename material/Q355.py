
class Q355:
    """kg N m s"""

    type = "solid"
    density = 7850
    elastic_modulus = 2.06e11
    poissons_ratio = 0.3
    alpha = 1.2e-5
    fee = 400 # 端面承压强度
    yield_strength = 305
    ultimate_tensile_strength = 470

    __t = [16, 40, 63, 80, 100]
    __yield_strength = [355, 345, 335, 325, 315]
    __f = [305, 295, 290, 280, 270]
    __fv = [175, 170, 165, 160, 155]

    def __interp(self, li, t):
        for i in range(len(self.__t)):
            if t <= self.__t[i]:
                return li[i]

    def get_yield_strength(self, t):
        return self.__interp(self.__yield_strength, t)
    
    def get_f(self, t):
        return self.__interp(self.__f, t)
    
    def get_fv(self, t):
        return self.__interp(self.__fv, t)

    def equivalent_density(self, area, multi, light_weight):
        return self.density * multi + light_weight / area