from tkinter import *
from tkinter import StringVar


class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.scvalue = StringVar()
        self.wm_iconbitmap("2.ico")

        self.geometry("400x600")

    def entry(self):
        self.scvalue = StringVar()
        self.scvalue.set("")
        self.screen = Entry(self, textvar=self.scvalue, font="lucida 25 bold")
        self.screen.pack(fill=X, padx=10, pady=10)

    def button(self):
        i = 1
        while (i <= 7):
            f = Frame(self, bg="grey")
            b = Button(f, text=str(int(10 - i)), padx=15, pady=2, font="lucida 30 bold")
            b.pack(side=LEFT, padx=15, pady=5)
            b.bind("<Button-1>", self.click)

            b = Button(f, text=str(int(9 - i)), padx=15, pady=2, font="lucida 30 bold")
            b.pack(side=LEFT, padx=15, pady=5)
            b.bind("<Button-1>", self.click)

            b = Button(f, text=str(int(8 - i)), padx=15, pady=2, font="lucida 30 bold")
            b.pack(side=LEFT, padx=15, pady=5)
            b.bind("<Button-1>", self.click)
            f.pack()
            i = i + 3

        f = Frame(self, bg="grey")
        b = Button(f, text="-", padx=25, pady=10, font="lucida 20 bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        b = Button(f, text="0", padx=25, pady=10, font="lucida 20 bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        b = Button(f, text="*", padx=25, pady=10, font="lucida 20 bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        f.pack()

        f = Frame(self, bg="grey")
        b = Button(f, text="/", padx=23, pady=10, font="lucida 20 bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        b = Button(f, text="%", padx=23, pady=10, font="lucida 20  bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        b = Button(f, text="=", padx=23, pady=10, font="lucida 20 bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        f.pack()

        f = Frame(self, bg="grey")
        b = Button(f, text="C", padx=24, pady=15, font="lucida 20 bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        b = Button(f, text=".", padx=24, pady=15, font="lucida 20 bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        b = Button(f, text="+", padx=24, pady=15, font="lucida 20 bold")
        b.pack(side=LEFT, padx=15, pady=5)
        b.bind("<Button-1>", self.click)

        f.pack()

    def click(self, event):

        text = event.widget.cget("text")
        if text == "=":
            if self.scvalue.get().isdigit():
                value = int(self.scvalue.get())
            else:
                try:
                    value = eval(self.screen.get())

                except Exception as e:
                    print(e)
                    value = "Error"
            self.scvalue.set(value)
            self.screen.update()
        elif text == "C":
            self.scvalue.set("")
            self.screen.update()

        else:
            self.scvalue.set(self.scvalue.get() + text)
            self.screen.update()


if __name__ == '__main__':
    window = GUI()

    window.entry()
    window.button()
    window.mainloop()
