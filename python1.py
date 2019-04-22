from tkinter import*
root=Tk()
root.geometry('500x500')
fr=Frame()
fr.pack(pady=5)
canv=Canvas(root,width=500,height=500)
canv.pack()
canv.create_oval(30,30,200,200,fill='green')

mainloop()
