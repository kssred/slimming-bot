from typing import Any


def is_float(value: Any) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_integer(value: Any) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
