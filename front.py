from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import random


win=Tk()
win.attributes('-fullscreen', True)
win["bg"]="black"

def cross():
    win.destroy()

def next():
    win1=Toplevel(win)
    win1.attributes('-fullscreen', True)
    win1["bg"]="black"

    def tictactoe():
        win2=Toplevel(win1)
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
                    messagebox.showinfo("Message","You win the game")
                    Reset()
            elif(t1.get()==t4.get()==t7.get()):
                if(t1.get()!=""):
                    messagebox.showinfo("Message","You win the game")
                    Reset()
            elif(t1.get()==t5.get()==t9.get()):
                if(t1.get()!=""):
                    messagebox.showinfo("Message","You win the game")
                    Reset()
            
            elif(t2.get()==t5.get()==t8.get()):
                if(t2.get()!=""):
                    messagebox.showinfo("Message","You win the game")
                    Reset()
            elif(t3.get()==t6.get()==t9.get()):
                if(t3.get()!=""):
                    messagebox.showinfo("Message","You win the game")
                    Reset()
            elif(t3.get()==t5.get()==t7.get()):
                if(t3.get()!=""):
                    messagebox.showinfo("Message","You win the game")
                    Reset()
            elif(t4.get()==t5.get()==t6.get()):
                if(t4.get()!=""):
                    messagebox.showinfo("Message","You win the game")
                    Reset()
            elif(t7.get()==t8.get()==t9.get()):
                if(t7.get()!=""):
                    messagebox.showinfo("Message","You win the game")
                    Reset()
            else:
                if(t1.get()!=""and t2.get()!=""and t3.get()!=""and t4.get()!="" and t5.get()!="" and t6.get()!=""and t7.get()!="" and t8.get()!="" and t9.get()!=""):
                    messagebox.showinfo("Message","You Lose the game")
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
    
    def numberpuzzle():
            win3=Toplevel(win1)
            win3.attributes('-fullscreen', True)
            win3["bg"]="black"

            bgimg = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\bg.jpg"))
            bglabel = Label(win3,image=bgimg,bg="black")
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
                    messagebox.showinfo(win3,f"You win")

                        
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
                win3.destroy()



            lb=Label(win3,text="Number Puzzle",font=("Bradley Hand ITC",50),background="black",foreground="white")
            lb.place(x=390,y=80)
            ls=[]
            var1=IntVar()
            tf1=Button(win3,bg="white",font=("Arial",30),textvariable=var1,background="black",state=DISABLED)
            tf1.place(x=400,y=200,height=100,width=100)
            var2=IntVar()
            tf2=Button(win3,bg="white",font=("Arial",30),textvariable=var2,background="black",state=DISABLED,)
            tf2.place(x=500,y=200,height=100,width=100)
            var3=IntVar()
            tf3=Button(win3,bg="white",font=("Arial",30),textvariable=var3,background="black",state=DISABLED)
            tf3.place(x=600,y=200,height=100,width=100)
            var4=IntVar()
            tf4=Button(win3,bg="white",font=("Arial",30),textvariable=var4,background="black",state=DISABLED)
            tf4.place(x=700,y=200,height=100,width=100)



            var5=IntVar()
            tf5=Button(win3,bg="white",font=("Arial",30),textvariable=var5,background="black",state=DISABLED)
            tf5.place(x=400,y=300,height=100,width=100)
            var6=IntVar()
            tf6=Button(win3,bg="white",font=("Arial",30),textvariable=var6,background="black",state=DISABLED)
            tf6.place(x=500,y=300,height=100,width=100)
            var7=IntVar()
            tf7=Button(win3,bg="white",font=("Arial",30),textvariable=var7,background="black",state=DISABLED)
            tf7.place(x=600,y=300,height=100,width=100)
            var8=IntVar()
            tf8=Button(win3,bg="white",font=("Arial",30),textvariable=var8,background="black",state=DISABLED)
            tf8.place(x=700,y=300,height=100,width=100)

            var9=IntVar()
            tf9=Button(win3,bg="white",font=("Arial",30),textvariable=var9,background="black",state=DISABLED)
            tf9.place(x=400,y=400,height=100,width=100)
            var10=IntVar()
            tf10=Button(win3,bg="white",font=("Arial",30),textvariable=var10,background="black",state=DISABLED,)
            tf10.place(x=500,y=400,height=100,width=100)
            var11=IntVar()
            tf11=Button(win3,bg="white",font=("Arial",30),textvariable=var11,background="black",state=DISABLED,)
            tf11.place(x=600,y=400,height=100,width=100)
            var12=IntVar()
            tf12=Button(win3,bg="white",font=("Arial",30),textvariable=var12,background="black",state=DISABLED,)
            tf12.place(x=700,y=400,height=100,width=100)

            var13=IntVar()
            tf13=Button(win3,bg="white",font=("Arial",30),textvariable=var13,background="black",state=DISABLED)
            tf13.place(x=400,y=500,height=100,width=100)
            var14=IntVar()
            tf14=Button(win3,bg="white",font=("Arial",30),textvariable=var14,background="black",state=DISABLED)
            tf14.place(x=500,y=500,height=100,width=100)
            var15=IntVar()
            tf15=Button(win3,bg="white",font=("Arial",30),textvariable=var15,background="black",state=DISABLED)
            tf15.place(x=600,y=500,height=100,width=100)
            var16=IntVar()
            tf16=Button(win3,bg="white",font=("Arial",30),textvariable=var16,background="black",state=DISABLED)
            tf16.place(x=700,y=500,height=100,width=100)

            ls=[[var1,var2,var3,var4],[var5,var6,var7,var8],[var9,var10,var11,var12],[var13,var14,var15,var16]]

            img2=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\reset1.jpg"))
            btreset=Button(win3,image=img2,bg="black",command=restart)
            btreset.place(x=1200,y=100)

            img3=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\cut.png"))
            btcross=Button(win3,image=img3,bg="black",command=cross)
            btcross.place(x=1200,y=30)



            win3.bind('<KeyPress>',key_press)


            win3.mainloop()


        

    def cross():
        win.destroy()
        
    bgimg = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\bg.jpg"))
    bglabel = Label(win1,image=bgimg,bg="black")
    bglabel.place(x=80, y=10)

    titleimg=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\wall-long-190421438.jpg"))
    titlelabel=Label(win1,image=titleimg,bg="black")
    titlelabel.place(x=220,y=20)

    bt1img=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\91PR2j5wL-L._AC_UF1000,1000_QL80_.jpg"))
    bttictactoe=Button(win1,image=bt1img,bg="black",command=tictactoe)
    bttictactoe.place(x=220,y=250)
    lb1=Button(win1,text="TIC TAC TOE",font=("Times New Roman",25),bg="black",disabledforeground="white",state=DISABLED)
    lb1.place(x=260,y=570)

    bt2img=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\images.jpg"))
    btnumber=Button(win1,image=bt2img,bg="black",command=numberpuzzle)
    btnumber.place(x=750,y=250)
    lb2=Button(win1,text="Number Puzzle",font=("Times New Roman",25),bg="black",disabledforeground="white",state=DISABLED)
    lb2.place(x=790,y=570)


    img3=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\cut.png"))
    btcross=Button(win1,image=img3,bg="black",command=cross)
    btcross.place(x=1200,y=30)

    win1.mainloop()



bgimg = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\1.jpg"))
bglabel = Label(win,image=bgimg,bg="black")
bglabel.place(x=80, y=10)

img1=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\cut.png"))
btcross=Button(win,image=img1,bg="black",command=cross)
btcross.place(x=1200,y=30)

img2=ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\python\\Graphics\\Game\\next2.jpg"))
btnext=Button(win,image=img2,bg="black",command=next)
btnext.place(x=1000,y=450)

lb1=Label(win,text="Welcome!!",font=("Bradley Hand ITC",50),foreground="white",background="black")
lb1.place(x=920,y=350)


win.mainloop()