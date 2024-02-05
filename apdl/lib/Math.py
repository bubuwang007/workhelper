from __future__ import annotations
import typing
from ..Expression import Expression

PARA = typing.TypeVar("PARA", Expression, int, float)

class Math:
    PI = 3.1415926
    E = 2.7182818

    @staticmethod
    def abs(expression: PARA) -> Expression:
        """绝对值"""
        return Expression(f"ABS({expression})")
    
    @staticmethod
    def sign(x: PARA, y:PARA) -> Expression:
        """y的正负号*x的绝对值"""
        return Expression(f"SIGN({x}, {y})")
    
    @staticmethod
    def exp(expression: PARA) -> Expression:
        """e"""
        return Expression(f"EXP({expression})")

    @staticmethod
    def log(expression: PARA) -> Expression:
        """ln"""
        return Expression(f"LOG({expression})")
    
    @staticmethod
    def log10(expression: PARA) -> Expression:
        """log10"""
        return Expression(f"LOG10({expression})")
    
    @staticmethod
    def sqrt(expression: PARA) -> Expression:
        """开方"""
        return Expression(f"SQRT({expression})")
    
    @staticmethod
    def round(expression: PARA) -> Expression:
        """四舍五入"""
        return Expression(f"NINT({expression})")
    
    @staticmethod
    def mod(expression: PARA, divisor: PARA) -> Expression:
        """取余"""
        return Expression(f"MOD({expression}, {divisor})")

    @staticmethod
    def rand(x:PARA, y:PARA) -> Expression:
        """获取x-y之间的随机数"""
        return Expression(f"RAND({x}, {y})")
    
    @staticmethod
    def GDIS(mean: PARA, std: PARA) -> Expression:
        """正态分布"""
        return Expression(f"GDIS({mean}, {std})")

    @staticmethod
    def sin(expression: PARA) -> Expression:
        """正弦"""
        return Expression(f"SIN({expression})")

    @staticmethod
    def cos(expression: PARA) -> Expression:
        """余弦"""
        return Expression(f"COS({expression})")

    @staticmethod
    def tan(expression: PARA) -> Expression:
        """正切"""
        return Expression(f"TAN({expression})")

    @staticmethod
    def asin(expression: PARA) -> Expression:
        """反正弦"""
        return Expression(f"ASIN({expression})")

    @staticmethod
    def acos(expression: PARA) -> Expression:
        """反余弦"""
        return Expression(f"ACOS({expression})")

    @staticmethod
    def atan(expression: PARA) -> Expression:
        """反正切"""
        return Expression(f"ATAN({expression})")

    @staticmethod
    def sinh(expression: PARA) -> Expression:
        """双曲正弦"""
        return Expression(f"SINH({expression})")

    @staticmethod
    def cosh(expression: PARA) -> Expression:
        """双曲余弦"""
        return Expression(f"COSH({expression})")

    @staticmethod
    def tanh(expression: PARA) -> Expression:
        """双曲正切"""
        return Expression(f"TANH({expression})")

