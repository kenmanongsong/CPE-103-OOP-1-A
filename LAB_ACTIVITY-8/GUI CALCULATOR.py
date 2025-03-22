import tkinter as tk
from tkinter import messagebox

history = []
history_window = None

def validate_input(value):
    try:
        return float(value)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return None

def update_history(operation, num1, num2, result_value):
    entry = f"{num1} {operation} {num2} = {result_value}"
    history.append(entry)
    if history_window:
        refresh_history_display()

def refresh_history_display():
    if history_window:
        for widget in history_frame.winfo_children():
            widget.destroy()

        for entry in history:
            label = tk.Label(history_frame, text=entry, font=("Arial", 10), fg="white", bg="black", anchor="w", width=40)
            label.pack(anchor="w", pady=2)

        history_canvas.update_idletasks()
        history_canvas.yview_moveto(1)

def add():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        result_value = num1 + num2
        result.set(result_value)
        update_history("+", num1, num2, result_value)

def subtract():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        result_value = num1 - num2
        result.set(result_value)
        update_history("-", num1, num2, result_value)

def multiply():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        result_value = num1 * num2
        result.set(result_value)
        update_history("*", num1, num2, result_value)

def divide():
    num1 = validate_input(entry1.get())
    num2 = validate_input(entry2.get())
    if num1 is not None and num2 is not None:
        if num2 == 0:
            result.set("Error! Division by zero.")
            update_history("/", num1, num2, "Error!")
        else:
            result_value = num1 / num2
            result.set(result_value)
            update_history("/", num1, num2, result_value)

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

def clear_history():
    history.clear()
    refresh_history_display()

def open_history():
    global history_window, history_canvas, history_frame

    if history_window and tk.Toplevel.winfo_exists(history_window):  # Prevent multiple windows
        history_window.lift()
        return

    history_window = tk.Toplevel(root)
    history_window.title("History")
    history_window.geometry("400x300")
    history_window.configure(bg="black")

    history_canvas = tk.Canvas(history_window, bg="black", height=250)
    history_scrollbar = tk.Scrollbar(history_window, orient="vertical", command=history_canvas.yview)
    history_frame = tk.Frame(history_canvas, bg="black")

    history_window_label = tk.Label(history_window, text="Calculation History", font=("Arial", 12, "bold"), fg="white", bg="black")
    history_window_label.pack(pady=5)

    history_window_button = tk.Button(history_window, text="Clear History", command=clear_history, font=("Arial", 10))
    history_window_button.pack(pady=5)

    history_canvas.create_window((0, 0), window=history_frame, anchor="nw")
    history_canvas.configure(yscrollcommand=history_scrollbar.set)

    history_canvas.pack(side="left", fill="both", expand=True)
    history_scrollbar.pack(side="right", fill="y")

    def update_scroll_region(event):
        history_canvas.configure(scrollregion=history_canvas.bbox("all"))

    history_frame.bind("<Configure>", update_scroll_region)

    refresh_history_display()

root = tk.Tk()
root.title("Calculator with History")
root.geometry("400x350")
root.configure(bg="black")

result = tk.StringVar()

entry_bg = "#333333"
entry_fg = "white"

tk.Label(root, text="Enter first number:", font=("Arial", 12, "bold"), fg="white", bg="black").pack()
entry1 = tk.Entry(root, font=("Arial", 12), width=20, bg=entry_bg, fg=entry_fg)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", font=("Arial", 12, "bold"), fg="white", bg="black").pack()
entry2 = tk.Entry(root, font=("Arial", 12), width=20, bg=entry_bg, fg=entry_fg)
entry2.pack(pady=5)

button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add", command=add, width=10, font=("Arial", 10)).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Subtract", command=subtract, width=10, font=("Arial", 10)).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Multiply", command=multiply, width=10, font=("Arial", 10)).grid(row=1, column=0, padx=5)
tk.Button(button_frame, text="Divide", command=divide, width=10, font=("Arial", 10)).grid(row=1, column=1, padx=5)

tk.Label(root, text="Result:", font=("Arial", 12, "bold"), fg="white", bg="black").pack(pady=5)
tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="cyan", bg="black").pack()

tk.Button(root, text="View History", command=open_history, width=22, font=("Arial", 10)).pack(pady=5)

tk.Button(root, text="Clear", command=clear, width=22, font=("Arial", 10)).pack(pady=5)

root.bind('<Return>', lambda event: add())

root.mainloop()