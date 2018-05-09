import Tkinter as tk
import tkFont as tkF
import tkMessageBox as tkMB
root = tk.Tk()

def showMsgBx():
    tkMB.showinfo("Wywolanie", "Komunikat")


def_fnt=tkF.nametofont("TkDefaultFont")
def_fnt.configure(size=20)
root.option_add("*Font", def_fnt)


def rbVarTest(var):
    global x
    if(var.get()==1):
        bt1.config(fg="blue")
    if(var.get()==2):
        bt1.config(fg="green")
    if(var.get()==3):
        bt1.config(fg="red")

v1=tk.IntVar()

rb1=tk.Radiobutton(root, text="1", variable=v1, value=1, command=lambda: rbVarTest(v1))
rb2=tk.Radiobutton(root, text="2", variable=v1, value=2, command=lambda: rbVarTest(v1))
rb3=tk.Radiobutton(root, text="3", variable=v1, value=3, command=lambda: rbVarTest(v1))

bt1=tk.Button(root, text="start", fg="blue", command=showMsgBx)
bt1.grid(row=0, column=0)

rb1.pack()
rb2.pack()
rb3.pack()
bt1.pack()


root.mainloop()