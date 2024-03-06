from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Mac import Mac
from .Command import Command
from .ElseIf import ElseIf
from .Else import Else

class If:

    def __init__(self, commands: Mac, condition):
        self.__commands = commands
        self.__commands.append(Command(f"*IF,{condition},THEN"))
        self.__commands.add_prefix()

    def ElseIf(self, condition) -> ElseIf:
        self.__commands.sub_prefix()
        return ElseIf(self.__commands, condition)

    def Else(self) -> Else:
        self.__commands.sub_prefix()
        return Else(self.__commands)

    def __enter__(self) -> If:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.__commands.sub_prefix()
        self.__commands.append(Command("*ENDIF"))
        self.__commands.finish()