from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Mac import Mac
    from .Scalar import Scalar
from .Command import Command


class Do:
    scope_num: int = 0

    def __init__(self, commands: Mac, rng: tuple):
        Do.scope_num += 1
        self.scope = f"do{Do.scope_num}"
        self.__commands = commands
        self.__i = commands.scalar("i", scope=self.scope, read_only=True)
        if isinstance(rng, int):
            rng = (1, rng, 1)
        elif len(rng) == 1:
            rng = (1, rng[0], 1)
        elif len(rng) == 2:
            rng = (rng[0], rng[1], 1)
        elif len(rng) == 3:
            rng = (rng[0], rng[1], rng[2])
        else:
            raise ValueError(f"Invalid range: {rng}")
        self.__commands.append(Command(f"*DO,{self.i},{rng[0]},{rng[1]},{rng[2]}"))
        self.__commands.add_prefix()

    @property
    def i(self) -> Scalar:
        return self.__i

    def cycle(self) -> None:
        self.__commands.append(Command(f"*CYCLE"))

    def exit(self) -> None:
        self.__commands.append(Command(f"*EXIT"))

    def __enter__(self) -> Do:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        Do.scope_num -= 1
        self.__commands.sub_prefix()
        self.__commands.append(Command(f"*ENDDO"))
        self.__commands.del_scalar(self.i)
