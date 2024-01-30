import re
from collections.abc import Iterable

re_dot = re.compile(r'\.$')
re_0_dot = re.compile(r'\.0*$')
re_0 = re.compile(r'0+$')

def float2str(f):
    s = str(f)
    s = re_0.sub("", s)
    return re_dot.sub("", s)

def clear_float_last_zero(s):
    if isinstance(s, str):
        return re_0_dot.sub('', s)
    if isinstance(s, Iterable):
        return [re_0_dot.sub('', str(i)) for i in s]
    return re_0_dot.sub('', str(s))