import re

EXP_PTR = re.compile(r"^\s*(\-?\s*\d+(?:\.\d+)?)\s*([\+\-]|[\*\/]\s*\-?)(\s*\d+(?:\.\d+)?)\s*$")

# Return a list with the expression [d1, op, d2]. If it fails, returns []
def validate_expression(exp: str) -> list:
    match = EXP_PTR.findall(exp)
    if (not match):
        return []
    mt = [m.replace(" ", "") for m in match[0]]

    signal = 1
    # Ex: mt[1] = "*-" means the second argument is negative
    if (len(mt[1]) == 2):
        mt[1] = mt[1][0]
        signal = -1

    return  [float(mt[0]), mt[1], signal*float(mt[2])]

def evaluate_expression(exp: list) -> float:
    if (len(exp) != 3):
        return 0

    if (exp[1] == "+"):
        return exp[0] + exp[2]
    if (exp[1] == "-"):
        return exp[0] - exp[2]
    if (exp[1] == "*"):
        return exp[0] * exp[2]
    # if (exp[1] == "/"):
    #     if (exp[2] == 0):
    #         raise ZeroDivisionError()
    #     return exp[0] / exp[2]

    return 0
