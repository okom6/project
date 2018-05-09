import Tkinter as tk
import thFont as tkF
import thMessageBox as tkMB

root = tk.TK()

def showMsgBx(ent):
    tkMB.showinfo("Wywolanie", ent.get())


def_fnt = tkF.namefont("TkDeafultFont")
def_fnt.configure(size=48)

root.option_add("*Font", def_fnt)

e1=tk.Entry(root)
e1.grid(row=0, column=0, columnspan=2, pady=40)

bt1=tk.Button(master, text="start", command=lambda: showMsgBx(e1))
bt1.grid(row=0, column=0, sticky=tk.W)

bt2=tk.Button(master, text="stop", command=root.quit)
bt2.grid(row=0, column=0, sticky=tk.E, pady=40)

root.mainloop()