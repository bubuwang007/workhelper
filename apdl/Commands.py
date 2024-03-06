from __future__ import annotations
from collections.abc import Iterable
from .Command import Command
from collections import UserList

class Commands(UserList[Command]):
    """Command的容器, 继承自UserList

    主要用于后续的Apdl类的基础类, 目前不用于其他用途

    Args:
        prefix (str): 前缀

    """
    indent: int = 0

    def append(self, item: Command) -> None:
        """添加命令

        命令的前缀为self.prefix, 默认为空, 主要作用是在命令前加上缩进

        Args:
            item (Command):命令

        """
        item.indent = self.indent
        return super().append(item)

    def __lshift__(self, other: Command | Iterable[Command]| str):
        if isinstance(other, Command):
            self.append(other)
        elif isinstance(other, str):
            self.append(Command(other))
        elif isinstance(other, Iterable):
            self.extend(other)
        else:
            raise ValueError(f"Unsupported type: {type(other)}")
        return self

    def extend(self, other: Iterable[Command]) -> None:
        for i in other:
            i.indent = self.indent
            self.append(i)

    def blank(self) -> None:
        """添加空行"""
        self.append(Command(""))

    def comment(self, msg: str) -> None:
        """添加注释"""
        self.append(Command(f"{msg}", is_comment = True))

    def block(self, msg: str, star_num =45, line_length=40) -> None:
        """添加注释块

        注释块组成为一个空行、一行*号、注释内容、一行*号、一个空行

        Args:
            msg (str): 注释块内容
        
        Examples:
            >>> cmds = Commands()
            >>> cmds.block("This is a block")
            >>> cmds
            ['',
             '!*********************************************',
             '! This is a block',
             '!*********************************************',
             '']
        """
        self.blank()
        self.append(Command(f"!{'*'*star_num}"))
        start, end, length = 0, 0, 0
        for i in msg:
            if ord(i) < 128:
                length += 1
            else:
                length += 2
            if length >= line_length:
                self.append(Command(f"! {msg[start:end]}"))
                length = 0
                start = end
            end += 1
        else:
            self.append(Command(f"! {msg[start:]}"))
        self.append(Command(f"!{'*'*star_num}"))
        self.blank()
    
    def add_prefix(self) -> None:
        """添加缩进

        为每一行命令增加缩进, 每次增加4个空格
        """
        self.indent += 1

    def sub_prefix(self) -> None:
        """减少缩进

        为每一行命令减少缩进, 每次减少4个空格
        """
        self.indent -= 1

    def __str__(self) -> str:
        return "\n".join([str(i) for i in self.data])