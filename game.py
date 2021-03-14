from tkinter import *
import tkinter as tk
import time
import random
import sys
import pymysql
db = pymysql.connect("localhost","root","q2we4rt6yu8io0p@Sql","business")
cursor=db.cursor()


global names
names=[]



# ----------------------------------------------------------------------------------------------------------------------------------------------------------- cultract office


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def passbook():
   passbk = Tk()
   passbk.title('PassBook')
   passbk.geometry('1000x800')
   canvas = Canvas(passbk,width=300,height=80)
   Label(passbk,text ="details are here",width="100", height ="2",bg ="chocolate3",font=("courier new",13)).pack()
   Label(text="",bg="tan").pack()
   canvas.pack()
    
   canvas.create_oval(10, 10, 80, 80,outline = "black", fill = "seaGreen3",width = 2)
    
   canvas.create_text(45,40,fill="red",text="a/c",font="calibri 30 bold")
   canvas.create_text(190,40,fill="black",font="calibri 20 bold",text="PassBook",)
   Label(passbk,text ="Amount On Players",width="100", height ="2",bg ="chocolate3",font=("courier new",13)).pack()
   Label(text="",bg="tan").pack()
   qry_name = f"select name from player"
   cursor.execute(qry_name)
   name = cursor.fetchall()
   n=[]
   for i in name:
       i =str(i)
       i = i.replace("(","")
       i = i.replace(")","")
       i = i.replace(",","")
       i = i.replace("'","")
       n.append(i)
  
   print(n) 
   qry_Money = f"select Money from player"
   cursor.execute(qry_Money)
   money = cursor.fetchall()
   m=[]
   
   for j in money:
       j =str(j)
       j = j.replace("(","")
       j = j.replace(")","")
       j = j.replace(",","")
       j = j.replace("'","")
       j = int(j)
       m.append(j)
   print(m)
   Label(passbk,text=f"{n[0]} : Rs.{m[0]}",bg='tan').pack()
   Label(passbk,text=f"{n[1]} : Rs.{m[1]}",bg='tan').pack()
   Label(passbk,text=f"{n[2]} : Rs.{m[2]}",bg='tan').pack()

   Label(text="",bg="tan").pack()
   Label(passbk,text ="Property Details: ",width="100", height ="2",bg ="chocolate3",font=("courier new",13)).pack()
   Label(text="",bg="tan").pack()


def check(place,idd):
    qry1 = f"select name from Property{idd+1}"
    cursor.execute(qry1)
    prop = cursor.fetchall()
    place = f"('{place}',)"

    for i in prop:
        i = str(i)
        if i==place:
            return idd
            

def rent(player,place):
    pass


def trans(place,idd):
        global transact
        transact = Tk()
        transact.title('Transaction')
        transact.geometry('400x400')

        
        chk = check(place,idd)
        def rent1():
            rent(names[chk],place)
        if chk==idd:
            
            Label(transact,text=f'you already own : {place} ',bg='tan').pack()
            Button(transact,text="continue",command=passbook).pack()
        elif chk!=idd and chk<3:
            Label(transact,text=f'this : {place} is owned by {names[idd]}',bg='tan').pack()
            Button(transact,text="continue",command=rent1).pack()



        else:
            Label(transact,text=f'confirm the name of city / business : {place}',bg='tan').pack()
            Label(transact,text=' Want to buy this place?',bg='tan').pack()
            def pay():
                qr=f"select max(id) from property1"
                cursor.execute(qr)
            
                i = cursor.fetchone()
                
                i = str(i)
                i = i.replace("(","")
                i = i.replace(")","")
                i = i.replace(",","")
                print(i)
                if i=='None':
                    i=0
                else:
                    i=int(i)
                print(i)
                qry= f"insert into property1 values({i+1},'{place}')"
                cursor.execute(qry)
                qry2 = f"select Price from article where name='{place}'"
                cursor.execute(qry2)
                price = cursor.fetchone()
                qry3 = f"select Money from player where id=1"
                
                
                
                cursor.execute(qry3)
                Money = cursor.fetchone()
                money = str(Money)
                money = money.replace("(","")
                money = money.replace(")","")
                money = money.replace(",","")
                money=int(money)
                price = str(price)
                price = price.replace("(","")
                price = price.replace(")","")
                price = price.replace(",","")
                price=int(price)
                print(money-price)
                if ((money-price)<0):
                    Label(transact,text=' Insufficient balance in your a/c',bg='tan').pack()
                else:
                    money=money-price
                    qry4 = f"update player set Money={money} where id=1"
                    cursor.execute(qry4)

        
                
                    db.commit()

                    Label(transact,text=' transaction Sucessful',bg='tan').pack()
                Button(transact,text="Continue",command=passbook).pack()

            def abort():
                Label(transact,text=' transaction Aborted',bg='tan').pack()
                Button(transact,text="Continue",command=passbook).pack()

            Button(transact,text='Pay Now',command=pay).pack()
            Button(transact,text="Abort",command=abort).pack()

        
        
        
                
        

def play():
    global playscr
    playscr = Tk()

    playscr.title(names[0])
    playscr.geometry('500x500')
    d= random.randint(1,27)
    def trans1():
        trans(place,0)
    query=f"select name from article where id={d}"
    
    cursor.execute(query)
    place=cursor.fetchone()
    place =str(place)
    place = place.replace("(","")
    place = place.replace(")","")
    place = place.replace(",","")
    place = place.replace("'","")
    db.commit()
    text1 = Label(playscr,text=f"{names[0]} you got {d}",bg='chocolate3')
    text1.grid(row=0,padx=10,pady=10)
    text2 = Label(playscr,text=f"you are at {place}",bg='chocolate3')
    text2.grid(row=1,padx=5,pady=10)
    button1 = Button(playscr,text='Make Transaction',command=trans1)
    button1.grid(row=2,padx=10,pady=10)
    button2 = Button(playscr,text='skip and see passbook',command=passbook)
    button2.grid(row=3,padx=10,pady=10)


#     playscr.mainloop()

def insert():
    
    reset()
    names.clear()
    names.append(name_verify1.get())
    names.append(name_verify2.get())
    names.append(name_verify3.get())    
    for i in range(3):
        query= f"insert into player values({i+1},'{names[i]}',25000,'Propert{i+1}')"
        cursor.execute(query)
    db.commit()
    start()

def start():
    global start1
    start1 = Tk()
    start1.title('Start')
    start1.geometry('500x500')
    start1.configure(bg='tan')
    
    Label(start1,text=f"welcome {names[0]} , {names[1]} and {names[2]}").pack()
    
    
    Button(start1,text=f"Start and roll dice for {names[0]}",bg="tan2",width="30",height="1",command=play).pack()
    
def continueG():
    query =f"select name from player"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        i = str(i)
        i = i.replace("(","")
        i = i.replace(")","")
        i = i.replace(",","")
        i = i.replace("'","")
        i = i.replace("","")
        names.append(i)
    start()


def reset():
    for i in range(3):
        q1=f"delete from player where id={i+1}"
        cursor.execute(q1)
    q2="drop table Property1"
    cursor.execute(q2)
    q2_1="create table Property1(id int(2) primary key,name varchar(20));"
    cursor.execute(q2_1)
    q3="drop table Property2"
    cursor.execute(q3)
    q3_1="create table Property2(id int(2) primary key,name varchar(20));"
    cursor.execute(q3_1)
    q4="drop table Property3"
    cursor.execute(q4)
    q4_1="create table Property3(id int(2) primary key,name varchar(20));"
    cursor.execute(q4_1)
    db.commit()
def main_screen():
    global screen
    screen = Tk()
    img= PhotoImage(file="D:\A_NKIT\ytd\ppp.png.png")
    IMG= img.subsample(4)
    screen.configure(bg ="tan")
    # screen.configure(bg="tan1")    
    screen.geometry("500x500")
    screen.title("Business")
    canvas = Canvas(screen,width=300,height=80)
    
    Label(text ="welcome to the Game",width="100", height ="2",bg ="chocolate3",font=("courier new",13)).pack()
    Label(text="",bg="tan").pack()
    canvas.pack()
    
    canvas.create_oval(10, 10, 80, 80,outline = "black", fill = "seaGreen3",width = 2)
    
    canvas.create_text(45,40,fill="red",text="$$",font="calibri 30 bold")
    canvas.create_text(190,40,fill="black",font="calibri 20 bold",text="Business",)

    Label(text="",bg="tan").pack()
    # Button(text="Login",bg="tan2",height ="2",width="20",command = login,compound=LEFT).pack()
    Label(text ="",bg="tan").pack()
    global name_entry1
    global name_verify1
    name_verify1 = StringVar()
    global name_entry2
    global name_verify2
    name_verify2 = StringVar()
    global name_entry3
    global name_verify3
    name_verify3 = StringVar()
    Button(screen,text="Continue game",bg="tan2",width="20",height="1",command=continueG).pack()
    
    Label(screen,text ="please enter the details below to Start").pack()
    Label(screen,text ="player 1*").pack()
    name_entry1=Entry(screen,textvariable=name_verify1,bg="tan2")
    name_entry1.pack()
    Label(text ="",bg="tan").pack()
    Label(screen,text ="player 2*").pack()
    name_entry2=Entry(screen,textvariable=name_verify2,bg="tan2")
    name_entry2.pack()
    Label(text ="",bg="tan").pack()
    Label(screen,text ="player 3*").pack()
    name_entry3=Entry(screen,textvariable=name_verify3,bg="tan2")
    name_entry3.pack()
    Label(text ="",bg="tan").pack()
    
  

    Button(screen,text="Start",bg="tan2",width="20",height="1",command=insert).pack()
    
   
    screen.mainloop()



main_screen()
