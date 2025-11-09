#!/usr/bin/env python3
from math import *
import pyfiglet
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich.text import Text

try:
    #Theme Declaration
    Theme = Theme({"instruction": "bold yellow", "error": "bold red"})
    console = Console(theme=Theme)

    # Banner
    banner = pyfiglet.figlet_format("ConsoleX")
    print("\n",banner,end="")

    #Help Table Declaration
    table = Table(
        title="Commands",
        title_justify='center',
        show_header= True,
        header_style="bold magenta",
    )
    table.add_column("Command",
                     style="bold cyan",
                     width=10)
    table.add_column('Description',
                     style="white",
                     min_width=12,
                     max_width=60)
    table.add_column('Example',
                     style="bold green",
                     width=25)
    math_data = [
        # Trig Functions (Input in Radians)
        ("sin", "Returns the sine of a number (input is in radians)", "sin(radiant)"),
        ("cos", "Returns the cosine of a number (input is in radians)", "cos(radiant)"),
        ("tan", "Returns the tangent of a number (input is in radians)", "tan(radiant)"),

        # Inverse Trig Functions (Output in Radians)
        ("asin", "Returns the arc sine of a number (output is in radians)", "asin(number)"),
        ("acos", "Returns the arc cosine of a number (output is in radians)", "acos(number)"),
        ("atan", "Returns the arc tangent of a number (output is in radians)", "atan(number)"),
        ("atan2", "Returns the arc tangent of y/x (output is in radians)", "atan2(y, x)"),

        # Hyperbolic Functions
        ("sinh", "Returns the hyperbolic sine of a number", "sinh(number)"),
        ("cosh", "Returns the hyperbolic cosine of a number", "cosh(number)"),
        ("tanh", "Returns the hyperbolic tangent of a number", "tanh(number)"),

        # Inverse Hyperbolic Functions
        ("asinh", "Returns the inverse hyperbolic sine of a number", "asinh(number)"),
        ("acosh", "Returns the inverse hyperbolic cosine of a number", "acosh(number)"),
        ("atanh", "Returns the inverse hyperbolic tangent of a number", "atanh(number)"),

        # Rounding Functions
        ("ceil", "Rounds a number up to the nearest integer", "ceil(number)"),
        ("floor", "Rounds a number down to the nearest integer", "floor(number)"),
        ("trunc", "Returns the truncated integer parts of a number", "trunc(number)"),

        # Power and Logarithmic Functions
        ("pow", "Returns the value of x to the power of y", "pow(x, y)"),
        ("sqrt", "Returns the square root of a number", "sqrt(number)"),
        ("exp", "Returns E raised to the power of x", "exp(x)"),
        ("log", "Returns the natural logarithm (base e) or log to a base", "log(number, base)"),
        ("log10", "Returns the base-10 logarithm of a number", "log10(number)"),

        # Conversion Functions
        ("degrees", "Converts an angle from radians to degrees", "degrees(radiant)"),
        ("radians", "Converts a degree value into radians", "radians(degree)"),

        # Other Common Functions
        ("fabs", "Returns the absolute value of a number", "fabs(number)"),
        ("factorial", "Returns the factorial of a number", "factorial(number)"),
        ("gcd", "Returns the greatest common divisor of two integers", "gcd(a, b)"),
        ("fsum", "Returns an accurate floating-point sum of items in an iterable", "fsum(iterable)"),
        ("dist", "Returns the Euclidean distance between two points", "dist(point_1, point_2)"),

        # Constants
        ("pi", "Returns the constant PI (3.1415...)", "pi"),
        ("e", "Returns Euler's number, the base of natural logarithms (2.7182...)", "e"),
        ("tau", "Returns the constant Tau (6.2831...)", "tau"),
        ("inf", "Returns a floating-point positive infinity", "inf"),
        ("nan", "Returns a floating-point 'Not a Number' (NaN) value", "nan"),
    ]
    for data in math_data:
        table.add_row(data[0], data[1], data[2])

    #Instruction
    console.print("""[bold yellow]
INSTRUCTIONS
1. Square Root = sqrt(value)
2. π = pi
3. sin(radian), cos(radian), tan(radian) are to be passed
4. There is no sec(),cosec(),cot()
5. For power operation use ** or pow()
6. Special Characters are not allowed
8. Use 'ANS' or 'ANSWER' for previous expression's answer
9. Expressions are Not Case Sensitive[/]
""", style='instruction')

    console.print("ENTER [bold red]'q'[/] or [bold red]'Q'[/] TO QUIT\n", style="instruction")
    try:
        ans = [0, 0]
        while True:
            expression = console.input("[bold cyan]Enter your expression: [/]").lower()
            if expression.strip() == 'q' or expression.strip() in  "quit":
                break
            elif expression.strip() ==  'h' or expression.strip() in 'help':
                console.print(table)
            else:
                if (expression.endswith('+') or expression.endswith('-')):
                    expression = expression+'0'
                elif (expression.endswith('*') or expression.endswith('/') or expression.endswith('**')):
                    expression = expression+'1'
                elif (expression.startswith('*') or expression.startswith('/')):
                    expression = '1'+expression
                expression = expression.replace("answer","ans")
                expression = expression.replace("ans", "ans[1]")
                value = eval(expression)
                console.print(Text(str(value), style="bold white"))
                if (ans == 'answer') or (ans == 'ans'):
                    ans[1] = ans[0]
                else:
                    ans[0] = ans[1]
                    ans[1] = value
    except:
        console.print("\nInvalid Expression: Enter a valid expression.\n", style='error')
except:
    console.print("UnExpected Error: Try Again\n", style="error")
quit()
print()