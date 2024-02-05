from __future__ import annotations


class Command:
    """命令类

    存储命令的相关信息，包括命令字符串、命令前缀、是否为注释、命令类型、回调函数等

    Attributes:
        cmd (str): 代表命令的字符串
        indent (str): 缩进数
        comment (bool): 是否为注释
    """

    cmd: str
    indent: int
    is_comment: bool

    def __init__(
        self,
        cmd: str,
        is_comment: bool = False,
        comment: str = ""
    ):
        """初始化命令

        Args:
            cmd (str): 命令字符串
            indent (int, optional): 缩进数. Defaults to 0.
            comment (bool, optional): 是否为注释. Defaults to False.
        """
        self.indent = 0
        self.cmd = cmd
        self.is_comment = is_comment
        if is_comment and comment != "":
            raise ValueError("Comment should not have a comment.")
        self.comment = comment

    def __str__(self):
        """命令流

        Returns:
            str: 命令流
        """
        indent = " " * 4 * self.indent
        is_comment = "! " if self.is_comment else ""
        if self.comment != "":
            comment = " ! " + self.comment
        else:
            comment = ""
        return indent + is_comment + self.cmd + comment

    def __repr__(self) -> str:
        return repr(self.__str__())

    def __iadd__(self, other: Command) -> Command:
        self.__check_is_modify()
        other.__check_is_modify()
        self.cmd += "$" + other.cmd
        return self

    def __add__(self, other: Command):
        self.__check_is_modify()
        other.__check_is_modify()
        return Command(self.cmd + "$" + other.cmd)

    def __check_is_modify(self):
        if self.is_comment:
            raise Exception("Cannot add command to a comment or a task.")