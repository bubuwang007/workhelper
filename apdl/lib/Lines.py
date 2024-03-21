from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class Lines:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def LREVERSE(self, line, no_e_flip=0) -> Command:
        '''Reverses the direction of a line.
        Args:
            line: Line number.
            no_e_flip: Specifies whether the line elements are flipped. If NO_E_FLIP = 0, the elements are flipped. If NO_E_FLIP = 1, the elements are not flipped.
        '''
        return Command(f"LREVERSE,{line},{no_e_flip}") 
    
    @prep7
    def L(self, p1, p2, ndiv="", space="", xv1="", yv1="", zv1="", xv2="", yv2="", zv2="") -> Command:
        '''Defines a line element by its two keypoints.
        Args:
            p1: Keypoint number at the start of the line.
            p2: Keypoint number at the end of the line.
            ndiv: Number of divisions. The default value is 1.
            space: Specifies the spacing of the divisions. The default value is 0.
            xv1, yv1, zv1: Components of the vector defining the orientation of the line at the start.
            xv2, yv2, zv2: Components of the vector defining the orientation of the line at the end.
        '''
        return Command(f"L,{p1},{p2},{ndiv},{space},{xv1},{yv1},{zv1},{xv2},{yv2},{zv2}")