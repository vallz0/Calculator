import math


class Calculator:
    def calculate(self, expression: str) -> float:
        expression = expression.replace("x", "*")
        expression = expression.replace("^", "**")
        expression = expression.replace("%", "/100*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("√", "**0.5")
        expression = expression.replace("!", "math.factorial(")

        if "*+" in expression:
            raise ValueError("Equação inválida.")

        return eval(expression)
