from __future__ import annotations
import os
from typing import Any

from .Command import Command
from .Commands import Commands
from .Processor import Processor
from .Scalar import Scalar
from .Array import Array
from .Do import Do
from .If import If


class Mac(Commands):
    name: str
    macs: set[type[Mac]]
    paras: list[str]
    scalars: dict[str, Scalar]
    arrays: dict[str, Array]
    debug: bool = False
    processor: Processor = Processor.begin
    tmp_index: int = 0
    tmp_array_index: int = 0

    def __init__(self, name: str):
        self.name = name
        self.macs = set()
        self.scalars = {}
        self.arrays = {}
        super().__init__()

    def use(self, mac) -> None:
        """添加要使用的宏

        Args:
            mac (type[Mac]): 宏文件的类

        """
        self.macs.add(mac)

    def switch_processor(self, processor: Processor) -> None:
        """切换所处的处理器

        主要通过额外实现的命令中调用, 不单独调用

        Args:
            processor (Processor): 需要切换的处理器

        """
        if processor != self.processor:
            self.processor = processor
            self.append(Command(processor.value))

    def finish(self) -> None:
        """结束命令流"""
        self.append(Command("FINISH"))
        self.processor = Processor.begin

    def prep7(self) -> None:
        """切换到prep7处理器"""
        self.switch_processor(Processor.prep7)

    def post26(self) -> None:
        """切换到post26处理器"""
        self.switch_processor(Processor.post26)

    def post1(self) -> None:
        """切换到post1处理器"""
        self.switch_processor(Processor.post1)

    def solu(self) -> None:
        """切换到solu处理器"""
        self.switch_processor(Processor.solu)

    def opt(self) -> None:
        """切换到opt处理器"""
        self.switch_processor(Processor.opt)

    def pds(self) -> None:
        """切换到pds处理器"""
        self.switch_processor(Processor.pds)

    def aux2(self) -> None:
        """切换到aux2处理器"""
        self.switch_processor(Processor.aux2)

    def aux12(self) -> None:
        """切换到aux12处理器"""
        self.switch_processor(Processor.aux12)

    def aux15(self) -> None:
        """切换到aux15处理器"""
        self.switch_processor(Processor.aux15)

    def runstat(self) -> None:
        """切换到runstat处理器"""
        self.switch_processor(Processor.runstat)

    def scalar(
        self, name: str, value=None, scope: str = "local", read_only=False
    ) -> Scalar:
        scalar = Scalar(name, self, value, scope, read_only)
        name = scalar.name
        if name in self.scalars:
            raise ValueError(f"Parameter {name} already exists")
        self.scalars.update({name: scalar})
        return scalar

    def tmp_scalar(self, value=None):
        self.tmp_index += 1
        return self.scalar(f"{self.name}{self.tmp_index}", value, scope="tmp")

    def __gt__(self, other: Any) -> Scalar:
        return self.tmp_scalar(other)

    def global_scalar(self, name: str, value=None, read_only=False) -> Scalar:
        return self.scalar(name, value, scope="global", read_only=read_only)

    def del_scalar(self, scalar: Scalar) -> None:
        scalar.delete()

    def Do(self, range: tuple) -> Do:
        return Do(self, range)

    def If(self, expression: str) -> If:
        return If(self, expression)

    def array(self, name: str, dimensions, scope: str = "local") -> Array:
        array = Array(name, dimensions, self, scope)
        name = array.name
        if name in self.arrays:
            raise ValueError(f"Array {name} already exists")
        self.arrays.update({name: array})
        return array

    def tmp_array(self, dimensions=None, data=None) -> Array:
        self.tmp_array_index += 1
        if dimensions is None and data is None:
            raise ValueError("Invalid parameters")
        if dimensions is not None and data is not None:
            arr = self.array(f"a{self.name}{self.tmp_index}", dimensions, scope="tmp")
            arr << data
        if dimensions is not None and data is None:
            arr = self.array(f"a{self.name}{self.tmp_index}", dimensions, scope="tmp")
        return arr

    def array_from_list(self, name: str, lst: list, scope: str = "local") -> Array:
        if not isinstance(lst, list):
            raise ValueError(f"Invalid type: {type(lst)}")
        if len(lst) == 0:
            raise ValueError(f"Invalid length: {len(lst)}")
        if isinstance(lst[0], list):
            row = len(lst)
            col = len(lst[0])
            array = self.array(name, (row, col), scope)
        else:
            row = len(lst)
            array = self.array(name, (row, 1), scope)
        array << lst
        return array

    def del_array(self, array: Array) -> None:
        array.delete()

    def end(self) -> None:
        """结束命令流(包含清理局部变量和数组)"""
        tmp = []
        for para in self.arrays.values():
            if para.scope not in ["system", "global"]:
                tmp.append(para)
        if len(tmp) > 0:
            self.block("清理数组")
        for i in tmp:
            self.del_array(i)

        tmp = []
        for para in self.scalars.values():
            if para.scope not in ["system", "global"] and para.used:
                tmp.append(para)
        if len(tmp) > 0:
            self.block("清理局部变量")
        for i in tmp:
            self.del_scalar(i)

    def save(self, path: str) -> str:
        """保存命令流到文件

        Args:
            path (str): 保存文件路径

        """
        with open(os.path.join(path, f"{self.name}.mac"), "w", encoding="u8") as f:
            f.write(str(self))
        print(f"Save {self.name}.mac")
        return os.path.abspath(os.path.join(path, f"{self.name}.mac"))

    def output(self, path: str) -> None:
        """输出命令流到文件

        Args:
            path (str): 输出文件路径

        """
        self.save(path)
        macs = set()
        stack = list(self.macs)
        while stack:
            mac = stack.pop()
            macs.add(mac)
            for m in mac.macs:
                stack.append(m)
        for mac in macs:
            mac.save(path)

    def excute(self, func, *args):
        self.use(func)
        self << func.call(*args)
        self.processor = func.processor

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return self.name
    
    def run(self, path: str):
        from mtl.launch._Launch import _Launch as Launch
        self.output(path)
        file = os.path.join(path, f"{self.name}.mac")
        Launch(check=True).launch_by_file(file)