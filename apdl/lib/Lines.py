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