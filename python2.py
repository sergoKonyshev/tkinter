from tkinter import*
root=Tk()
root.geometry('500x500')
fr=Frame()
fr.pack(pady=5)
canv=Canvas(root,width=500,height=500)
canv.pack()
canv.create_oval(30,30,200,200,fill='green')
canv.create_oval(45,45,100,100,fill='orange')
mainloop()
