from __future__ import annotations
import typing

from .Expression import Expression
from .Command import Command

if typing.TYPE_CHECKING:
    from .Mac import Mac
from .utils import check_identifier


class Scalar(Expression):
    active: bool = True
    used: bool = False

    def __init__(
        self,
        id: str,
        commands: Mac,
        value=None,
        scope: str = "local",
        read_only: bool = False,
    ) -> None:
        self.scope = scope
        self.__id = id
        self.__commands = commands
        self.__read_only = read_only
        if value is not None:
            self.__set(value)
        check_identifier(self.name)
        Expression.__init__(self, self.name)

    def switch_commands(self, commands: Mac):
        if self.scope != "global":
            raise ValueError(f"Warning: {self.__id} is not global")
        self.__old_commands = self.__commands
        self.__commands = commands

    def switch_back(self):
        if self.scope != "global":
            raise ValueError(f"Warning: {self.__id} is not global")
        self.__commands = self.__old_commands

    @property
    def name(self) -> str:
        if not self.active:
            raise ValueError(f"Warning: {self.__id} is not active")
        if self.scope == "global":
            return self.__id
        elif self.scope == "local":
            return f"l_{self.__id}"
        elif self.scope == "system":
            return f"_{self.__id}"
        elif self.scope == "tmp":
            return f"{self.__id}"
        else:
            return f"{self.scope}_{self.__id}"

    def __set(self, expression: Expression | int | float | str) -> Command:
        cmd = Command(f"{self.name}={expression}")
        self.__commands << (cmd)
        self.used = True
        return cmd

    def set(
        self, expression: Expression | int | float | str, add: bool = True
    ) -> Command:
        if self.__read_only:
            raise ValueError(f"Warning: {self.name} is read only")
        if add:
            return self.__set(expression)
        return Command(f"{self.name}={expression}")

    def __lshift__(self, ohter):
        self.set(ohter)

    def delete(self):
        if self.used:
            self.__commands << Command(f"{self.name}=")
        del self.__commands.scalars[self.name]
        self.active = False