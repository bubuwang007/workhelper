from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class Graphics:

    def __init__(self, commands: Mac):
        self.commands = commands
    
    @all
    def VIEW(self, xv, yv, zv, wn=1)->Command:
        '''设置视图方向
        Args:
            wn: 视图编号
            xv: 视图方向x分量
            yv: 视图方向y分量
            zv: 视图方向z分量
        1,0,-1,0 正常模型视图,Y轴朝屏幕内
        1,0,0,1  默认视图,Z轴朝屏幕外
        '''
        return Command(f"/VIEW,{wn},{xv},{yv},{zv}")
    
    @all
    def REPLOT(self, label="RESIZE")->Command:
        '''重绘
        Args:
            label: 图形标签 RESIZE, FAST
        '''
        return Command(f"/REPLOT,{label}")