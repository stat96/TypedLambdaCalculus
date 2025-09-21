# Type checker for Typed Lambda Calculus
from lambda_types import Type, TInt, TBool, TFun
from lambda_ast import Expr, Var, Abs, App, IntLit, BoolLit
Context = dict

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
