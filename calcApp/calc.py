import re

EXP_PTR = re.compile(r"^\s*(\-?\s*\d+)\s*([\+|\-|\*|\/])(\s*\d+)\s*$")

# Return a list with the expression [d1, op, d2]. If it fails, returns []
def validate_expression(exp: str) -> list:
    match = EXP_PTR.findall(exp)
    if (not match):
        return []
    mt = [m.replace(" ", "") for m in match[0]]

    return  [float(mt[0]), mt[1], float(mt[2])]

def evaluate_expression(exp: list) -> float:
    if (len(exp) != 3):
        return 0

    if (exp[1] == "+"):
        return exp[0] + exp[2]
    if (exp[1] == "-"):
        return exp[0] - exp[2]
    if (exp[1] == "*"):
        return exp[0] * exp[2]
    if (exp[1] == "/"):
        return exp[0] / exp[2]

    return 0
