from abc import ABCMeta, abstractmethod
from .Mac import Mac
from .lib.System import System

class Func(Mac, metaclass=ABCMeta):
    """可调用的宏文件
    必须实现单例模式
    继承使用
    """
    name: str
    para_num: int = 0

    def __init__(self):
        super().__init__(self.name)
        sys = System(self)
        sys.FINISH()
        self.actions()

    @abstractmethod
    def actions(self):
        '''定义宏文件的内容
        需要在此方法中注意处理器的切换
        '''
        pass

    @abstractmethod
    def call(*args, **kwargs):
        pass

    def define_para(self):
        self.para_num += 1
        return self.scalar(f"arg{self.para_num}", scope="global")
