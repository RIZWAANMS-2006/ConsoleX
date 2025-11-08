# ConsoleX
A beautiful and powerful terminal calculator built with Python.
ConsoleX is a small interactive math expression evaluator with a formatted help table and colored console output using `rich` and banner rendering via `pyfiglet`.

## Features
- Interactive expression evaluation (uses Python `eval` for expressions)
- Built-in math functions and constants (via `math`)
- Colored output and help table (uses `rich`)
- ASCII banner (uses `pyfiglet`)
- Keeps last two results accessible via `ANS` / `ANSWER`

## Requirements
- Python 3.8+ (tested on Windows)
- Packages listed in `requirements.txt`:
  - `rich`
  - `pyfiglet`

## Installation
1. Clone the repository.
2. Create a virtual environment (recommended):
   - `python -m venv venv`
   - `venv\Scripts\activate`
3. Install dependencies:
   - `pip install -r requirements.txt`

## Usage
Run the program from the project root:
- `python ConsoleX.py`

Interactive controls:
- Enter an expression (e.g. `sqrt(9)`, `sin(pi/2)`, `2**10`)
- Use `ANS` or `ANSWER` to refer to previous results
- Type `h` or `help` to show command table
- Type `q` or `Q` to quit

Examples:
- `sqrt(16)`
- `pow(2, 8)`
- `sin(pi/2)`

## Output
<img width="1920" height="1128" alt="C__Windows_System32_cmd exe - powershell 11_8_2025 1_13_18 PM" src="https://github.com/user-attachments/assets/d147de20-6814-4371-82d1-e3d32e63fcd5" />


## Troubleshooting: styling / color not showing
If `console.print(value, style="red")` or other styles do not appear colored:
- Run the program in a terminal that supports ANSI colors, e.g. Windows Terminal, PowerShell, or Git Bash. Classic `cmd.exe` on older Windows may not show colors.
- Ensure `rich` is up to date: `pip install -U rich`.
- Use `console.print(Text(str(value), style="red"))` to apply explicit `Text` styling.
- Avoid using plain `print()` for styled output; use `console.print()` consistently.
- If needed, force a truecolor/ANSI-aware console by creating `Console` with parameters (see `rich` docs).

## Security note
This program evaluates user input with Python's `eval`. Do not run untrusted code. Consider replacing `eval` with a safe expression parser if you plan to accept input from untrusted sources.

## Files
- `ConsoleX.py` \- main program
- `requirements.txt` \- dependency list

## Contributing
- Open issues or pull requests on the repository.
- Follow standard Python style and include tests where applicable.

## License
MIT License. See `LICENSE` for details.
