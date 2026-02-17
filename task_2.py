import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"(?<=\s)\d+(?:\.\d+)?(?=\s)"
    
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))
if __name__ == "__main__":
    text = " 1000.01  27.45  324.00 "
    print(sum_profit(text, generator_numbers))