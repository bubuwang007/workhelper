from __future__ import annotations
import os
import typing

if typing.TYPE_CHECKING:
    from ..Mac import Mac

from ..Expression import Expression
from ..Processor import *
from ..Command import Command

class System:

    def __init__(self, commands: Mac):
        self.commands = commands

    @all
    def print(self, *args) -> Command:
        """ 在ANSYS黑窗口打印消息
        
        Args:
            *args: 消息内容
        
        Returns:
            Command: 命令

        """
        paras = []
        for i in args:
            if isinstance(i, Expression):
                paras.append(f"%{i}%")
            else:
                paras.append(f"{i}")
        return Command(f"/COM,{''.join(paras)}")

    @all
    def FINISH(self) -> Command:
        """结束当前模块"""
        return Command("FINISH")

    @all
    def CLEAR(self, start: bool = True) -> Command:
        if start:
            return Command("/CLEAR,START")
        else:
            return Command("/CLEAR,NOSTART")

    @begin
    def PSEARCH(self, pathstr: str) -> Command:
        pathstr = os.path.abspath(pathstr)
        if not os.path.exists(pathstr):
            os.makedirs(pathstr)
        return Command(f"/PSEARCH,'{pathstr}'")

    @all
    def print_enabled(self, flag: bool=True) -> Command:
        if flag:
            return Command(f"/GO")
        else:
            return Command(f"/NOPR")

    @all
    def CWD(self, path: str) -> Command:
        path = os.path.abspath(path)
        return Command(f"/CWD,'{path}'")

    @all
    def FILNAME(self, filename: str) -> Command:
        return Command(f"/FILNAME,'{filename}'")

    @all
    def TITLE(self, name: str) -> Command:
        return Command(f"/TITLE,'{name}'")

    @all
    def warning(self, flag: bool=True) -> Command:
        if flag:
            return Command("/UIS,MSGPOP,0")
        else:
            return Command("/UIS,MSGPOP,3")
       
    def begin(self, *, filename: str, title: str, directory: str, paths: list[str]=[]):
        self.FINISH()
        self.CLEAR(True)
        for i in paths:
            self.PSEARCH(i)
        self.FILNAME(filename)
        self.TITLE(title)
        self.CWD(directory)

    def NERR(self, nmerr, nmabt, ifkey: int|str='', num: int|str='') -> Command:
        '''Limits the number of warning and error messages displayed.
            NMERR
                Maximum number of warning and error messages displayed per command.
            NMABT
                Maximum number of warning and error messages allowed per command before run aborts (must be greater than zero).
            IFKEY
                Specifies whether or not to abort if an error occurs during a /INPUT operation:
                0 — Do not abort.
                1 — Abort.
            NUM
                The number of invalid command warnings before a stop warning will be issued:
                0 — Disables the stop warning/error function.
                n — An integer value representing the number of warnings that will be encountered before prompting the user to stop (default = 5).
        '''
        return Command(f"/NERR,{nmerr},{nmabt},,{ifkey},{num}")
