from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number', bg = '#64884e', font=("Arial", 14), bd=3)
        self.lbl2=Label(win, text='Second number', bg = '#64884e', font=("Arial", 14), bd=3)
        self.lbl3=Label(win, text='Result', bg = '#64884e', font=("Arial", 14), bd=3)

        self.t1=Entry(win, font=("Arial", 14), bd=3)
        self.t2=Entry(win, font=("Arial", 14), bd=3)
        self.t3=Entry(win, font=("Arial", 14), bd=3)
        self.t4=Entry(win, font=("Arial", 14), bd=3)

        self.btn1 = Button(win, text='Add', fg = 'black', bg = '#ecb0b0')
        self.btn2 = Button(win, text='Subtract', fg = 'black', bg = '#ecb0b0')
        self.btn3 = Button(win, text='Multiply', fg = 'black', bg = '#ecb0b0')
        self.btn4 = Button(win, text='Divide', fg = 'black', bg = '#ecb0b0')
        self.btn5 = Button(win, text='Clear', fg = 'black', bg = '#ecb0b0')

        self.lbl1.place(x=50, y=50)
        self.t1.place(x=200, y=50)

        self.lbl2.place(x=50, y=100)
        self.t2.place(x=200, y=100)

        self.lbl3.place(x=10, y=100)
        self.t3.place(x=200, y=100)

        self.b1=Button(win, text='Add', command=self.add, fg = 'black', bg = '#ecb0b0',font= ("Arial", 14), bd=3)
        self.b2=Button(win, text='Subtract', command=self.subtract, fg = 'black', bg = '#ecb0b0', font= ("Arial", 14), bd=3)
        self.b3= Button(win, text='Multiply',command=self.multiply, fg = 'black', bg = '#ecb0b0', font= ("Arial", 14), bd=3)
        self.b4 = Button(win, text='Divide',command=self.divide, fg = 'black', bg = '#ecb0b0', font= ("Arial", 14), bd=3)
        self.b5 = Button(win, text='Clear',command=self.clear, fg = 'black', bg = '#d11d1d', font= ("Arial", 14), bd=3)

        self.b3.bind('<Button-1>', lambda event: self.multiply())
        self.b4.bind('<Button-1>', lambda event: self.divide())
        self.b5.bind('<Button-1>', lambda event: self.clear())

        self.b1.place(x=90, y=150)
        self.b2.place(x=160, y=150)
        self.b3.place(x=260, y=150)
        self.b4.place(x=360, y=150)
        self.b5.place(x=200, y=250)

        self.lbl3.place(x=100, y=200)

        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        num1 = float(self.t1.get())
        num2 = float(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def subtract(self):
        self.t3.delete(0, 'end')
        num1 = float(self.t1.get())
        num2 = float(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def multiply (self):
        self.t3.delete(0, 'end')
        num1 = float(self.t1.get())
        num2 = float(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def divide (self):
        self.t3.delete(0, 'end')
        num1 = float(self.t1.get())
        num2 = float(self.t2.get())
        result = num1/num2
        self.t3.insert(END, str(result))

    def clear (self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0 ,'end')
window=Tk()
mywin=MyWindow(window)
window.title('SIGMA CALCULATOR')
window.geometry("500x330+20+20")
window.configure(bg = '#64884e')
window.mainloop()

