from tkinter import*
from random import randrange as rnd,choice

colors=['yellow','green','black','blue','magenta']

x=0
y=0
r=0
points=0
miss=0

def new_ball():
                global x, y, r, res
                canv.delete(ALL)
                x=rnd(100,700)
                y=rnd(100,500)
                r=rnd(30,50)
                res=canv.create_text(60,20,text=str(points)+'/'+str(miss),font='arrial 20')
                canv.create_oval(x-r,y-r,x+r,y+r,fill=choice(colors), width=0)
                root.after(1000,new_ball)

def click(event):
                                global points,miss,res
                                if abs(x-event.x)< r and abs(y-event.y)< r:
                                                points+=1
                                                canv.delete(ALL)
                                                res=canv.create_text(60,20,text=str(points)+'/'+str(miss),font='arrial 20')

                                else: 
                                                     miss +=1
                                                     canv.delete(ALL)

                                                     res=canv.create_text(60,20,text=str(points)+'/'+str(miss))
root=Tk()

root.geometry('800x550')
root.title('catch ball')
canv=Canvas(root,width=800,height=550,bg='lightblue')
canv.pack()

root.config(cursor='cross_reverse')
root.after(1000,new_ball)
canv_bind('<Button-1>',click)

mainloop()



                                     







                                     
