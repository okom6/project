import Tkinter as tk
import thFont as tkF
root=tk.TK()

#def_fnt=tkF.

def labelConfig(lab, txt):
    lab.config(text=txt, fg="light green", bg="dark green")
    
lb=tk.Label(root, text="Hello world!")
lb.pack()

labelConfig(lb, "123")

root.mainloop()