from __future__ import annotations
import re

class BaseExpression:
    def __init__(self, apdl: str):
        if len(apdl) > 256:
            raise ValueError(f"Expression too long: {apdl}")
        self.apdl = apdl

    def __str__(self) -> str:
        return self.apdl

    def __repr__(self) -> str:
        return repr(self.apdl)

class Expression(BaseExpression):
    operator = re.compile(r"(\+|\-|\*|\/|\*\*)")

    def __add__(self, other) -> Expression:
        return Expression(f"{self}+{other}")

    def __radd__(self, other) -> Expression:
        return Expression(f"{other}+{self}")

    def __sub__(self, other) -> Expression:
        a, b = self, self.__check_operator(other)
        return Expression(f"{a}-{b}")

    def __rsub__(self, other) -> Expression:
        a, b= self.__check_operator(self), other
        return Expression(f"{b}-{a}")

    def __check_operator(self, other) -> str:
        return f"({other})" if re.search(self.operator, str(other)) else str(other)

    def __mul__(self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a}*{b}")

    def __rmul__(self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{b}*{a}")

    def __truediv__(self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a}/{b}")

    def __rtruediv__(self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{b}/{a}")

    def __pow__(self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a}**{b}")

    def __rpow__(self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{b}**{a}")

    def __lt__ (self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a},LT,{b}")

    def __le__ (self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a},LE,{b}")

    def __eq__ (self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a},EQ,{b}")

    def __ne__ (self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a},NE,{b}")

    def __gt__ (self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a},GT,{b}")

    def __ge__ (self, other) -> Expression:
        a, b = self.__check_operator(self), self.__check_operator(other)
        return Expression(f"{a},GE,{b}")

    def __neg__(self) -> Expression:
        a = self.__check_operator(self)
        return Expression(f"-{a}")

    def sqrt(self) -> Expression:
        return Expression(f"SQRT({self})")