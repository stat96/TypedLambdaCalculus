 # Main entry for Typed Lambda Calculus Interpreter
from lambda_ast import Abs, Var, IntLit, App
from lambda_types import TInt
from typechecker import type_of
from evaluator import eval_expr

def main():
    # λx:Int. x
    id_int = Abs("x", TInt(), Var("x"))
    # (λx:Int. x) 42
    app = App(id_int, IntLit(42))
    ctx = {}
    print("Expression:", app)
    print("Type:", type_of(app, ctx))
    print("Evaluated:", eval_expr(app, {}))

if __name__ == "__main__":
    main()
