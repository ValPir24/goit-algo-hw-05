import re
from typing import Callable

def generator_numbers(text: str): # Functions finds numbers in input text
    for value in re.findall(r"(?<=\s)\d+\.\d+(?=\s)|(?<=\s)\d+(?=\s)", text):
        yield float(value)

def sum_profit(text: str, func: Callable): # Function caclulates sum of all numbers
    total_income = 0
    for i in func(text):
        total_income += i
    return total_income

# Debugging
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")