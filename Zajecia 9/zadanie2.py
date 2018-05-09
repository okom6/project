import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB
import time
root = tk.Tk()

def showMsgBx():
    tkMB.showinfo("Wywolanie", "KONIEC")


def_fnt=tkF.nametofont("TkDefaultFont")
def_fnt.configure(size=20)
root.option_add("*Font", def_fnt)

def licznik():
    t = 10
    while(t>0):
        time.sleep(1)
        t=t-1
        lb.config(text=t)
        print(t)
    showMsgBx()

lb = tk.Label(root)

bt1=tk.Button(root, text="start", fg="blue", command=licznik)
bt1.grid(row=0, column=0)

lb.pack()
bt1.pack()


root.mainloop()