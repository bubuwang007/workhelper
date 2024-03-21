from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac
    from ..Scalar import Scalar

from ..Processor import *
from ..Command import Command

class Constraint:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def D(self, node, lab, value="", value2="", nend="", ninc="",
          lab2="", lab3="", lab4="", lab5="", lab6="") -> Command:
        '''Defines a constraint.'''
        return Command(f"D,{node},{lab},{value},{value2},{nend},{ninc},{lab2},{lab3},{lab4},{lab5},{lab6}")

    def d(self, node, *lab):
        lab = list(*lab)
        while len(lab) < 6:
            lab.append("")
        self.D(node,lab[0],lab2=lab[1],lab3=lab[2],lab4=lab[3],lab5=lab[4],lab6=lab[5])

    def dx(self, node, value, value2="", nend="", ninc=""):
        self.D(node, "UX", value, value2, nend, ninc)

    def dy(self, node, value="", value2="", nend="", ninc=""):
        self.D(node, "UY", value, value2, nend, ninc)

    def dz(self, node, value="", value2="", nend="", ninc=""):
        self.D(node, "UZ", value, value2, nend, ninc)

    def drx(self, node, value="", value2="", nend="", ninc=""):
        self.D(node, "ROTX", value, value2, nend, ninc)
    
    def dry(self, node, value="", value2="", nend="", ninc=""):
        self.D(node, "ROTY", value, value2, nend, ninc)

    def drz(self, node, value="", value2="", nend="", ninc=""):
        self.D(node, "ROTZ", value, value2, nend, ninc)

    def dxyz(self, node, value="", value2="", nend="", ninc=""):
        self.D(node, "UX", value, value2, nend, ninc, "UY", "UZ")

    def drxyz(self, node, value="", value2="", nend="", ninc=""):
        self.D(node, "ROTX", value, value2, nend, ninc, "ROTY", "ROTZ")


