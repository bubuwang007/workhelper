from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac
    from ..Scalar import Scalar

from ..Processor import *
from ..Command import Command

class ElementType:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def ET(self, itype, ename, *kopt, inopr="") -> Command:
        '''Defines an element type.
        Args:
            itype: Element type number.
            ename: Element name.
            kopt: Optional arguments.
        '''
        return Command(f"ET,{itype},{ename},{','.join(map(str,kopt))},{inopr}")

    @prep7
    def KEYOPT(self, itype, knum, value) -> Command:
        '''Specifies key options for element types.
        Args:
            itype: Element type number.
            knum: Key option number.
            value: Key option value.
        '''
        return Command(f"KEYOPT,{itype},{knum},{value}")

    def mesh200(self, itype, *kopt):
        self.ET(itype, "MESH200", *kopt)  

    def beam188(self, itype, *kopt):
        self.ET(itype, "BEAM188", *kopt)  

    def mass21(self, itype, *kopt):
        self.ET(itype, "MASS21", *kopt)

    @all
    def GET(self, parname, entity, entnum="", item1="", it1num="", item2="", it2num="") -> Command:
        '''Retrieves data from the database.
        '''
        return Command(f"*GET,{parname},{entity},{entnum},{item1},{it1num},{item2},{it2num}")

    def get_max_etype(self) -> Scalar:
        par = self.commands.tmp_scalar()
        self.GET(par, entity="ETYP", entnum="0", item1="NUM", it1num="MAX")
        par.used = True
        return par