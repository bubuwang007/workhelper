from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class Meshing:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def AMESH(self, na1, na2="", ninc=""):
        '''Generates nodes and area elements within areas.
        Args:
            na1: First area number.
            na2: Last area number.
            ninc: Increment.
        '''
        return Command(f"AMESH,{na1},{na2},{ninc}")
    
    def amesh_all(self):
        self.AMESH("ALL")

    @prep7
    def LATT(self, mat, real, etype, kb, ke, secnum):
        '''Defines a lattice structure.
        Args:
            mat: Material reference number.
            real: Real constant set number.
            type: Lattice type.
            kb: Key option for the beginning of the lattice.
            ke: Key option for the end of the lattice.
            secnum: Section number.
        '''
        return Command(f"LATT,{mat},{real},{etype},,{kb},{ke},{secnum}")
    
    def latt_beam188(self, mat, etype, secnum, kb="", real=""):
        self.LATT(mat, real, etype, kb, "", secnum)

    def latt_link10(self, mat, real, etype):
        self.LATT(mat, real, etype, kb="", ke="", secnum="")

    @prep7
    def LESIZE(self, lnum="", size="", angsize="", ndiv="", sapce="", kforc="", layer1="", layer2="", kyndiv=""):
        '''Specifies the divisions and spacing ratio on unmeshed lines.
        Args:
            lnum: Line or area number.
            size: 
                If NDIV is blank, SIZE is the division (element edge) length.The number of divisions is automatically calculated from the line length (rounded upward to next integer). If SIZE is zero (or blank), use ANGSIZ or NDIV.
            angsize: 
                The division arc (in degrees) spanned by the element edge (except for straight lines, which always result in one division). The number of divisions is automatically calculated from the line length (rounded upward to next integer).
            ndiv:
                If positive, NDIV is the number of element divisions per line. If -1 (and KFORC = 1), NDIV is assumed to be zero element divisions per line. TARGE169 with a rigid specification ignores NDIV and will always mesh with one element division
            sapce: 
                Spacing ratio. If positive, nominal ratio of last division size to first division size (if > 1.0, sizes increase, if < 1.0, sizes decrease). If negative, |SPACE| is nominal ratio of center division(s) size to end divisions size. Ratio defaults to 1.0 (uniform spacing). For layer-meshing, a value of 1.0 normally is used. If SPACE = FREE, ratio is determined by other considerations
            kforc: 
                KFORC 0-3 are used only with NL1 = ALL. Specifies which selected lines are to be modified.
                0 — Modify only selected lines having undefined (zero) divisions.
                1 — Modify all selected lines.
                2 — Modify only selected lines having fewer divisions (including zero) than specified with this command.
                3 — Modify only selected lines having more divisions than specified with this command.
                4 — Modify only nonzero settings for SIZE, ANGSIZ, NDIV, SPACE, LAYER1, and LAYER2. If KFORC = 4, blank or 0 settings remain unchanged.
            layer1: Layer-meshing control parameter.
            layer2: Layer-meshing control parameter.
            kyndiv: 
                0, No, and Off means that SmartSizing cannot override specified divisions and spacing ratios. Mapped mesh fails if divisions do not match. This defines the specification as "hard".
                1, Yes, and On means that SmartSizing can override specified divisions and spacing ratios for curvature or proximity. Mapped meshing can override divisions to obtain required matching divisions. This defines the specification as" soft".
        '''
        return Command(f"LESIZE,{lnum},{size},{angsize},{ndiv},{sapce},{kforc},{layer1},{layer2},{kyndiv}")
    
    def lesize_by_size(self, lnum, size):
        self.LESIZE(lnum, size)

    def lesize_by_div(self, lnum, ndiv):
        self.LESIZE(lnum, ndiv=ndiv)

    @prep7
    def LMESH(self, nl1, nl2="", ninc=""):
        '''Generates nodes and line elements within lines.
        Args:
            nl1: First line number.
            nl2: Last line number.
            ninc: Increment.
        '''
        return Command(f"LMESH,{nl1},{nl2},{ninc}")
    
    def lmesh_all(self):
        self.LMESH("ALL")

    @prep7
    def REAL(self, num):
        return Command(f"REAL,{num}")
    
    @prep7
    def TYPE(self, num):
        return Command(f"TYPE,{num}")

    @prep7
    def MAT(self, num):
        return Command(f"MAT,{num}")