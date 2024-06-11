from tkinter import *
from PIL import ImageTk,Image



win=Tk()
win.attributes('-fullscreen', True)
win["bg"]="black"


'''def game1():
    tictactoe.tictactoe()'''

def cross():
  win.destroy()
    
bgimg = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\bg.jpg"))
bglabel = Label(win,image=bgimg,bg="black")
bglabel.place(x=80, y=10)

titleimg=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\wall-long-190421438.jpg"))
titlelabel=Label(win,image=titleimg,bg="black")
titlelabel.place(x=220,y=20)

bt1img=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\91PR2j5wL-L._AC_UF1000,1000_QL80_.jpg"))
bttictactoe=Button(win,image=bt1img,bg="black")
bttictactoe.place(x=220,y=250)
lb1=Button(win,text="TIC TAC TOE",font=("Times New Roman",25),bg="black",disabledforeground="white",state=DISABLED)
lb1.place(x=260,y=570)

bt2img=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\images.jpg"))
btnumber=Button(win,image=bt2img,bg="black")
btnumber.place(x=750,y=250)
lb2=Button(win,text="Number Puzzle",font=("Times New Roman",25),bg="black",disabledforeground="white",state=DISABLED)
lb2.place(x=790,y=570)


img3=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\cut.png"))
btcross=Button(win,image=img3,bg="black",command=cross)
btcross.place(x=1200,y=30)

win.mainloop()