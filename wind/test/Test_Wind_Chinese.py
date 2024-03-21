import unittest
from workhelper.wind.Wind_Chinese import Wind_Chinese

class TestWindChinese(unittest.TestCase):

    def setUp(self):
        self.wind_info1 = {
            "结构宽度": 30,
            "结构高度": 100,
            "基本风压": 0.15,
            "地面粗糙度": "A",
            "1阶频率": 0.5,
            "类型": "高层",
            "地形": "平地",
        }
        self.wind1 = Wind_Chinese(self.wind_info1)

    def test_basic_paras(self):
        self.assertEqual(self.wind1.B, 30)
        self.assertEqual(self.wind1.H, 100)
        self.assertAlmostEqual(self.wind1.basic_wind_pressure, 0.15)
        self.assertAlmostEqual(self.wind1.g, 2.5)
        self.assertAlmostEqual(self.wind1.frep, 0.5)
        self.assertEqual(self.wind1.terrain, "平地")
        self.assertEqual(self.wind1.structural_type, "高层")
        self.assertEqual(self.wind1.ground_roughness, "A")
        self.assertEqual(self.wind1.ground_roughness_index, 0)
        self.assertAlmostEqual(self.wind1.I10, 0.12)
        self.assertAlmostEqual(self.wind1.kw, 1.28)
        self.assertAlmostEqual(self.wind1.k, 0.944)
        self.assertAlmostEqual(self.wind1.a1, 0.155)

        self.assertAlmostEqual(
            self.wind1.rho_x, 0.9092477
        )
        self.assertAlmostEqual(
            self.wind1.rho_z, 0.7164673
        )
        self.assertAlmostEqual(
            self.wind1.phi_1_z(5), 0.01
        )
        # self.assertAlmostEqual(
        #     self.wind1.B_z(5), 1
        # )


if __name__ == "__main__":
    unittest.main()
