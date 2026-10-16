# mypackage/math_helpers.py
from .string_helpers import uppercase
def square(x):
    return x * x

def square_str(x):
    return uppercase(f"квадрат {x} равен {x*x}")