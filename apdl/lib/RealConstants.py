from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Scalar import Scalar
from ..Processor import *
from ..Command import Command

class RealConstants:

    def __init__(self, commands: Mac):
        self.commands = commands
    
    @prep7
    def R(self, nset, *r) -> Command:
        '''Defines real constants.
        Args:
            nset: Set number.
            r: Real constants.
        '''
        return Command(f"R,{nset}, {','.join(map(str, r))}")
    
    @prep7
    def RMORE(self, *r):
        '''Defines additional real constants.
        Args:
            r: Real constants.
        '''
        if len(r) > 6:
            raise ValueError("The maximum number of real constants is 6.")
        return Command(f"RMORE,{','.join(map(str, r))}")

    def r(self, nset, *r):
        if len(r) < 6:
            self.R(nset, *r)
        else:
            self.R(nset, *r[:6])
            self.RMORE(*r[6:])

    @all
    def GET(self, parname, entity, entnum="", item1="", it1num="", item2="", it2num="") -> Command:
        '''Retrieves data from the database.
        '''
        return Command(f"*GET,{parname},{entity},{entnum},{item1},{it1num},{item2},{it2num}")
    
    def get_max_rnum(self) -> Scalar:
        par = self.commands.tmp_scalar()
        self.GET(par, entity="RCON", entnum="0", item1="NUM", it1num="MAX")
        par.used = True
        return par
