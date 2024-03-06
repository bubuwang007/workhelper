from abc import ABCMeta, abstractmethod
from .Mac import Mac

class Segment(Mac, metaclass=ABCMeta):
    """可调用的宏文件
    必须实现单例模式
    继承使用
    """
    name: str="a_a"

    def __init__(self):
        super().__init__(self.name)
        self.actions()

    @abstractmethod
    def actions(self):
        pass

    def save(self):
        raise NotImplementedError

    def output(self, path: str):
        raise NotImplementedError