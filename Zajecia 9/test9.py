import Tkinter as tk

root = tk.Tk()

cnv=tk.Canvas(root, width=200, height=100)

cnv.pack()
cnv.create_rectlange(50,20,150,80, fill="blue")
cnv.create_rectlange(65,35,135,65, fill="yellow")
cnv.create_line(0,0,50,20, fill="red", width=3)


root.mainloop()