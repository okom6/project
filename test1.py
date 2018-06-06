import logging

def main():
    logging.basicConfig(filrname='C:\Users\student\Desktop\Zajecia10\app.log', level=logging.INFO)
    logging.info("Start")
    logging.warning("Warn")
    logging.debug("A problem occurred")

if __name__ =="__main__":
    main()

    import Tkinter as tk
import tkFont as tkF

root = tk.Tk()
root.grid_propagate(False)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def potwierdz():
    ta.config(font=("TkDefaultFont", int(e1.get())))

def zapisz():
    f2 = open("plik1.txt", "w")
    f2.write(ta.get("1.0", "end-1c"))
    f2.close()

def wczytaj():
    f2 = open("plik1.txt", "r")
    ta.delete(1.0, "end-1c")
    ta.insert("end-1c", f2.read())
    f2.close()

def_fnt=tkF.nametofont("TkDefaultFont")
def_fnt.configure(size=24)
root.option_add("*Font", def_fnt)

sb=tk.Scrollbar(root)
ta=tk.Text(root, height=10, width=50, font=("TkDefaultFont", 30))

sb.pack(side=tk.RIGHT, fill=tk.Y)
ta.pack(side=tk.LEFT, fill=tk.Y)

sb.config(command=ta.yview)
ta.config(yscrollcommand=sb.set)

e1=tk.Entry(root)
e1.pack(side=tk.TOP, fill=tk.X)

bt1=tk.Button(root, text="potwierdz", command=potwierdz)
bt1.pack(side=tk.TOP, fill=tk.X)

bt2=tk.Button(root, text="zapisz", command=zapisz)
bt2.pack(side=tk.TOP, fill=tk.X)

bt3=tk.Button(root, text="wczytaj", command=wczytaj)
bt3.pack(side=tk.TOP, fill=tk.X)

root.mainloop()
