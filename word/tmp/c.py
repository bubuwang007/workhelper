import re

a = rf"(?P<num>\d+(\.\d+))"
b = rf"(?P<name>a|b|c)"
c = rf"(?P<type>int|float|str)"

pattern = re.compile(rf"{a}|{b}|{c}")
string = "123.456a v b v c int"

for i in pattern.finditer(string):
    print(i.groupdict())
    print(i.lastgroup)
    print(i.group())
