from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac
    from ..Scalar import Scalar

from ..Processor import *
from ..Command import Command

class Nodes:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def NMODIFY(self, node, x, y, z, thxy, thyz, thzx):
        '''Modify coordinates of this node.'''
        return Command(f"NMODIFY,{node},{x},{y},{z},{thxy},{thyz},{thzx}") 
    
    def nmodify_thzx(self, node, thzx):
        self.NMODIFY(node, "", "", "", 0, 0, thzx)