from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command

class Aux15:

    def __init__(self, commands: Mac):
        self.commands = commands

    @aux15
    def IOPTN(self, lab, val) -> Command:
        return Command(f"IOPTN,{lab},{val}")

    @aux15
    def IGESIN(self, filename, ext=""):
        return Command(f"IGESIN,'{filename}','{ext}'")