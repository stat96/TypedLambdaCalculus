# Type inference for Typed Lambda Calculus (System F)
from ast import Var, Abs, App, IntLit, BoolLit
from types import TInt, TBool, TFun

def infer_type(expr, ctx=None):
    ctx = ctx or {}
    if isinstance(expr, Var):
        return ctx.get(expr.name, None)
    elif isinstance(expr, IntLit):
        return TInt()
    elif isinstance(expr, BoolLit):
        return TBool()
    elif isinstance(expr, Abs):
        ctx2 = ctx.copy()
        ctx2[expr.param] = expr.param_type
        body_type = infer_type(expr.body, ctx2)
        return TFun(expr.param_type, body_type)
    elif isinstance(expr, App):
        func_type = infer_type(expr.func, ctx)
        arg_type = infer_type(expr.arg, ctx)
        if isinstance(func_type, TFun) and func_type.arg == arg_type:
            return func_type.ret
        return None
    return None
