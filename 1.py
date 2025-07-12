from tkinter import*
from tkinter import messagebox

w=Tk()
w.geometry("1000x1000")

def ok():
    e1=ent.get()
    messagebox.showinfo("ok",e1)


lab=Label(w,text="enter",font=("times",20))
lab.place(x=50,y=100)

ent=Entry(w,font=("times",20))
ent.place(x=150,y=100)

button=Button(w,text="click",font=("times",20),command=ok)
button.place(x=50,y=200)



w.mainloop()


