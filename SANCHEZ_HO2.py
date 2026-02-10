import tkinter as tk

window = tk.Tk()

window.title("hello my world")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg="pink", cursor="hand2")

label = tk.Label(window, text="Student Profile",
    font = ("times new roman", 35),
    fg = "brown",
    bg = "pink",
    anchor = "center")

label_1 = tk.Label(window, text="Name: Zyan Kloe S. Sanchez",
    font = ("arial", 18),
    fg = "brown",
    bg = "pink")

label_2 = tk.Label(window, text="Age: 19",
    font = ("arial", 18),
    fg = "brown",
    bg = "pink")

label_3 = tk.Label(window, text="Course and Section: BSIT-1A",
    font = ("arial", 18),
    fg = "brown",
    bg = "pink")

label_4 = tk.Label(window, text="Birthday: November 20, 2006",
    font = ("arial", 18),
    fg = "brown",
    bg = "pink")

label_5 = tk.Label(window, text="Motto: Treat yourself as kindly as you treat others.",
    font = ("arial", 18),
    fg = "brown",
    bg = "pink")

label.pack(padx=10, pady=50)
label_1.pack(padx=20, pady=6, anchor = "w")
label_2.pack(padx=20, pady=6, anchor = "w")
label_3.pack(padx=20, pady=6, anchor = "w")
label_4.pack(padx=20, pady=6, anchor = "w")
label_5.pack(padx=20, pady=6, anchor = "w")

window.mainloop()

