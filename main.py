
from mypackage import utils, math_helpers, string_helpers
import mypackage.nested.deep
print(utils.greet("Аня"))
print(utils.add(2, 3))
print(utils.PI)
print(math_helpers.square(5))
print(math_helpers.square_str(5))       # ← новая функция
print(string_helpers.uppercase("hello"))
print(string_helpers.reverse("abc"))
