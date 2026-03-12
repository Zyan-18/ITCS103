import tkinter as tk

window = tk.Tk()

window.title("Simple Calculator")
window.config(bg="pink")


frame=tk.Frame(window, bg="white")
frame.grid(row=0, column=0, columnspan=3)


label = tk.Label(frame, text="Welcome!", bg="white",
    fg="Black", font=("Arial", 12, "bold"))
label.grid(padx=100, pady=15) 


label1=tk.Label(window, text="Enter 1st Number:",
    bg="light gray", fg="Black", font=("Arial", 11, "bold"))
label1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


entry1=tk.Entry(window)
entry1.grid(row=1, column=2)
value = entry1.get()


label2=tk.Label(window, text="Enter 2nd Number:",
    bg="light gray", fg="Black", font=("Arial", 11, "bold"))
label2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


entry2=tk.Entry(window)
entry2.grid(row=2, column=2)
value = entry2.get()


def on_enter(event):
    event.widget['bg'] = "pink2"

def on_leave(event):
    event.widget['bg'] = "light gray"


# ADDITION
def add():
    no_1 = int(entry1.get())
    no_2 = int(entry2.get())

    a = int((no_1 + no_2))
    label['text'] = f"The sum of {no_1} + {no_2} is {a}."

addition = tk.Button(window, text="Add", command=add)
addition.grid(row=3, column=0, columnspan=2, pady=8)
addition.bind("<Enter>", on_enter)
addition.bind("<Leave>", on_leave)

# SUBTRACTION
def sub():
    no_1 = int(entry1.get())
    no_2 = int(entry2.get())

    b = int((no_1 - no_2))
    label['text'] = f"The difference of {no_1} - {no_2} is {b}."

subtraction = tk.Button(window, text="Subtract", command=sub)
subtraction.grid(row=3, column=2, columnspan=2, pady=8)
subtraction.bind("<Enter>", on_enter)
subtraction.bind("<Leave>", on_leave)


# MULTIPLICATION
def multiply():
    no_1 = int(entry1.get())
    no_2 = int(entry2.get())

    c = int((no_1 * no_2))
    label['text'] = f"The product of {no_1} x {no_2} is {c}."

multiplication = tk.Button(window, text="Multiply", command=multiply)
multiplication.grid(row=4, column=0, columnspan=2, pady=8)
multiplication.bind("<Enter>", on_enter)
multiplication.bind("<Leave>", on_leave)


# DIVISION
def divide():
    no_1 = int(entry1.get())
    no_2 = int(entry2.get())

    d = int((no_1 / no_2))
    label['text'] = f"The qoutient of {no_1} / {no_2} is {d}."

division = tk.Button(window, text="Divide", command=divide)
division.grid(row=4, column=2, columnspan=2, pady=8)
division.bind("<Enter>", on_enter)
division.bind("<Leave>", on_leave)

window.mainloop()