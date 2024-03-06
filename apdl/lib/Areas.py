from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class Areas:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def A(self, *p) -> Command:
        '''Creates an area by connecting keypoints.
        Args:
            p: List of keypoints.
        '''
        if len(p) > 18 or len(p) < 3:
            raise ValueError("The maximum number of keypoints is 18 and the minimum is 3.")
        return Command(f"A,{','.join(map(str, p))}")
    
    def get_return(self):
        return self.commands.tmp_scalar('_RETURN')