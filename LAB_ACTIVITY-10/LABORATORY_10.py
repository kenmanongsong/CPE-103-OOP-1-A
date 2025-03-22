import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import os

window = tk.Tk()
window.title('Birthdate Selection')
window.geometry('500x350')

try:
    icon_path = "instagram_ig_logo_icon_181500.ico"
    if os.path.exists(icon_path):
        window.iconbitmap(icon_path)
    else:
        print(f"Icon file not found at: {icon_path}")
except tk.TclError:
    print("Error: Invalid icon file.")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=2)


def show_birthdate():
    day = day_combobox.get()
    month = month_combobox.get()
    year = year_combobox.get()
    showinfo(
        title="Birthdate Information",
        message=f"Your birthdate is: {month} {day}, {year}")

try:
    bg_image = Image.open("2022_Acer_Consumer_Option_03_3840x2400.jpg")
    bg_image = bg_image.resize((500, 350))
    bg_photo = ImageTk.PhotoImage(bg_image)
except FileNotFoundError:
    print("Error: background.jpg not found. Using default background.")
    bg_photo = None

if bg_photo:
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    window.config(bg="lightgray")

title_label = ttk.Label(
    window,
    text="Select Your Birthdate",
    font=("Times New Roman", 16),
    anchor="center")
title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

day_label = ttk.Label(
    window,
    text="Day (DD):",
    font=("Times New Roman", 12))
day_label.grid(row=1, column=0)

day_values = [str(i) for i in range(1, 32)]
day_combobox = ttk.Combobox(
    window, width=50, values=day_values, state="readonly")
day_combobox.grid(row=1, column=1, padx=(0, 10))


month_label = ttk.Label(
    window,
    text="Month:",
    font=("Times New Roman", 12))
month_label.grid(row=2, column=0)

month_values = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"]
month_combobox = ttk.Combobox(
    window, width=50, values=month_values, state="readonly")
month_combobox.grid(row=2, column=1, padx=(0, 10))

year_label = ttk.Label(
    window,
    text="Year (YYYY):",
    font=("Times New Roman", 12))
year_label.grid(row=3, column=0)

year_values = [str(i) for i in range(1900, 2026)]
year_combobox = ttk.Combobox(
    window, width=50, values=year_values, state="readonly")
year_combobox.grid(row=3, column=1, padx=(0, 10))

show_button = ttk.Button(
    window, text="Show Birthdate", command=show_birthdate)
show_button.grid(row=4, column=0, columnspan=2, pady=(30, 40))

window.mainloop()