from tkinter import *
import random
from tkinter import messagebox

win=Tk()
win.maxsize(500,500)
win.minsize(500,500)
win.title("GAME")
win["bg"]="Black"

frame1=Frame(win)
frame1.pack()

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


def start():
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

ls=[]
var1=IntVar()
tf1=Entry(win,bg="white",font=("Arial",30),textvariable=var1,state=DISABLED,disabledforeground="black")
tf1.place(x=100,y=80,height=70,width=70)
var2=IntVar()
tf2=Entry(win,bg="white",font=("Arial",30),textvariable=var2,state=DISABLED,disabledforeground="black")
tf2.place(x=170,y=80,height=70,width=70)
var3=IntVar()
tf3=Entry(win,bg="white",font=("Arial",30),textvariable=var3,state=DISABLED,disabledforeground="black")
tf3.place(x=240,y=80,height=70,width=70)
var4=IntVar()
tf4=Entry(win,bg="white",font=("Arial",30),textvariable=var4,state=DISABLED,disabledforeground="black")
tf4.place(x=310,y=80,height=70,width=70)



var5=IntVar()
tf5=Entry(win,bg="white",font=("Arial",30),textvariable=var5,state=DISABLED,disabledforeground="black")
tf5.place(x=100,y=150,height=70,width=70)
var6=IntVar()
tf6=Entry(win,bg="white",font=("Arial",30),textvariable=var6,state=DISABLED,disabledforeground="black")
tf6.place(x=170,y=150,height=70,width=70)
var7=IntVar()
tf7=Entry(win,bg="white",font=("Arial",30),textvariable=var7,state=DISABLED,disabledforeground="black")
tf7.place(x=240,y=150,height=70,width=70)
var8=IntVar()
tf8=Entry(win,bg="white",font=("Arial",30),textvariable=var8,state=DISABLED,disabledforeground="black")
tf8.place(x=310,y=150,height=70,width=70)

var9=IntVar()
tf9=Entry(win,bg="white",font=("Arial",30),textvariable=var9,state=DISABLED,disabledforeground="black")
tf9.place(x=100,y=220,height=70,width=70)
var10=IntVar()
tf10=Entry(win,bg="white",font=("Arial",30),textvariable=var10,state=DISABLED,disabledforeground="black")
tf10.place(x=170,y=220,height=70,width=70)
var11=IntVar()
tf11=Entry(win,bg="white",font=("Arial",30),textvariable=var11,state=DISABLED,disabledforeground="black")
tf11.place(x=240,y=220,height=70,width=70)
var12=IntVar()
tf12=Entry(win,bg="white",font=("Arial",30),textvariable=var12,state=DISABLED,disabledforeground="black")
tf12.place(x=310,y=220,height=70,width=70)

var13=IntVar()
tf13=Entry(win,bg="white",font=("Arial",30),textvariable=var13,state=DISABLED,disabledforeground="black")
tf13.place(x=100,y=290,height=70,width=70)
var14=IntVar()
tf14=Entry(win,bg="white",font=("Arial",30),textvariable=var14,state=DISABLED,disabledforeground="black")
tf14.place(x=170,y=290,height=70,width=70)
var15=IntVar()
tf15=Entry(win,bg="white",font=("Arial",30),textvariable=var15,state=DISABLED,disabledforeground="black")
tf15.place(x=240,y=290,height=70,width=70)
var16=IntVar()
tf16=Entry(win,bg="white",font=("Arial",30),textvariable=var16,state=DISABLED,disabledforeground="black")
tf16.place(x=310,y=290,height=70,width=70)

ls=[[var1,var2,var3,var4],[var5,var6,var7,var8],[var9,var10,var11,var12],[var13,var14,var15,var16]]

btstart=Button(win,text="START",bg="white",command=start)
btstart.place(x=200,y=400)

btrestart=Button(win,text="RESTART",bg="white",command=restart)
btrestart.place(x=200,y=450)



win.bind('<KeyPress>',key_press)


win.mainloop()