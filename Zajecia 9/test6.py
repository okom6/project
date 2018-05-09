import Tkinter as tk
import thFont as tkF
import thMessageBox as tkMB

root = tk.TK()

def showMsgBx(ent):
    tkMB.showinfo("Wywolanie", ent.get())


def_fnt = tkF.namefont("TkDeafultFont")
def_fnt.configure(size=48)

root.option_add("*Font", def_fnt)

def valueTest(vtest):
    print(vtest.get())
    
var1=tk.BoleanVar()
var2=tk.BoleanVar()

cb1=tk.Checkbutton(root, text="Op1", command=valueTest, variable=var1)
cb1.grid(row=0, column=0)
cb2=tk.Checkbutton(root, text="Op2", command=valueTest, variable=var2)
cb2.grid(row=0, column=2)

root.mainloop()