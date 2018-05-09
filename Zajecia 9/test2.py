import Tkinter as tk
import thFont as tkF

root = tk.TK()


def_fnt=tkF.namefont("TkDeafultFont")
 
def_fnt.configure(size=48)
 
root.option_add("*Font", def_fnt)
 
lb1=tk.Label(root, text="L1". bg="red")
lb2 = tk.Label(root, text="L2".bg = "greeb")
lb3 = tk.Label(root, text="L3".bg = "blue")


lb = tk.Label(root, text="Hello world!")
lb.pack()

root.mainloop()