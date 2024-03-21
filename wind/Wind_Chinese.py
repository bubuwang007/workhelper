import numpy as np
from typing import TypeVar

T = TypeVar("T")


class Wind_Chinese:
    global_dict = {
        "g": 2.5,  # 峰值因子
        "damp_ratio": 0.01,  # 阻尼比
        "ground_roughness": ["A", "B", "C", "D"],  # 地面粗糙度
        "ground_roughness_index": {"A": 0, "B": 1, "C": 2, "D": 3},
        "I10": [0.12, 0.14, 0.23, 0.39],  # 10m 高度名义揣流强度
        "kw": [1.28, 1.0, 0.54, 0.26],  # 地面粗糙度修正系数
        "k_a": {
            "高层": {
                "k": [0.944, 0.67, 0.295, 0.112],
                "a1": [0.155, 0.187, 0.261, 0.346],
            },
            "高耸": {
                "k": [1.276, 0.910, 0.404, 0.155],
                "a1": [0.186, 0.218, 0.292, 0.376],
            },
        },
        "H": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
        "modal_shapes": {
            "高层": [0, 0.02, 0.08, 0.17, 0.27, 0.38, 0.45, 0.67, 0.74, 0.86, 1],
            "高耸": [0, 0.02, 0.06, 0.14, 0.23, 0.34, 0.46, 0.59, 0.79, 0.86, 1],
        },
        "rho": 1.25,  # 空气密度
        "structural_type": ["高层", "高耸"],
        "terrain": ["平地", "山坡", "山峰"],
        # "H1":[5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500],
        # "wind_profile_factor": { # 风压高度变化系数
        #     "A": [1.09, 1.28, 1.42, 1.52, 1.67, 1.79, 1.89, 1.97, 2.05, 2.12, 2.18,
        #             2.23, 2.46, 2.64, 2.78, 2.91, 2.91, 2.91, 2.91, 2.91, 2.91],
        #     "B": [1.00, 1.00, 1.13, 1.23, 1.39, 1.52, 1.62, 1.71, 1.79, 1.87, 1.93,
        #             2.00, 2.25, 2.46, 2.63, 2.77, 2.91, 2.91, 2.91, 2.91, 2.91],
        #     "C": [0.65, 0.65, 0.65, 0.74, 0.88, 1.00, 1.10, 1.20, 1.28, 1.36, 1.43,
        #             1.50, 1.79, 2.03, 2.24, 2.43, 2.60, 2.76, 2.91, 2.91, 2.91],
        #     "D": [0.51, 0.51, 0.51, 0.51, 0.51, 0.60, 0.69, 0.77, 0.84, 0.91, 0.98,
        #             1.04, 1.33, 1.58, 1.81, 2.02, 2.22, 2.40, 2.58, 2.74, 2.91]
        # }
    }

    def __init__(self, wind_info):
        self.wind_info = wind_info
        self.__check()

    def __check(self):
        if self.wind_info["地面粗糙度"] not in self.global_dict["ground_roughness"]:
            raise ValueError("地面粗糙度取值为A、B、C、D")
        if self.wind_info["类型"] not in self.global_dict["structural_type"]:
            raise ValueError("类型取值为高耸、高层")

        if "地形" not in self.wind_info:
            self.wind_info["地形"] = "平地"
        elif self.wind_info["地形"] not in self.global_dict["terrain"]:
            raise ValueError("地形取值为平地、山坡、山峰")

    @property
    def B(self):
        return float(self.wind_info["结构宽度"])

    @property
    def H(self):
        return float(self.wind_info["结构高度"])

    @property
    def basic_wind_pressure(self):
        return float(self.wind_info["基本风压"])

    @property
    def g(self):
        return self.global_dict["g"]

    @property
    def frep(self):
        return float(self.wind_info["1阶频率"])

    @property
    def ground_roughness(self):
        return self.wind_info["地面粗糙度"]

    @property
    def ground_roughness_index(self):
        return self.global_dict["ground_roughness_index"][self.ground_roughness]

    @property
    def structural_type(self):
        return self.wind_info["类型"]

    @property
    def terrain(self):
        return self.wind_info["地形"]

    @property
    def mountain_height(self):
        if self.terrain == "平地":
            raise ValueError("平地无山高")
        else:
            return float(self.wind_info["山高"])

    @property
    def slope(self):
        if self.terrain == "平地":
            raise ValueError("平地无坡度")
        else:
            return float(self.wind_info["坡度"])

    @property
    def I10(self):
        return self.global_dict["I10"][self.ground_roughness_index]

    @property
    def kw(self):
        return self.global_dict["kw"][self.ground_roughness_index]

    @property
    def k(self):
        return self.global_dict["k_a"][self.structural_type]["k"][
            self.ground_roughness_index
        ]

    @property
    def a1(self):
        return self.global_dict["k_a"][self.structural_type]["a1"][
            self.ground_roughness_index
        ]

    @property
    def damp_ratio(self):
        return self.global_dict["damp_ratio"]

    """计算属性"""

    @property
    def basic_wind_speed(self):
        q = self.basic_wind_pressure * 1000
        return np.sqrt(2 * q / self.global_dict["rho"])

    @property
    def rho_x(self):
        return (10 * np.sqrt(self.B + 50 * (np.e ** (-self.B / 50)) - 50)) / self.B

    @property
    def rho_z(self):
        return (10 * np.sqrt(self.H + 60 * (np.e ** (-self.H / 60)) - 60)) / self.H

    def phi_1_z(self, h):
        h = 5 if h < 5 else h
        return self.interpolate(
            h/self.H,
            self.global_dict["H"],
            self.global_dict["modal_shapes"][self.wind_info["类型"]],
        )

    def mu_z(self, h):
        """高度变化系数"""
        h = 5 if h < 5 else h
        match self.wind_info["地面粗糙度"]:
            case "A":
                return 1.284 * (h / 10) ** 0.24
            case "B":
                return 1 * (h / 10) ** 0.30
            case "C":
                return 0.544 * (h / 10) ** 0.44
            case "D":
                return 0.262 * (h / 10) ** 0.60

    def B_z(self, h):
        if self.H > 300:
            raise NotImplementedError("暂时不支持高度大于300m的结构")
        return (
            self.k
            * self.H**self.a1
            * self.rho_x
            * self.rho_z
            * self.phi_1_z(h)
            / self.mu_z(h)
        )

    @property
    def x1(self):
        ret = 30 * self.frep / np.sqrt(self.kw * self.basic_wind_pressure)
        if ret < 5:
            raise ValueError("x1应该小于5，请检查参数！")
        return ret

    @property
    def R(self):
        # 共振分量因子
        tmp1 = np.pi / (6 * self.damp_ratio)
        tmp2 = self.x1**2 / (1 + self.x1**2) ** (4 / 3)
        return np.sqrt(tmp1 * tmp2)

    def beta_z(self, h):
        return 1 + 2 * self.g * self.I10 * self.B_z(h) * np.sqrt(self.R**2 + 1)

    def yita_B(self, h):
        if self.terrain == "平地":
            return 1

        if self.terrain == "山峰":
            k = 2.2
        elif self.terrain == "山坡":
            k = 1.6
        else:
            raise ValueError("地形参数错误, 必须为平地、山坡、山峰")

        tan_alpha = min(0.3, np.tan(self.slope * np.pi / 180))
        z = min(h, self.mountain_height*2.5)
        return (1 + k * tan_alpha * (1 - z / (2.5 * self.mountain_height))) ** 2

    def modal_shapes(self, h):
        return self.interpolate(
            h,
            self.global_dict["H"],
            self.global_dict["modal_shapes"][self.wind_info["类型"]],
        )

    def interpolate(self, v: T, fr: list[T], to: list[T]) -> T:
        for i in range(len(fr)):
            if v < fr[i]:
                return to[i - 1] + (v - fr[i - 1]) * (to[i] - to[i - 1]) / (
                    fr[i] - fr[i - 1]
                )
        return to[-1]

    @property
    def x(self):
        ret = []
        num = 0
        while num < self.H:
            ret.append(num)
            num += 5
        ret.append(int(np.ceil(self.H)))
        return ret

    @property
    def y(self):
        ret = []
        for i in self.x:
            ret.append(self.mu_z(i) * self.beta_z(i) * self.yita_B(i) * self.basic_wind_pressure)
        return ret
    
    def wind_pressure(self, h):
        return self.interpolate(h, self.x, self.y)

if __name__ == "__main__":
    wind_info = {
        "结构宽度": 30,
        "结构高度": 100,
        "基本风压": 0.15,
        "地面粗糙度": "A",
        "1阶频率": 0.5,
        "类型": "高耸",
    }
    wind = Wind_Chinese(wind_info)
    print(wind.x)
    print(wind.y)
    print(wind.wind_pressure(5))
