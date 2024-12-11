import tkinter as tk
from tkinter import messagebox
import operations

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")

        # Поля для ввода значений
        self.left_value = tk.Entry(root, width=20, font=('Arial', 14))
        self.left_value.grid(row=0, column=0, padx=5, pady=5)

        self.right_value = tk.Entry(root, width=20, font=('Arial', 14))
        self.right_value.grid(row=0, column=1, padx=5, pady=5)

        # Кнопки операций
        buttons = [
            ("+", self.add),
            ("-", self.subtract),
            ("*", self.multiply),
            ("/", self.divide),
            ("%", self.modulus),
            ("sin", self.sin),
            ("cos", self.cos),
            ("x^y", self.power),
            ("\u221a", self.square_root),
            ("floor", self.floor),
            ("ceil", self.ceil),
        ]

        for i, (text, command) in enumerate(buttons):
            row, col = divmod(i, 3)
            button = tk.Button(root, text=text, width=10, height=2, command=command)
            button.grid(row=row + 1, column=col, padx=5, pady=5)

    def get_values(self):
        try:
            left = float(self.left_value.get()) if self.left_value.get() else 0
            right = float(self.right_value.get()) if self.right_value.get() else 0
            return left, right
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа.")
            return None, None

    def display_result(self, result):
        self.left_value.delete(0, tk.END)
        self.left_value.insert(0, str(result))
        self.right_value.delete(0, tk.END)

    # Операции
    def add(self):
        left, right = self.get_values()
        if left is not None:
            self.display_result(operations.add(left, right))

    def subtract(self):
        left, right = self.get_values()
        if left is not None:
            self.display_result(operations.subtract(left, right))

    def multiply(self):
        left, right = self.get_values()
        if left is not None:
            self.display_result(operations.multiply(left, right))

    def divide(self):
        left, right = self.get_values()
        if left is not None:
            try:
                self.display_result(operations.divide(left, right))
            except ValueError as e:
                messagebox.showerror("Ошибка", str(e))

    def modulus(self):
        left, right = self.get_values()
        if left is not None:
            self.display_result(operations.modulus(left, right))

    def power(self):
        left, right = self.get_values()
        if left is not None:
            self.display_result(operations.power(left, right))

    def square_root(self):
        left, _ = self.get_values()
        if left is not None:
            try:
                self.display_result(operations.square_root(left))
            except ValueError as e:
                messagebox.showerror("Ошибка", str(e))

    def sin(self):
        left, _ = self.get_values()
        if left is not None:
            self.display_result(operations.sin(left))

    def cos(self):
        left, _ = self.get_values()
        if left is not None:
            self.display_result(operations.cos(left))

    def floor(self):
        left, _ = self.get_values()
        if left is not None:
            self.display_result(operations.floor(left))

    def ceil(self):
        left, _ = self.get_values()
        if left is not None:
            self.display_result(operations.ceil(left))

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
