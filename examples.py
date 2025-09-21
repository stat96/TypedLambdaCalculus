# Example programs for Typed Lambda Calculus
from lambda_ast import Abs, Var, IntLit
from lambda_types import TInt

def get_examples():
    # λx:Int. x
    id_int = Abs("x", TInt(), Var("x"))
    # (λx:Int. x) 42
    app = (id_int, IntLit(42))
    return id_int, app
