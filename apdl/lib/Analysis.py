from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac
    from ..Scalar import Scalar

from ..Processor import *
from ..Command import Command

class Analysis:

    def __init__(self, commands: Mac):
        self.commands = commands

    @solu
    def SOLVE(self, action="") -> Command:
        '''Solves the current analysis.'''
        return Command(f"SOLVE,{action}")

    def solve(self):
        self.SOLVE()

    @solu
    def ANTYPE(self, antype, status="", ldstep="", substep="",action="", prelp="") -> Command:
        '''Specifies the analysis type.
        antype:
            static or 0 - Static analysis
            buckle or 1 - Buckling analysis,Implies that a previous static solution was performed with prestress effects calculated (PSTRES,ON). Valid for structural degrees of freedom only.
            modal or 2 - Modal analysis
            harmonic or 3 - Harmonic analysis
            transient or 4 - Transient analysis
            substr or 7 - Substructuring analysis
            spectrum or 8 - Spectrum analysis
            soil or 9 - Soil analysis
        '''
        return Command(f"ANTYPE,{antype},{status},{ldstep},{substep},{action},,{prelp}")

    def static(self):
        self.ANTYPE("0")
    
    def buckle(self):
        self.ANTYPE("1")
    
    def modal(self):
        self.ANTYPE("2")
    
    def spectrum(self):
        self.ANTYPE("8")

    @solu
    def PSTRES(self, key) -> Command:
        '''Specifies whether prestress effects are included in the analysis.
        key:
            on or 1 - Prestress effects are included in the analysis.
            off or 0 - Prestress effects are not included in the analysis.
        '''
        return Command(f"PSTRES,{key}")
    
    def consider_prestress(self, key=True):
        self.PSTRES(key)

    @solu
    def ACEL(self, ax, ay, az) -> Command:
        '''Specifies the acceleration vector for the analysis.
        '''
        return Command(f"ACEL,{ax},{ay},{az}")
    
    def gravity(self, az):
        self.ACEL(0, 0, az)

    @solu
    def NLGEOM(self, key) -> Command:
        '''Specifies whether large deflection effects are included in the analysis.
        key:
            on - Large deflection effects are included in the analysis.
            off - Large deflection effects are not included in the analysis.
        '''
        key = "ON" if bool(key) else "OFF"
        return Command(f"NLGEOM,{key}")
    
    def large_deflection(self, key=True):
        self.NLGEOM(key)
    
    @solu
    def EQSLV(self, lab, taler="", mult="", keepfile=""):
        '''Specifies the equation solver to be used.
        '''
        return Command(f"EQSLV,{lab},{taler},{mult},{keepfile}")
    
    def eqslv_sparse(self):
        self.EQSLV("SPARSE")

    @solu
    def MODOPT(self, method, nmode):
        '''Specifies the modal analysis options.
        不完整
        method:
            LANB - Lanczos method
            SUBSP - Subspace method
            KRYLOV - Krylov-Schur method
        nmode:
            Number of modes to be extracted.
        '''
        return Command(f"MODOPT,{method},{nmode}")
    
    def mode_lanczos(self, nmode):
        self.MODOPT("LANB", nmode)

    @solu
    def MXPAND(self, nmode, elcalc) -> Command:
        '''Specifies the number of modes to be expanded and the element calculation option.
        不完整
        '''
        elcalc = "ON" if bool(elcalc) else "OFF"
        return Command(f"MXPAND,{nmode},,,{elcalc}")

    @solu
    def LUMPM(self, key) -> Command:
        '''Specifies whether the mass matrix is lumped.
        key:
            on - The mass matrix is lumped.
            off - The mass matrix is not lumped.
        '''
        key = "ON" if bool(key) else "OFF"
        return Command(f"LUMPM,{key}")