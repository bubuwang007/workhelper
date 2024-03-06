from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class CrossSections:
    
    def __init__(self, commands: Mac):
        self.commands = commands
    
    @prep7
    def SECTYPE(self, sec_id, *, type="BEAM", subtype="", refinekey: str|int="") -> Command:
        '''定义截面类型
        type = BEAM
        subtype:
            RECT: 矩形截面
            QUAD: 四边形截面
            CSOLID: 圆形截面
            CTUBE: 圆管截面
            CHAN: 槽钢截面
            I: I型截面
            Z: Z型截面
            L: L型截面
            T: T型截面
            HATS: 帽梁截面
            HREC: 矩形管截面
            ASEC: 任意截面
            MESH: 网格截面
        '''
        return Command(f"SECTYPE,{sec_id},{type},{subtype},,{refinekey}")
    
    @prep7
    def SECDATA(self, *args) -> Command:
        '''定义截面数据
        '''
        return Command(f"SECDATA,{','.join(map(str, args))}")

    def rect(self, sec_id, w, h) -> None:
        '''定义矩形截面
        '''
        self.SECTYPE(sec_id, subtype="RECT")
        self.SECDATA(w, h)

    def hrec(self, sec_id, w, h, tw, th) -> None:
        '''定义矩形管截面
        '''
        self.SECTYPE(sec_id, subtype="HREC")
        self.SECDATA(w, h, tw, tw, th, th)

    def csolid(self, sec_id, d) -> None:
        '''定义圆形截面
        '''
        self.SECTYPE(sec_id, subtype="CSOLID")
        self.SECDATA(d)

    def ctube(self, sec_id, d, t) -> None:
        '''定义圆管截面
        '''
        self.SECTYPE(sec_id, subtype="CTUBE")
        self.SECDATA(d/2-t, d/2)

    def i(self, sec_id, h, w, tw, tf) -> None:
        '''定义I型截面
        '''
        self.SECTYPE(sec_id, subtype="I")
        self.SECDATA(w, w, h, tw, tw, tf)

    def l(self, sec_id, l, t) -> None:
        '''定义L型截面
        '''
        self.SECTYPE(sec_id, subtype="L")
        self.SECDATA(l, l, t, t)

    @prep7
    def SECWRITE(self, fname,ext,eletype):
        '''将截面数据写入文件
        '''
        return Command(f"SECWRITE,{fname},{ext},,{eletype}")
    
    @prep7
    def SECOFFSET(self, location, offset1="", offset2="", cg_y="", cg_z="", sh_y="", sh_z=""):
        '''定义截面偏移
        '''
        return Command(f"SECOFFSET,{location},{offset1},{offset2},{cg_y},{cg_z},{sh_y},{sh_z}")
    
    @prep7
    def SECREAD(self, fname, ext, option):
        '''从文件中读取截面数据
        option:
            MESH: 读取网格截面
            LIBRARY: 读取截面库
        '''
        return Command(f"SECREAD,{fname},{ext},,{option}")
    
    @prep7
    def SECPLOT(self, secid, val1, val2="", val3=""):
        '''绘制截面
        '''
        return Command(f"SECPLOT,{secid},{val1},{val2},{val3}")

    @prep7
    def SLIST(self, start, stop="", step="", details="FULL", type=""):
        '''列出截面
        details:
            FULL: 完整列表
            BRIEF: 简要列表
            GROUP: If a section calls other sections, this option lists those sections too.
        '''
        return Command(f"SLIST,{start},{stop},{step},{details},{type}")