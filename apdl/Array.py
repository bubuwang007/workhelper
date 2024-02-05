from __future__ import annotations
import typing

from .Command import Command
from .Do import Do
from .utils import check_identifier
from .Expression import BaseExpression, Expression

if typing.TYPE_CHECKING:
    from .Mac import Mac

class Array(BaseExpression):
    active: bool = True

    def __init__(self, name: str, dimensions, commands: Mac, scope: str = "local"):
        self.scope = scope
        self.__id = name
        self.__commands = commands
        self.__d_num = len(dimensions)
        self.__dimensions = []
        BaseExpression.__init__(self, f"{self.name}")
        check_identifier(self.name)
        for i in range(self.__d_num):
            tmp = self.__commands.scalar(f"{self.__id}_{i+1}", dimensions[i], scope=self.scope, read_only=True)
            self.__dimensions.append(tmp)
        self.__commands << f"*DIM,{self.name},arr,{self.row},{self.col},{self.plane}"

    @property
    def row(self):
        return self.__dimensions[0]
    
    @property
    def col(self):
        if self.__d_num < 2:
            return 1
        return self.__dimensions[1]

    @property
    def plane(self):
        if self.__d_num < 3:
            return 1
        return self.__dimensions[2]

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
    
    def __getitem__(self, key):
        if isinstance(key, int):
            key = (key,)
        return Expression(f"{self.name}({','.join([str(i) for i in key])})")
    
    def __setitem__(self, key, value):
        if isinstance(key, int):
            key = (key,)
        self.__commands << Command(f"{self.name}({','.join([str(i) for i in key])})={value}")

    def __lshift__(self, data):
        if isinstance(data, int|float|str):
            self[1, 1] = data
        elif isinstance(data, list):
            if isinstance(data[0], list):
                for i, row in enumerate(data, 1):
                    for j, value in enumerate(row, 1):
                        self[i, j] = value
            else:
                for i, value in enumerate(data, 1):
                    self[i] = value

    def iter_rows(self, start=1, end=None, step = 1) -> Do:
        if end is None:
            end = self.row
        return Do(self.__commands, (start, end, step))

    def iter_cols(self, start=1, end=None, step = 1) -> Do:
        if end is None:
            end = self.col
        return Do(self.__commands, (start, end, step))
    
    def iter_planes(self, start=1, end=None, step = 1) -> Do:
        if end is None:
            end = self.plane
        return Do(self.__commands, (start, end, step))

    def delete(self):
        for d in self.__dimensions:
            d.delete()
        del self.__commands.arrays[self.name]
        self.__commands << Command(f"{self.name}=")
        self.active = False