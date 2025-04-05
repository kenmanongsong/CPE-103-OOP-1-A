import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.config(bg="gray")

        self.equation = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.equation, borderwidth=5, font=('Arial', 16), justify='right', bg="white", fg="black")
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

        buttons_data = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '+'),
            ('C',),('=',),
        ]

        self.buttons = {}
        row_val = 1
        for row_index, row_buttons in enumerate(buttons_data):
            col_val = 0
            for col_index, button_text in enumerate(row_buttons):
                button = tk.Button(master, text=button_text, padx=20, pady=20, font=('Arial', 14),
                                    command=lambda text=button_text: self.click(text),
                                    bg="gray", fg="white", activebackground="dim gray", activeforeground="white")
                button.grid(row=row_val, column=col_val, padx=1, pady=1, sticky="nsew")
                self.buttons[button_text] = button
                col_val += 1
            row_val += 1

        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        for i in range(len(buttons_data) + 1):
            master.grid_rowconfigure(i, weight=1)

        self.buttons['7'].grid(row=2, column=0, sticky="nsew")
        self.buttons['4'].grid(row=3, column=0, sticky="nsew")
        self.buttons['1'].grid(row=4, column=0, sticky="nsew")
        self.buttons['0'].grid(row=5, column=0, sticky="nsew")
        self.buttons['.'].grid(row=4, column=3, sticky="nsew")
        self.buttons['='].grid(row=5, column=1, columnspan=4, sticky="nsew")
        self.buttons['C'].grid(row=2, column=3, sticky="nsew")
        self.buttons['8'].grid(row=2, column=1, sticky="nsew")
        self.buttons['5'].grid(row=3, column=1, sticky="nsew")
        self.buttons['2'].grid(row=4, column=1, sticky="nsew")
        self.buttons['9'].grid(row=2, column=2, sticky="nsew")
        self.buttons['6'].grid(row=3, column=2, sticky="nsew")
        self.buttons['3'].grid(row=4, column=2, sticky="nsew")
        self.buttons['/'].grid(row=4, column=4, sticky="nsew")
        self.buttons['*'].grid(row=3, column=3, sticky="nsew")
        self.buttons['-'].grid(row=2, column=4, sticky="nsew")
        self.buttons['+'].grid(row=3, column=4, sticky="nsew")

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.equation.get())
                self.equation.set(result)
            except Exception as e:
                self.equation.set("Error")
        elif key == 'C':
            self.equation.set("")
        else:
            self.equation.set(self.equation.get() + key)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()