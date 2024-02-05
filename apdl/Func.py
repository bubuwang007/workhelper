from abc import ABCMeta, abstractmethod
from .Mac import Mac

class Func(Mac, metaclass=ABCMeta):
    """可调用的宏文件
    必须实现单例模式
    继承使用
    """
    name: str
    para_num: int = 0

    def __init__(self):
        super().__init__(self.name)
        self.actions()

    @abstractmethod
    def actions(self):
        pass

    @abstractmethod
    def call(*args, **kwargs):
        pass

    def define_para(self):
        self.para_num += 1
        return self.scalar(f"arg{self.para_num}", scope="global")
