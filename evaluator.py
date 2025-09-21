# Evaluator for Typed Lambda Calculus
from lambda_ast import Expr, Var, Abs, App, IntLit, BoolLit
Env = dict

def eval_expr(expr: Expr, env: Env):
    if isinstance(expr, Var):
        return env.get(expr.name, expr.name)
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
