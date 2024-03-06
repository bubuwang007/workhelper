from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command
from ..Scalar import Scalar

class Get:

    def __init__(self, commands: Mac):
        self.commands = commands

    def lcount(self) -> Scalar:
        scalar = self.commands.tmp_scalar()
        self.commands.append(Command(f"*GET,{scalar},LINE,0,COUNT"))
        scalar.used = True
        return scalar

    def lnum(self) -> Scalar:
        scalar = self.commands.tmp_scalar()
        self.commands.append(Command(f"*GET,{scalar},LINE,0,NUM,MIN"))
        scalar.used = True
        return scalar

    def lnext(self, scalar: Scalar) -> Scalar:
        scalar << Command((f"LSNEXT({scalar})"))
        return scalar

    def ncount(self) -> Scalar:
        scalar = self.commands.tmp_scalar()
        self.commands.append(Command(f"*GET,{scalar},NODE,0,COUNT"))
        scalar.used = True
        return scalar
    
    def nnum(self) -> Scalar:
        scalar = self.commands.tmp_scalar()
        self.commands.append(Command(f"*GET,{scalar},NODE,0,NUM,MIN"))
        scalar.used = True
        return scalar

    def nnext(self, scalar: Scalar) -> Scalar:
        scalar << Command((f"NDNEXT({scalar})"))
        return scalar

    def kcount(self) -> Scalar:
        scalar = self.commands.tmp_scalar()
        self.commands.append(Command(f"*GET,{scalar},KP,0,COUNT"))
        scalar.used = True
        return scalar
    
    def knum(self) -> Scalar:
        scalar = self.commands.tmp_scalar()
        self.commands.append(Command(f"*GET,{scalar},KP,0,NUM,MIN"))
        scalar.used = True
        return scalar

    def knext(self, scalar: Scalar) -> Scalar:
        scalar << Command((f"KPNEXT({scalar})"))
        return scalar
    
    def kx(self, k) -> Scalar:
        scalar = self.commands.tmp_scalar(Command(f"KX({k})"))
        return scalar
    
    def ky(self, k) -> Scalar:
        scalar = self.commands.tmp_scalar(Command(f"KY({k})"))
        return scalar
    
    def kz(self, k) -> Scalar:
        scalar = self.commands.tmp_scalar(Command(f"KZ({k})"))
        return scalar

    def kxyz(self, k) -> tuple[Scalar, Scalar, Scalar]:
        return self.kx(k), self.ky(k), self.kz(k)
    
    def get_line_kp(self, line_num, pos) -> Scalar:
        scalar = self.commands.tmp_scalar()
        self.commands.append(Command(f"*GET,{scalar},LINE,{line_num},KP,{pos}"))
        scalar.used = True
        return scalar
    
    def node(self, x, y, z):
        scalar = self.commands.tmp_scalar()
        scalar << Command(f"NODE({x},{y},{z})")
        return scalar