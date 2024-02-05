from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Mac import Mac
from .Command import Command

class ElseIf:

    def __init__(self, commands: Mac, condition):
        self.__commands = commands
        self.__commands.append(Command(f"*ELSEIF,{condition}"))
        self.__commands.add_prefix()

    def __enter__(self) -> ElseIf:
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass