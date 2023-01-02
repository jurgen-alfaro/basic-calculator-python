from __future__ import annotations  # To use decorators


class Calculator:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return "<class 'Calculator'>"

    @staticmethod
    def add(a: int, b: int) -> None:
        answer = a + b
        print(f"{a} + {b} = {answer}\n")

    @staticmethod
    def sub(a: int, b: int) -> None:
        answer = a - b
        print(f"{a} - {b} = {answer}\n")

    @staticmethod
    def mult(a: int, b: int) -> None:
        answer = a * b
        print(f"{a} * {b} = {answer}\n")

    @staticmethod
    def div(a: int, b: int) -> None:
        try:
            answer = a / b
            print(f"{a} / {b} = {answer:.2f}\n")
        except ZeroDivisionError:
            print("Can't divide by zero\n")
