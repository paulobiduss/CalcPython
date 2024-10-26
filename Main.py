import tkinter as tk

def press_button(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal_button():
        try:
            global expression
            result = str(eval(expression))
            equation.set(result)
            expression = result
        except:
            equation.set("Erro")
            expression = ""

def clear_button():
    global expression
    expression = ""
    equation.set("")

window = tk.Tk()
window.title("Calculadora")

expression = ""

equation = tk.StringVar()

display = tk.Entry(window, textvariable=equation, font=('Arial', 18), justify='right')
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

buttons = [
      ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
      ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
      ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
      ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, font=('Arial', 18), command = equal_button)
    else:
        button = tk.Button(window, text=text, font=('Arial', 18), command=lambda t=text: press_button(t))

    button.grid(row=row, column=col, ipadx=10, ipady=10, sticky="nsew")

clear = tk.Button(window, text='C', font=('Arial', 18), command=clear_button)
clear.grid(row=4, column=0, columnspan=2, ipadx=10, ipady=10, sticky="nsew")

for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
