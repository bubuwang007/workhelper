from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class GraphicsPrimitives:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def PCIRC(self, rad1, rad2, theta1, theta2):
        '''Creates a circular area centered about the working plane origin.
        Args:
            rad1: Inner radius of the circular area.
            rad2: Outer radius of the circular area.
            theta1: Starting angle of the circular area.
            theta2: Ending angle of the circular area.
        '''
        return Command(f"PCIRC,{rad1},{rad2},{theta1},{theta2}")
    
    def ctube(self, d, t):
        '''Creates a circular tube area.
        Args:
            d: Diameter of the circular tube.
            t: Thickness of the circular tube.
        '''
        self.PCIRC(d/2-t, d/2, 0, 360)

    def csolid(self, d):
        '''Creates a circular solid area.
        Args:
            d: Diameter of the circular solid.
        '''
        self.PCIRC(0, d/2, 0, 360)

    @prep7
    def BLC4(self, xcorner, ycorner, xlength, ylength, depth=0):
        '''Creates a block area ro block based working plane.
        Args:
            xcorner: X-coordinate of the first corner point.
            ycorner: Y-coordinate of the first corner point.
            xlength: X-length of the block volume.
            ylength: Y-length of the block volume.
            depth: Depth of the block volume.
        '''
        return Command(f"BLC4,{xcorner},{ycorner},{xlength},{ylength},{depth}")
    
    @prep7
    def BLC5(self, xcenter, ycenter, xlength, ylength, depth=0):
        '''Creates a block area ro block based working plane.
        Args:
            xcenter: X-coordinate of the center point.
            ycenter: Y-coordinate of the center point.
            xlength: X-length of the block volume.
            ylength: Y-length of the block volume.
            depth: Depth of the block volume.
        '''
        return Command(f"BLC5,{xcenter},{ycenter},{xlength},{ylength},{depth}")

