from __future__ import annotations
import re
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class Selecting:

    re_xyz = re.compile(r"([xyzXYZ])=([+-]?(?:\d+\.\d+|\d+|[a-zA-Z_]+)),?([(+-]?(?:\d+\.\d+|\d+|[a-zA-Z_]+))?")

    def __init__(self, commands: Mac):
        self.commands = commands

    @all
    def ALLSEL(self, labt="ALL", entity="ALL") -> Command:
        return Command(f"ALLSEL,{labt},{entity}")

    @all
    def LSEL(self, type="S", item="", comp="",vmin="",vmax="",vinc="",lswp="") -> Command:
        return Command(f"LSEL,{type},{item},{comp},{vmin},{vmax},{vinc},{lswp}")

    def lsel_none(self):
        self.LSEL("NONE")

    def lsel_xrange(self, xmin, xmax="", type="S"):
        self.LSEL(type, "LOC", "X", xmin, xmax)

    def lsel_yrange(self, ymin, ymax="", type="S"):
        self.LSEL(type, "LOC", "Y", ymin, ymax)

    def lsel_zrange(self, zmin, zmax="", type="S"):
        self.LSEL(type, "LOC", "Z", zmin, zmax)

    def lsel_by_num(self, start, end="", step="", type="S"):
        self.LSEL(type, "LINE", "",start, end, step)

    @all
    def ASEL(self, type="S", item="", comp="",vmin="",vmax="",vinc="",kswp="") -> Command:
        return Command(f"ASEL,{type},{item},{comp},{vmin},{vmax},{vinc},{kswp}")

    @all
    def NSEL(self, type="S", item="", comp="",vmin="",vmax="",vinc="",kabs="") -> Command:
        return Command(f"NSEL,{type},{item},{comp},{vmin},{vmax},{vinc},{kabs}")

    def nsel_all(self):
        self.NSEL("ALL")
    
    def nsel_none(self):
        self.NSEL("NONE")

    def nsel_by_num(self, start, end="", step="", type="S"):
        self.NSEL(type, "NODE", "", start, end, step)

    def nsel_xrange(self, xmin, xmax="", type="S"):
        self.NSEL(type, "LOC", "X", xmin, xmax)

    def nsel_yrange(self, ymin, ymax="", type="S"):
        self.NSEL(type, "LOC", "Y", ymin, ymax)

    def nsel_zrange(self, zmin, zmax="", type="S"):
        self.NSEL(type, "LOC", "Z", zmin, zmax)

    def asel_none(self):
        self.ASEL("NONE")

    def select_loc(self, entity_type:str, loc_str:str, select_type="S", tolerance=1e-6):
        """选择一个位置"""
        loc = self.re_xyz.findall(loc_str)
        for ind, i in enumerate(loc):
            if len(i)!= 3:
                raise ValueError("位置字符串格式错误")
            else:
                # print(i)
                if i[-1] == "":
                    tmp = (i[0].upper(), str(i[1])+f"-{tolerance}", str(i[1])+f"+{tolerance}")
                else:
                    tmp = (i[0].upper(), i[1], i[2])
            if ind == 0:
                getattr(self, f"{entity_type.upper()}SEL")(select_type, "LOC", *tmp)
            else:
                getattr(self, f"{entity_type.upper()}SEL")("R", "LOC", *tmp)

    @all
    def KSLL(self, type="S") -> Command:
        return Command(f"KSLL,{type}")
    
    @all
    def KSEL(self, type="S", item="", comp="",vmin="",vmax="",vinc="",kabs="") -> Command:
        return Command(f"KSEL,{type},{item},{comp},{vmin},{vmax},{vinc},{kabs}")
    
    def ksel_none(self):
        self.KSEL("NONE")

    def ksel_xrange(self, xmin, xmax="", type="S"):
        self.KSEL(type, "LOC", "X", xmin, xmax)

    def ksel_yrange(self, ymin, ymax="", type="S"):
        self.KSEL(type, "LOC", "Y", ymin, ymax)

    def ksel_zrange(self, zmin, zmax="", type="S"):
        self.KSEL(type, "LOC", "Z", zmin, zmax)
    
    @all
    def NSLK(self, type="S") -> Command:
        return Command(f"NSLK,{type}")

    @all
    def NSLE(self, type="S", nodetype="", num="") -> Command:
        return Command(f"NSLE,{type},{nodetype},{num}")

    @all
    def ESLL(self, type="S") -> Command:
        return Command(f"ESLL,{type}")

    @all
    def ESLN(self, type="S", ekey="", nodetype="") -> Command:
        return Command(f"ESLN,{type},{ekey},{nodetype}")

    @all
    def NSLL(self, type="S", nkey="") -> Command:
        return Command(f"NSLL,{type},{nkey}")

    @all
    def ESEL(self, type="S", item="", comp="",vmin="",vmax="",vinc="", kabs="") -> Command:
        return Command(f"ESEL,{type},{item},{comp},{vmin},{vmax},{vinc},{kabs}")

    def esel_ename(self, ename, select_type="S"):
        self.ESEL(select_type, "ENAME", vmin = ename)

    def esel_none(self):
        self.ESEL("NONE")

    def esel_by_num(self, start, end="", step="", type="S"):
        self.ESEL(type, "ELEM", "", start, end, step)

    def esel_by_etypenum(self, start, end="", step="", select_type="S"):
        self.ESEL(select_type, "TYPE", "", start, end, step)

    def esel_xrange(self, xmin, xmax="", type="S"):
        self.ESEL(type, "CENT", "X", xmin, xmax)
    
    def esel_yrange(self, ymin, ymax="", type="S"):
        self.ESEL(type, "CENT", "Y", ymin, ymax)
    
    def esel_zrange(self, zmin, zmax="", type="S"):
        self.ESEL(type, "CENT", "Z", zmin, zmax)