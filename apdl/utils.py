import re

re_identifier = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")

def check_identifier(name: str) -> None:
    """检查变量名是否合法和长度是否超过32个字符
    
    Args:
        name (str): 变量名
    
    Raises:
        ValueError: 变量名不合法
    """
    if not re_identifier.match(name):
        raise ValueError(f"Invalid identifier {name}")
    if len(name) > 32:
        raise ValueError(f"Identifier {name} is too long")

def is_number(s)->bool:
    try:
        float(s)
        return True
    except ValueError:
        return False