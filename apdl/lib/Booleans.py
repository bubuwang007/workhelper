from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class Booleans:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def AADD(self, *args) -> Command:
        '''Adds separate areas to create a single area.
        '''
        if len(args)>9:
            raise ValueError("Too many arguments")
        return Command(f"AADD,{','.join(map(str, args))}")
    
    @prep7
    def ASBA(self, na1, na2, *,sepo="", keep1="", keep2="") -> Command:
        '''Subtracts areas from areas.
        Args:
            na1: Area number of the area to be subtracted from.
            na2: Area number of the area to subtracted.
            sepo: Separation option.
                (blank) — The resulting areas will share line(s) where they touch.
                SEPO — The resulting areas will have separate, but coincident line(s) where they touch.
            keep1: Keep option for area number NA1.
                (blank) — Use the setting of KEEP on the BOPTN command.
                DELETE — Delete NA1 areas after ASBA operation (override BOPTN command settings).
                KEEP — Keep NA1 areas after ASBA operation (override BOPTN command settings).
            keep2: Keep option for area number NA2.
                (blank) — Use the setting of KEEP on the BOPTN command.
                DELETE — Delete NA2 areas after ASBA operation (override BOPTN command settings).
                KEEP — Keep NA2 areas after ASBA operation (override BOPTN command settings).
        '''
        return Command(f"ASBA,{na1},{na2},{sepo},{keep1},{keep2}")