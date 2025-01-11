from tkinter import StringVar
from customtkinter import CTk, CTkButton, CTkLabel
from calculator import Calculator
from constants import COLORS

class CalculatorUI:
    def __init__(self) -> None:
        self.window = CTk()
        self.window.title("Calc")
        self.window.geometry("315x450")
        self.window.config(bg=COLORS["background"])
        self.window.resizable(False, False)

        self.calculator = Calculator()
        self.all_value = ""
        self.value_text = StringVar()

        self.create_widgets()

    def create_widgets(self) -> None:
        # Display
        CTkLabel(
            self.window,
            textvariable=self.value_text,
            width=15,
            height=2,
            padx=7,
            anchor="e",
            justify="right",
            font=("Ivy", 30),
            text_color=COLORS["text"],
            bg_color=COLORS["background"]
        ).place(x=10, y=30)

        # Buttons
        buttons = [
            ("C", self.clear, 10, 170), ("(", lambda: self.enter_value("("), 85, 170),
            (")", lambda: self.enter_value(")"), 160, 170), ("÷", lambda: self.enter_value("÷"), 235, 170),
            ("7", lambda: self.enter_value("7"), 10, 225), ("8", lambda: self.enter_value("8"), 85, 225),
            ("9", lambda: self.enter_value("9"), 160, 225), ("x", lambda: self.enter_value("x"), 235, 225),
            ("4", lambda: self.enter_value("4"), 10, 280), ("5", lambda: self.enter_value("5"), 85, 280),
            ("6", lambda: self.enter_value("6"), 160, 280), ("-", lambda: self.enter_value("-"), 235, 280),
            ("1", lambda: self.enter_value("1"), 10, 335), ("2", lambda: self.enter_value("2"), 85, 335),
            ("3", lambda: self.enter_value("3"), 160, 335), ("+", lambda: self.enter_value("+"), 235, 335),
            (".", lambda: self.enter_value("."), 10, 390), ("0", lambda: self.enter_value("0"), 85, 390),
            ("^", lambda: self.enter_value("^"), 160, 390), ("=", self.calculate, 235, 390),
        ]

        for text, command, x, y in buttons:
            CTkButton(
                master=self.window,
                text=text,
                command=command,
                width=70,
                height=50,
                corner_radius=5,
                font=("Ivy", 20),
                text_color=COLORS["button_text"],
                fg_color=COLORS["button"],
                hover_color=COLORS["button_hover"],
                border_color=COLORS["border"],
                border_width=2
            ).place(x=x, y=y)

    def enter_value(self, value: str) -> None:
        self.all_value += value
        self.value_text.set(self.all_value)

    def calculate(self) -> None:
        try:
            result = self.calculator.calculate(self.all_value)
            self.value_text.set(result)
        except Exception as e:
            self.value_text.set(str(e))

    def clear(self) -> None:
        self.all_value = ""
        self.value_text.set("")

    def run(self) -> None:
        self.window.mainloop()
