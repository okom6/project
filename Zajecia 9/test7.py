import Tkinter as tk
import thFont as tkF
import thMessageBox as tkMB

root = tk.TK()


def showMsgBx(ent):
    tkMB.showinfo("Wywolanie", ent.get())


def_fnt = tkF.namefont("TkDeafultFont")
def_fnt.configure(size=24)
root.option_add("*Font", def_fnt)


def rbVarTest(var):
    print(var.get())

v1=tk.IntVar()
v2=tk.IntVar()

rb1=tk.RadioButton(root, text="1", variable=v1, value=1, command=lambda: rbVarTest(v1))
rb2=tk.RadioButton(root, text="2", variable=v1, value=2, command=lambda: rbVarTest(v1))


rb3=tk.RadioButton(root, text="3", variable=v2, value=3, command=lambda: rbVarTest(v2))
rb4=tk.RadioButton(root, text="4", variable=v2, value=4, command=lambda: rbVarTest(v2))

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()

root.mainloop()