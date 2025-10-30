"""
core module for joytide

we will add our function here in our own branch.
after finishing a function we will need to add tests for them in the tests folder

for now this file is empty on purpose.
"""


def banner(
    text: str, border: str = "*", padding: int = 1, align: str = "center"
) -> str:
    """
    Make a simple ASCII banner.
    align: 'left' | 'center' | 'right'
    """
    if not isinstance(text, str):
        raise TypeError("text must be str")
    if not isinstance(border, str) or len(border) == 0:
        raise ValueError("border must be a non-empty string")
    if not isinstance(padding, int) or padding < 0:
        raise ValueError("padding must be >= 0")
    if align not in {"left", "center", "right"}:
        raise ValueError("align must be 'left', 'center', or 'right'")

    inner_width = len(text) + padding * 2

    if align == "left":
        inner = text.ljust(inner_width)
    elif align == "right":
        inner = text.rjust(inner_width)
    else:
        inner = text.center(inner_width)

    middle = f"{border}|{inner}|{border}"
    top = border * len(middle)
    bottom = top
    return "\n".join([top, middle, bottom])
