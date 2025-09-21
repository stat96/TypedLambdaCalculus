# Type definitions for Typed Lambda Calculus
class Type:
    pass
class TInt(Type):
    def __str__(self): return "Int"
    def __eq__(self, other): return isinstance(other, TInt)
class TBool(Type):
    def __str__(self): return "Bool"
    def __eq__(self, other): return isinstance(other, TBool)
class TFun(Type):
    def __init__(self, arg: Type, ret: Type):
        self.arg = arg
        self.ret = ret
    def __str__(self): return f"({self.arg} -> {self.ret})"
    def __eq__(self, other):
        return isinstance(other, TFun) and self.arg == other.arg and self.ret == other.ret
