from tkinter import *

# Window
window = Tk()
window.title("Fahrenheit and Celsius Converter")
window.minsize(300, 100)
window.config(padx=50, pady=50)


# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)


# Label
fahrenheit = Label(text="Fahrenheit")
fahrenheit.config(padx=0, pady=10)
fahrenheit.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.config(padx=0, pady=10)
is_equal_to.grid(column=0, row=1)

celsius = Label(text="0")
celsius.config(padx=0, pady=10)
celsius.grid(column=1, row=1)

cs = Label(text="Celsius")
cs.config(padx=0, pady=10)
cs.grid(column=2, row=1)


def calculate():
    f = float(entry.get())
    c = (f - 32) * 5 / 9
    celsius.config(text=round(c, 4))


# Button
button = Button(text="Converter", command=calculate)
button.config(padx=10, pady=10)
button.grid(column=1, row=2)


window.mainloop()
