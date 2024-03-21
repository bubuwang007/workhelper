from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac
    from ..Scalar import Scalar

from ..Processor import *
from ..Command import Command

class ConstraintEquations:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def CERIG(self, master, slave, *dof) -> Command:
        '''Generates constraint equations between nodes.
            dof: 
            ALL, UXYZ, RXYZ, UX, UY, UZ, ROTX, ROTY, ROTZ
        '''
        if len(dof) > 5:
            raise ValueError("Too many dof!")
        return Command(f"CERIG,{master},{slave},{','.join(map(str,dof))}")