from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class WorkingPlane:

    def __init__(self, commands: Mac):
        self.commands = commands

    @all
    def KWPAVE(self, *args) -> Command:
        '''Moves the working plane origin to the average location of keypoints.
        '''
        if len(args)>9:
            raise ValueError("Too many arguments")
        return Command(f"KWPAVE,{','.join(map(str, args))}")

    @all
    def KWPLAN(self, korgin, kxax, kplan, *, wn=1):
        '''Defines the working plane using three keypoints.
        Args:
            korgin: Keypoint defining the origin of the working plane.
            kxax: Keypoint defining the x-axis of the working plane.
            kplan: Keypoint defining the plane of the working plane.
            wn: Working plane number. Defaults to 1.
        '''
        return Command(f"KWPLAN,{wn},{korgin},{kxax},{kplan}")
    
    @all
    def NWPAVE(self, *args) -> Command:
        '''Moves the working plane origin to the average location of nodes.
        '''
        if len(args)>9:
            raise ValueError("Too many arguments")
        return Command(f"NWPAVE,{','.join(map(str, args))}")

    @all
    def NWPLAN(self, norgin, nxax, nplan, *, wn=1):
        '''Defines the working plane using three nodes.
        Args:
            norgin: Node defining the origin of the working plane.
            nxax: Node defining the x-axis of the working plane.
            nplan: Node defining the plane of the working plane.
            wn: Working plane number. Defaults to 1.
        '''
        return Command(f"NWPLAN,{wn},{norgin},{nxax},{nplan}")
    
    @all
    def WPCSYS(self, kcn="", wn=-1) -> Command:
        '''Defines the working plane location based on a coordinate system.
        Args:
            kcn: Coordinate system number. KCN may be 0,1,2 or any previously defined local coordinate system number (defaults to the active system).
            wn: Working plane number. Defaults to 1.
        '''
        return Command(f"WPCSYS,{wn},{kcn}")
    
    @all
    def WPOFFS(self, dx=0, dy=0, dz=0) -> Command:
        '''Moves the working plane origin by the specified offset.
        Args:
            dx, dy, dz: Offset values in the global Cartesian coordinate system.
        '''
        return Command(f"WPOFFS,{dx},{dy},{dz}")
    
    @all
    def WPROTA(self, thxy=0, thyz=0, thzx=0) -> Command:
        '''Rotates the working plane.
        Args:
            thxy: Angle of rotation about the global Z-axis.
            thyz: Angle of rotation about the global X-axis.
            thzx: Angle of rotation about the global Y-axis.
        '''
        return Command(f"WPROTA,{thxy},{thyz},{thzx}")
    
    @all
    def WPSTYL(self) -> Command:
        raise NotImplementedError