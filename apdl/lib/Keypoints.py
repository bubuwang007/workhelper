from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac
    from ..Scalar import Scalar

from ..Processor import *
from ..Command import Command

class Keypoints:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def K(self, x=0, y=0, z=0, npt=""):
        '''Creates a keypoint.(Returns the keypoint number created.)
        Args:
            npt: Keypoint number. If blank, the next available keypoint number is used.
            x: X-coordinate of the keypoint.
            y: Y-coordinate of the keypoint.
            z: Z-coordinate of the keypoint.
        '''
        return Command(f"K,{npt},{x},{y},{z}")

    def get_return(self):
        return self.commands.tmp_scalar('_RETURN')
    
    @all
    def GET(self, entity, entnum="", item1="", it1num="", item2="", it2num="") -> Command:
        '''Retrieves data from the database.
        '''
        self.par = self.commands.tmp_scalar()
        self.par.used = True
        return Command(f"*GET,{self.par},{entity},{entnum},{item1},{it1num},{item2},{it2num}")
    
    def get_max_knum(self) -> Scalar:
        self.GET(entity="KP", entnum="0", item1="NUM", it1num="MAX")
        return self.par
