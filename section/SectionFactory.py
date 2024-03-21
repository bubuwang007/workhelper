import re
import math

try:
    from .C_Circular_Rect import C_Circular_Rect
    from .C_Circular_Rect0 import C_Circular_Rect0
    from .C_OctagonPipe_Rect import C_OctagonPipe_Rect
    from .Circular import Circular
    from .CircularPipe import CircularPipe
    from .Combination import Combination
    from .I_Plate import I_Plate
    from .I import I
    from .InclineRectangle import InclineRectangle
    from .L import L
    from .Octagon import Octagon
    from .OctagonPipe import OctagonPipe
    from .Polygon import Polygon
    from .Rectangle import Rectangle
    from .RectanglePipe import RectanglePipe
    from .Section import Section
    from .P_MultiCircularPipe import P_MultiCircularPipe
except ImportError:
    from workhelper.section.C_Circular_Rect import C_Circular_Rect
    from workhelper.section.C_Circular_Rect0 import C_Circular_Rect0
    from workhelper.section.C_OctagonPipe_Rect import C_OctagonPipe_Rect
    from workhelper.section.Circular import Circular
    from workhelper.section.CircularPipe import CircularPipe
    from workhelper.section.Combination import Combination
    from workhelper.section.I_Plate import I_Plate
    from workhelper.section.I import I
    from workhelper.section.InclineRectangle import InclineRectangle
    from workhelper.section.L import L
    from workhelper.section.Octagon import Octagon
    from workhelper.section.OctagonPipe import OctagonPipe
    from workhelper.section.Polygon import Polygon
    from workhelper.section.Rectangle import Rectangle
    from workhelper.section.RectanglePipe import RectanglePipe
    from workhelper.section.Section import Section
    from workhelper.section.P_MultiCircularPipe import P_MultiCircularPipe

FLOAT = r"(\d+(?:\.\d+)?)"
INT = r"(\d+)"
convert_mapping = {
    "p": {
        "p1": re.compile(rf"^p{FLOAT}$"),
        "p2": re.compile(rf"^p{INT}[x×]{FLOAT}$"),
        # "p4": re.compile(rf"^p{INT}[x×]{FLOAT}[x×]{INT}[x×]{INT}$"),
        "p6": re.compile(rf"^p{INT}[x×]{FLOAT}[+]{FLOAT}[x×]{INT}[x×]{FLOAT}[x×]{FLOAT}$"),
    },
    "s": {
        "s1": re.compile(rf"^s{INT}[x×]{INT}[x×]{FLOAT}$"),
    },
    "c": {
        "c1": re.compile(rf"^c{INT}[x×]{FLOAT}\+{INT}[x×]{INT}[x×]{FLOAT}$"),
        "c2": re.compile(rf"^c{INT}[x×]{FLOAT}\+{INT}[x×]{INT}[x×]{FLOAT}[x×]{FLOAT}$"),
    },
    "b": {
        "b2": re.compile(rf"^b{INT}[x×]{INT}[x×]{FLOAT}[x×]{FLOAT}$"),
        "b1": re.compile(rf"^b{INT}[x×]{INT}$"),
    },
    "l": {
        "l1": re.compile(rf"^l{INT}[x×]{FLOAT}$"),
    },
    "h": {
        "h1": re.compile(rf"^h{INT}[x×]{INT}[x×]{FLOAT}[x×]{FLOAT}$"),
        "h2": re.compile(rf"^h{INT}[x×]{INT}[x×]{FLOAT}[x×]{FLOAT}[x×]{FLOAT}$"),
    },
    "a": {"a1": re.compile(rf"^a{INT}$")},
    "o": {
        # o500x375x152.5x245x180x190x14+250x150x8x8
        "o1": re.compile(rf"^o{FLOAT}[x×]{FLOAT}[x×]{FLOAT}[x×]{FLOAT}[x×]{FLOAT}[x×]{FLOAT}[x×]{FLOAT}\+{FLOAT}[x×]{FLOAT}[x×]{FLOAT}[x×]{FLOAT}$"),
    }
}

sec_mapping = {
    "b1": Rectangle, # 方管
    "b2": RectanglePipe,
    "c1": C_Circular_Rect0,
    "c2": C_Circular_Rect,
    "h1": I,
    "h2": I_Plate,
    "l1": L,
    "p1": Circular,
    "p2": CircularPipe,
    "p6": P_MultiCircularPipe,
    # "p4": p4,
    "s1": Circular,
    "o1": C_OctagonPipe_Rect,
}

class SectionFactory:
    @staticmethod
    def convert(size: str):
        size = size.lower().strip()
        head = size[0]
        search_map = convert_mapping[head]
        for key, value in search_map.items():
            result = value.findall(size)
            if result:
                if isinstance(result[0], tuple):
                    result = result[0]
                else:
                    result = (result[0],)
                return key, result
        raise ValueError(f"未找到匹配的部件类型: {size}")

    @staticmethod
    def get_section_class(size: str):
        paras = SectionFactory.convert(size)
        return sec_mapping[paras[0]]

    @staticmethod
    def get_section(size: tuple):
        """获取截面对象"""
        paras = SectionFactory.convert(size)
        if hasattr(SectionFactory, paras[0]):
            sizes = getattr(SectionFactory, paras[0])(paras[1])
        else:
            sizes = SectionFactory.normal(paras[1])
        obj = sec_mapping[paras[0]]
        return obj(*sizes)

    @staticmethod
    def normal(paras: tuple):
        return [float(i)/1000 for i in paras]

    @staticmethod
    def s1(paras: tuple):
        tmp = [float(paras[0])/1000, int(paras[1])]
        d = math.sqrt(tmp[1]) * tmp[0]
        return [d]

    # @staticmethod
    # def b1(paras: tuple):
    #     tmp = SectionFactory.normal(paras)
    #     return [*tmp, tmp[-1]]

    @staticmethod
    def p6(paras: tuple):
        posi = [3]
        ret = []
        for ind, i in enumerate(paras):
            if ind in posi:
                ret.append(int(i))
            else:
                ret.append(float(i)/1000)
        return ret

if __name__ == "__main__":
    
    s = "b2550x2000"
    sec = SectionFactory.get_section(s)
    print(type(sec))
    print(sec)
    sec.plot()
