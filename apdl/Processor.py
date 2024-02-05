import enum
from functools import wraps


class Processor(enum.Enum):
    begin = "FINISH"
    prep7 = "/PREP7"
    post26 = "/POST26"
    post1 = "/POST1"
    solu = "/SOLU"
    opt = "/OPT"
    pds = "/PDS"
    aux2 = "/AUX2"
    aux12 = "/AUX12"
    aux15 = "/AUX15"
    runstat = "/RUNSTAT"


def all(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        args[0].commands.append(ret)
        return ret
    return wrapper


def wrapper_processor(processor: Processor):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            commands = args[0].commands
            if commands.processor != processor:
                commands.switch_processor(processor)
            ret = func(*args, **kwargs)
            args[0].commands.append(ret)
            return ret
        return wrapper
    return decorator


begin = wrapper_processor(Processor.begin)
prep7 = wrapper_processor(Processor.prep7)
post26 = wrapper_processor(Processor.post26)
post1 = wrapper_processor(Processor.post1)
solu = wrapper_processor(Processor.solu)
opt = wrapper_processor(Processor.opt)
pds = wrapper_processor(Processor.pds)
aux2 = wrapper_processor(Processor.aux2)
aux12 = wrapper_processor(Processor.aux12)
aux15 = wrapper_processor(Processor.aux15)
runstat = wrapper_processor(Processor.runstat)

__all__ = [
    "Processor",
    "all",
    "begin",
    "prep7",
    "post26",
    "post1",
    "solu",
    "opt",
    "pds",
    "aux2",
    "aux12",
    "aux15",
    "runstat",
]
