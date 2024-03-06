from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Processor import *
from ..Command import Command


class Components:
    def __init__(self, commands: Mac):
        self.commands = commands

    @all
    def CM(self, cname, entity) -> Command:
        """创建一个组件
        Args:
            cname: 组件名称
            entity: VOLU, AREA, LINE, KP,ELEM, NODE
        """
        return Command(f"CM,{cname},{entity}")

    @all
    def CMSEL(self, type="S", name="", entity="") -> Command:
        """选择一个组件
        Args:
            type: S, R, A, U, ALL, NONE
            name: 组件名称
            entity: VOLU, AREA, LINE, KP, ELEM, NODE
        """
        return Command(f"CMSEL,{type},{name},{entity}")

    def areas(self, cname) -> CM:
        self.CM(cname, "AREA")
        return CM(cname, "AREA")

    def cmsel_none(self):
        self.CMSEL("NONE")

    def cmsel_all(self):
        self.CMSEL("ALL")

    def cmsel_add(self, name):
        self.CMSEL("A", name)

class CM:
    """组件"""

    name: str
    entity_type: str

    def __init__(self, name, entity_type):
        self.entity_type = entity_type
        self.name = name

    def __str__(self):
        return self.name
