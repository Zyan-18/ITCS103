import tkinter as tk

window = tk.Tk()

window.title("SANCHEZ HO EXAM")
window.geometry("600x300")
window.resizable(True,True)
window.configure(bg="white", cursor="heart")

def reg():
    popup = tk.Toplevel()
    popup.title("Registration")
    popup.geometry("400x300")
    popup.resizable(True,True)
    popup.configure(bg="blue", cursor="heart")

    def reg_get():
        label33.get()
        label55.get()

    label11= tk.Label(popup, text="Register Now!",
        font=("Arial", 20),
        fg="white",
        bg="blue",
        anchor="center")
    label11.place(x=10, y=30)

    label22 = tk.Label(popup, text="Username:",
        font=("Arial", 20),
        fg="black",
        bg="blue",
        anchor="center")
    label22.place(x=0, y=80)

    label33 = tk.Entry(popup,
        width=40)
    label33.place(x=150, y=90)

    label44 = tk.Label(popup, text="Password:",
        font=("Arial", 20),
        fg="black",
        bg="blue",
        anchor="center")
    label44.place(x=0, y=130)

    label55 = tk.Entry(popup,
        width=40,
        show="*")
    label55.place(x=150, y=140)

    btn = tk.Checkbutton(popup, text="See Password",
        font=("Arial", 15))
    btn.place(x=180, y=180)

    label66 = tk.Button(popup, text="Register",
        font=("Arial", 15),
        fg="black",
        bg="white",
        anchor="center",
        width=30)
    label66.place(x=30, y=240)
    
def log():
    popup = tk.Toplevel()
    popup.title("Log In")
    popup.geometry("400x300")
    popup.resizable(True,True)
    popup.configure(bg="red", cursor="heart")

    def reg_get():
        label333.get()
        label555.get()

    label111= tk.Label(popup, text="Log In Now!",
        font=("Arial", 20),
        fg="black",
        bg="red",
        anchor="center")
    label111.place(x=180, y=30)

    label222 = tk.Label(popup, text="Username:",
        font=("Arial", 20),
        fg="black",
        bg="red",
        anchor="center")
    label222.place(x=0, y=80)

    label333 = tk.Entry(popup,
        width=40)
    label333.place(x=150, y=90)

    label444 = tk.Label(popup, text="Password:",
        font=("Arial", 20),
        fg="black",
        bg="red",
        anchor="center")
    label444.place(x=0, y=130)

    label555 = tk.Entry(popup,
        width=40,
        show="*")
    label555.place(x=150, y=140)

    btn1 = tk.Checkbutton(popup, text="See Password",
        font=("Arial", 15))
    btn1.place(x=180, y=180)

    label666 = tk.Button(popup, text="Register",
        font=("Arial", 15),
        fg="white",
        bg="green",
        anchor="center",
        width=30)
    label666.place(x=30, y=240)



label1 = tk.Label(window, text="Welcome!",
     font=("Arial", 30),
     fg="black",
     bg="white",
     anchor="center")
label1.place(x=220, y=30)

label2 = tk.Button(window, text="Register",
     font=("Arial", 20),
     fg="black",
     bg="blue",
     anchor="center",
     width=38,
     command=reg)
label2.place(x=0, y=100)

label3 = tk.Button(window, text="Log In",
     font=("Arial", 20),
     fg="black",
     bg="green",
     anchor="center",
     width=38,
     command=log)
label3.place(x=0, y=200)



window.mainloop()