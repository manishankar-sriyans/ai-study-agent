import ast, operator as op
OPS = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv, ast.Pow: op.pow}
def _eval(n):
    if isinstance(n, ast.Constant): return n.value
    if isinstance(n, ast.BinOp): return OPS[type(n.op)](_eval(n.left), _eval(n.right))
    raise ValueError("unsupported")
def calculator(expression): return str(_eval(ast.parse(expression, mode="eval").body))
def save_note(text):
    open("notes.txt", "a").write(text + "\n"); return "saved"
def read_notes():
    try: return open("notes.txt").read() or "empty"
    except FileNotFoundError: return "empty"
TOOLS = {"calculator": calculator, "save_note": save_note, "read_notes": read_notes}
