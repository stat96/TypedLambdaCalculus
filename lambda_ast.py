# AST definitions for Typed Lambda Calculus
class Expr:
    pass
class Var(Expr):
    def __init__(self, name: str): self.name = name
    def __str__(self): return self.name
class Abs(Expr):
    def __init__(self, param: str, param_type, body):
        self.param = param
        self.param_type = param_type
        self.body = body
    def __str__(self): return f"(λ{self.param}:{self.param_type}. {self.body})"
class App(Expr):
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg
    def __str__(self): return f"({self.func} {self.arg})"
class IntLit(Expr):
    def __init__(self, value: int): self.value = value
    def __str__(self): return str(self.value)
class BoolLit(Expr):
    def __init__(self, value: bool): self.value = value
    def __str__(self): return str(self.value)
