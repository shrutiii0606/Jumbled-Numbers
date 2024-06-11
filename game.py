from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk,Image

win=Tk()
win.attributes('-fullscreen', True)
win["bg"]="black"

bgimg = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\bg.jpg"))
bglabel = Label(win,image=bgimg,bg="black")
bglabel.place(x=80, y=10)



randomlist = []
def key_press(e):
   value=1
   i=0
   while(i<4):
       j=0
       while(j<4):
           if(ls[i][j].get()==value%16):
               value+=1
           j+=1
       i+=1

   if(value==17):
       messagebox.showinfo(win,f"You win{value}")

           
   var=IntVar()
   i=0
   while(i<4):
        j=0
        while(j<4):
          if(ls[i][j].get()==0):
             a=i
             b=j    
          j+=1
        i+=1
   if(e.keysym=='Down'):
        ls[a][b].set(ls[(a+1)%4][b].get())
        ls[(a+1)%4][b].set(0)      
   elif(e.keysym=='Up'):
        ls[a][b].set(ls[(a-1)%4][b].get())
        ls[(a-1)%4][b].set(0) 
        
   elif(e.keysym=='Left'):
       ls[a][b].set(ls[a][(b-1)%4].get())
       ls[a][(b-1)%4].set(0) 
   elif(e.keysym=='Right'):
        ls[a][b].set(ls[a][(b+1)%4].get())
        ls[a][(b+1)%4].set(0) 
       
    
def restart():
    randomlist.clear()
    randomlist.extend(random.sample(range(0, 16), 16))
    var1.set(randomlist[0])
    var2.set(randomlist[1])
    var3.set(randomlist[2])
    var4.set(randomlist[3])
    var5.set(randomlist[4])
    var6.set(randomlist[5])
    var7.set(randomlist[6])
    var8.set(randomlist[7])
    var9.set(randomlist[8])
    var10.set(randomlist[9])
    var11.set(randomlist[10])
    var12.set(randomlist[11])
    var13.set(randomlist[12])
    var14.set(randomlist[13])
    var15.set(randomlist[14])
    var16.set(randomlist[15])

def cross():
  win.destroy()



lb=Label(win,text="Number Puzzle",font=("Bradley Hand ITC",50),background="black",foreground="white")
lb.place(x=390,y=80)
ls=[]
var1=IntVar()
tf1=Button(win,bg="white",font=("Arial",30),textvariable=var1,background="black",state=DISABLED)
tf1.place(x=400,y=200,height=100,width=100)
var2=IntVar()
tf2=Button(win,bg="white",font=("Arial",30),textvariable=var2,background="black",state=DISABLED,)
tf2.place(x=500,y=200,height=100,width=100)
var3=IntVar()
tf3=Button(win,bg="white",font=("Arial",30),textvariable=var3,background="black",state=DISABLED)
tf3.place(x=600,y=200,height=100,width=100)
var4=IntVar()
tf4=Button(win,bg="white",font=("Arial",30),textvariable=var4,background="black",state=DISABLED)
tf4.place(x=700,y=200,height=100,width=100)



var5=IntVar()
tf5=Button(win,bg="white",font=("Arial",30),textvariable=var5,background="black",state=DISABLED)
tf5.place(x=400,y=300,height=100,width=100)
var6=IntVar()
tf6=Button(win,bg="white",font=("Arial",30),textvariable=var6,background="black",state=DISABLED)
tf6.place(x=500,y=300,height=100,width=100)
var7=IntVar()
tf7=Button(win,bg="white",font=("Arial",30),textvariable=var7,background="black",state=DISABLED)
tf7.place(x=600,y=300,height=100,width=100)
var8=IntVar()
tf8=Button(win,bg="white",font=("Arial",30),textvariable=var8,background="black",state=DISABLED)
tf8.place(x=700,y=300,height=100,width=100)

var9=IntVar()
tf9=Button(win,bg="white",font=("Arial",30),textvariable=var9,background="black",state=DISABLED)
tf9.place(x=400,y=400,height=100,width=100)
var10=IntVar()
tf10=Button(win,bg="white",font=("Arial",30),textvariable=var10,background="black",state=DISABLED,)
tf10.place(x=500,y=400,height=100,width=100)
var11=IntVar()
tf11=Button(win,bg="white",font=("Arial",30),textvariable=var11,background="black",state=DISABLED,)
tf11.place(x=600,y=400,height=100,width=100)
var12=IntVar()
tf12=Button(win,bg="white",font=("Arial",30),textvariable=var12,background="black",state=DISABLED,)
tf12.place(x=700,y=400,height=100,width=100)

var13=IntVar()
tf13=Button(win,bg="white",font=("Arial",30),textvariable=var13,background="black",state=DISABLED)
tf13.place(x=400,y=500,height=100,width=100)
var14=IntVar()
tf14=Button(win,bg="white",font=("Arial",30),textvariable=var14,background="black",state=DISABLED)
tf14.place(x=500,y=500,height=100,width=100)
var15=IntVar()
tf15=Button(win,bg="white",font=("Arial",30),textvariable=var15,background="black",state=DISABLED)
tf15.place(x=600,y=500,height=100,width=100)
var16=IntVar()
tf16=Button(win,bg="white",font=("Arial",30),textvariable=var16,background="black",state=DISABLED)
tf16.place(x=700,y=500,height=100,width=100)

ls=[[var1,var2,var3,var4],[var5,var6,var7,var8],[var9,var10,var11,var12],[var13,var14,var15,var16]]

img2=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\reset1.jpg"))
btreset=Button(win,image=img2,bg="black",command=restart)
btreset.place(x=1200,y=100)

img3=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\cut.png"))
btcross=Button(win,image=img3,bg="black",command=cross)
btcross.place(x=1200,y=30)



win.bind('<KeyPress>',key_press)


win.mainloop()