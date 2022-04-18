import tkinter as tk

calculation_string = ''


def add_to_calculation(symbol):
    global calculation_string
    calculation_string += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation_string)


def evaluate_calculation():
    pass


def clear_field():
    pass


root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)

root.mainloop()