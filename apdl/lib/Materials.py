from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class Materials:

    def __init__(self, commands: Mac):
        self.commands = commands

    @prep7
    def MP(self, lab, mat_num, *args) -> Command:
        """定义材料属性
        Lab:
            ALPD: Mass matrix multiplier for damping.
            ALPX: Secant coefficients of thermal expansion (also ALPY, ALPZ).
            BETD: Stiffness matrix multiplier for damping.
            BETX: Coefficient of diffusion expansion (also BETY, BETZ).
            BVIS: Bulk viscosity.
            C:    Specific heat.
            DENS: Mass density.
            EX:   Young's modulus.
            GXY:  Shear modulus.
            MU:   Coefficient of friction. 
            NUXY: Minor Poisson's ratios (also NUYZ, NUXZ)
        Mat:
            Material number
        Args:
            Value of the material property
        """
        return Command(f"MP,{lab},{mat_num},{','.join(map(str,args))}")
    
    def define_material(self, mat_id, ex, prxy, dens, alpx):
        self.MP("EX", mat_id, f"{ex:.5E}")
        self.MP("PRXY", mat_id, prxy)
        self.MP("DENS", mat_id, dens)
        self.MP("ALPX", mat_id, alpx)