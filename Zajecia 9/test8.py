import Tkinter as tk
import thFont as tkF

root = tk.TK()


def showMsgBx(ent):
    tkMB.showinfo("Wywolanie", ent.get())


def_fnt = tkF.namefont("TkDeafultFont")
def_fnt.configure(size=24)
root.option_add("*Font", def_fnt)


ts=tk.Text(root, height=10, width=50)
sb=tk.ScrollBar(root)

sb.config(command=ta.yview)

ta.config(yscrollcommand=sc.set)

ta.pack(side=tk.LEFT, fill=tk.Y)
sb.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()