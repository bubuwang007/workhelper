from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Mac import Mac
from .Command import Command

class Else:

    def __init__(self, commands: Mac):
        self.__commands = commands
        self.__commands.append(Command(f"*ELSE"))
        self.__commands.add_prefix()
        self.__commands.finish()

    def __enter__(self) -> Else:
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass