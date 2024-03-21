from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac
    from ..Scalar import Scalar

from ..Processor import *
from ..Command import Command

class Forces:

    def __init__(self, commands: Mac):
        self.commands = commands

    @solu
    def F(self, node, lab, value, value2="", nend="", ninc=""):
        return Command(f"F,{node},{lab},{value},{value2},{nend},{ninc}")

    def fx(self, node, value):
        return self.F(node, "FX", value)
    
    def fy(self, node, value):
        return self.F(node, "FY", value)
    
    def fz(self, node, value):
        return self.F(node, "FZ", value)