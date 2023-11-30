from tkinter import *

class Calculator:
    def __init__(self, master):
        self.expression = ""
        self.equation_var = StringVar()
        self.create_gui(master)

    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation_var.set(self.expression)

    def equal_press(self):
        try:
            total = str(eval(self.expression))
            self.equation_var.set(total)
            self.expression = ""
        except:
            self.equation_var.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation_var.set("")

    def create_gui(self, master):
        master.configure(background="#f0f0f0")
        master.title("Simple Calculator")
        master.geometry("300x400")

        expression_field = Entry(master, textvariable=self.equation_var, font=('Arial', 18), bd=10, relief=SUNKEN)
        expression_field.grid(row=0, column=0, columnspan=4, pady=10, ipadx=10, ipady=10, sticky='nsew')

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = Button(master, text=button, fg='white', bg='#4CAF50', command=self.equal_press, height=2, width=5, font=('Arial', 14), bd=5)
            elif button == 'Clear':
                btn = Button(master, text=button, fg='white', bg='#FF8C00', command=self.clear, height=2, width=5, font=('Arial', 14), bd=5)
            else:
                btn = Button(master, text=button, fg='white', bg='#FF4500', command=lambda b=button: self.press(b), height=2, width=5, font=('Arial', 14), bd=5)

            btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure row and column weights to make buttons and entry field expandable
        for i in range(1, 6):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
