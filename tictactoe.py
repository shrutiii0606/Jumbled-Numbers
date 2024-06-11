from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

win2=Tk()
win2.attributes('-fullscreen', True)
win2["bg"]="black"

bgimg = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\bg.jpg"))
bglabel = Label(win2,image=bgimg,bg="black")
bglabel.place(x=80, y=10)

def Reset():
    bt1["state"]=NORMAL
    bt2["state"]=NORMAL
    bt3["state"]=NORMAL
    bt4["state"]=NORMAL
    bt5["state"]=NORMAL
    bt6["state"]=NORMAL
    bt7["state"]=NORMAL
    bt8["state"]=NORMAL
    bt9["state"]=NORMAL

    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")
    t6.set("")
    t7.set("")
    t8.set("")
    t9.set("")

def cross():
  win2.destroy()

var=IntVar()
var.set(0)
def game(textvariable,bt):
  if(var.get()==0):
   textvariable.set("X")
   var.set(1)
   bt["state"]=DISABLED
   
   
  else:
    textvariable.set("O")
    var.set(0)
    bt["state"]=DISABLED
   


  if(t1.get()==t2.get()==t3.get()):
     if(t1.get()!=""):
      messagebox.showin2fo("Message","You win2 the game")
      Reset()
  elif(t1.get()==t4.get()==t7.get()):
      if(t1.get()!=""):
       messagebox.showin2fo("Message","You win2 the game")
       Reset()
  elif(t1.get()==t5.get()==t9.get()):
     if(t1.get()!=""):
      messagebox.showin2fo("Message","You win2 the game")
      Reset()
  
  elif(t2.get()==t5.get()==t8.get()):
    if(t2.get()!=""):
     messagebox.showin2fo("Message","You win2 the game")
     Reset()
  elif(t3.get()==t6.get()==t9.get()):
    if(t3.get()!=""):
     messagebox.showin2fo("Message","You win2 the game")
     Reset()
  elif(t3.get()==t5.get()==t7.get()):
    if(t3.get()!=""):
     messagebox.showin2fo("Message","You win2 the game")
     Reset()
  elif(t4.get()==t5.get()==t6.get()):
    if(t4.get()!=""):
     messagebox.showin2fo("Message","You win2 the game")
     Reset()
  elif(t7.get()==t8.get()==t9.get()):
    if(t7.get()!=""):
     messagebox.showin2fo("Message","You win2 the game")
     Reset()
  else:
    if(t1.get()!=""and t2.get()!=""and t3.get()!=""and t4.get()!="" and t5.get()!="" and t6.get()!=""and t7.get()!="" and t8.get()!="" and t9.get()!=""):
     messagebox.showin2fo("Message","You Lose the game")
     Reset()
    


img1=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\Screenshot 2023-10-14 234255.png"))
lb1=Label(win2,image=img1,bg="black")
lb1.place(x=440,y=50)


t1=StringVar()


bt1=Button(win2,font=("Algerian",40),textvariable=t1,bg="black",command=lambda:game(t1,bt1))
bt1.place(x=440,y=220,height=120,width=120)


t2=StringVar()
bt2=Button(win2,font=("Algerian",40),textvariable=t2,bg="black",command=lambda:game(t2,bt2))
bt2.place(x=560,y=220,height=120,width=120)


t3=StringVar()
bt3=Button(win2,font=("Algerian",40),textvariable=t3,bg="black",command=lambda:game(t3,bt3))
bt3.place(x=680,y=220,height=120,width=120)

t4=StringVar()
bt4=Button(win2,font=("Algerian",40),textvariable=t4,bg="black",command=lambda:game(t4,bt4))
bt4.place(x=440,y=340,height=120,width=120)

t5=StringVar()
bt5=Button(win2,font=("Algerian",40),textvariable=t5,bg="black",command=lambda:game(t5,bt5))
bt5.place(x=560,y=340,height=120,width=120)

t6=StringVar()
bt6=Button(win2,font=("Algerian",40),textvariable=t6,bg="black",command=lambda:game(t6,bt6))
bt6.place(x=680,y=340,height=120,width=120)

t7=StringVar()
bt7=Button(win2,font=("Algerian",40),textvariable=t7,bg="black",command=lambda:game(t7,bt7))
bt7.place(x=440,y=460,height=120,width=120)

t8=StringVar()
bt8=Button(win2,font=("Algerian",40),textvariable=t8,bg="black",command=lambda:game(t8,bt8))
bt8.place(x=560,y=460,height=120,width=120)

t9=StringVar()
bt9=Button(win2,font=("Algerian",40),textvariable=t9,bg="black",command=lambda:game(t9,bt9))
bt9.place(x=680,y=460,height=120,width=120)

img2=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\reset1.jpg"))
btreset=Button(win2,image=img2,bg="black",command=Reset)
btreset.place(x=1200,y=100)

img3=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\cut.png"))
btcross=Button(win2,image=img3,bg="black",command=cross)
btcross.place(x=1200,y=30)

win2.mainloop()
