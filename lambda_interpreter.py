"""
Typed Lambda Calculus Interpreter
Implements type checking and evaluation for simply typed lambda calculus.
"""
from typing import Union, Dict, Optional

# AST Definitions
class Type:
    pass

class TInt(Type):
    def __str__(self):
        return "Int"
    def __eq__(self, other):
        return isinstance(other, TInt)

class TBool(Type):
    def __str__(self):
        return "Bool"
    def __eq__(self, other):
        return isinstance(other, TBool)

class TFun(Type):
    def __init__(self, arg: Type, ret: Type):
        self.arg = arg
        self.ret = ret
    def __str__(self):
        return f"({self.arg} -> {self.ret})"
    def __eq__(self, other):
        return (
            isinstance(other, TFun)
            and self.arg == other.arg
            and self.ret == other.ret
        )

class Expr:
    pass

class Var(Expr):
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return self.name

class Abs(Expr):
    def __init__(self, param: str, param_type: Type, body: Expr):
        self.param = param
        self.param_type = param_type
        self.body = body
    def __str__(self):
        return f"(λ{self.param}:{self.param_type}. {self.body})"

class App(Expr):
    def __init__(self, func: Expr, arg: Expr):
        self.func = func
        self.arg = arg
    def __str__(self):
        return f"({self.func} {self.arg})"

class IntLit(Expr):
    def __init__(self, value: int):
        self.value = value
    def __str__(self):
        return str(self.value)

class BoolLit(Expr):
    def __init__(self, value: bool):
        self.value = value
    def __str__(self):
        return str(self.value)

# Type Checking
Context = Dict[str, Type]
def type_of(expr: Expr, ctx: Context) -> Type:
    if isinstance(expr, Var):
        if expr.name in ctx:
            return ctx[expr.name]
        raise TypeError(f"Unbound variable: {expr.name}")
    elif isinstance(expr, Abs):
        new_ctx = ctx.copy()
        new_ctx[expr.param] = expr.param_type
        body_type = type_of(expr.body, new_ctx)
        return TFun(expr.param_type, body_type)
    elif isinstance(expr, App):
        func_type = type_of(expr.func, ctx)
        arg_type = type_of(expr.arg, ctx)
        if isinstance(func_type, TFun) and func_type.arg == arg_type:
            return func_type.ret
        raise TypeError(f"Type mismatch in application: {func_type} applied to {arg_type}")
    elif isinstance(expr, IntLit):
        return TInt()
    elif isinstance(expr, BoolLit):
        return TBool()
    else:
        raise TypeError("Unknown expression type")

# Evaluation
Env = Dict[str, Union[int, bool, Expr]]
def eval_expr(expr: Expr, env: Env) -> Union[int, bool, Expr]:
    if isinstance(expr, Var):
        return env[expr.name]
    elif isinstance(expr, Abs):
        return expr
    elif isinstance(expr, App):
        func = eval_expr(expr.func, env)
        arg = eval_expr(expr.arg, env)
        if isinstance(func, Abs):
            new_env = env.copy()
            new_env[func.param] = arg
            return eval_expr(func.body, new_env)
        else:
            raise ValueError("Trying to apply non-function")
    elif isinstance(expr, IntLit):
        return expr.value
    elif isinstance(expr, BoolLit):
        return expr.value
    else:
        raise ValueError("Unknown expression type")

# Example Usage
def example():
    # λx:Int. x
    id_int = Abs("x", TInt(), Var("x"))
    # (λx:Int. x) 42
    app = App(id_int, IntLit(42))
    ctx = {}
    print("Expression:", app)
    print("Type:", type_of(app, ctx))
    print("Evaluated:", eval_expr(app, {}))

if __name__ == "__main__":
    example()
