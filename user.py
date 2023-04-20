from tkinter import *
import datetime
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)




a = datetime.datetime.now()

class user:
    alloweduser = 0
    user_list = []
    user_age = []
    a =  "users.txt"
    f = open(a,"w")


    def __init__(self,gotname,gotlastname,gotage,gotcode,gotphone):
        self.name = gotname
        self.lastname = gotlastname
        self._age = gotage
        self.code = gotcode
        self.phone = gotphone
        user.alloweduser +=1
        user.user_list.append([gotname,gotlastname])
        user.user_age.append(gotage)
    

    def __repr__(self):
        return f"{self.name} {self.lastname} by NCode: {self.code} by age {self._age}"


    def left(self):
        user.alloweduser -=1
        user.user_list.remove([self.name,self.lastname])
        user.user_age.remove(self._age)
        print(F"{self.name} had left!")
    
    def file(self):
        dic = {}
        dic["name"] = self.name
        dic["last name"] = self.lastname
        dic["age"] = self._age
        dic["phone"] = self.phone
        dic["national code"] = self.code
        dic["date"] = a.date()
        dic["time"] = a.time()
        note = f"{self.name}_{self.lastname} =" + str(dic) +"\n"
        user.f.write(note)

window=Tk()

window.geometry("450x450")
window.title("Sign in")

# Make a frame
frame1=Frame(window,bg="orange")
frame1.pack(expand=True,fill=BOTH)


frame2=Frame(window,bg="lavender")
frame2.pack(expand=True,fill=BOTH)

sogn=Label(frame1,text="Sing in",font=("",16),bg="orange")
sogn.place(x=200,y=3)


entryText_1 = StringVar()
entry_1 = Entry( frame1, textvariable=entryText_1)
entryText_1.set("Name")
entry_1.place(x=16,y=40)

entryText_2 = StringVar()
entry_2 = Entry( frame1, textvariable=entryText_2)
entryText_2.set("Last Name")
entry_2.place(x=210,y=40)

entryText_3 = StringVar()
entry_3 = Spinbox( frame1, textvariable=entryText_3,from_=1,to=100)
entryText_3.set("Age")
entry_3.place(x=16,y=100)

entryText_4 = StringVar()
entry_4 = Entry( frame1, textvariable=entryText_4)
entryText_4.set("Phone Number")
entry_4.place(x=210,y=100)

entryText_5 = StringVar()
entry_5 = Entry( frame1, textvariable=entryText_5)
entryText_5.set("National Code")
entry_5.place(x=16,y=150)

lbl = Label(frame2, font=('calibri', 12, 'bold'),foreground='black',bg="lavender")
lbl.place(x=360,y=195)
time()

def save(user_n = 0):
    user_n +=1
    name_user = "usre_" +str(user_n)
    name_user = user(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get())
    print(name_user)
    allowed_number.config(text=f"Online users: {user.alloweduser}")
    name_user.file()


btn3=Button(frame1,text="Save",bg="pink",command=save,font=("",20))
btn3.place(x=220,y=150)


allowed_number = Label(frame2,text=f"Online users: {0}",bg="lavender",fg="black", font=('calibri', 12, 'bold'))
allowed_number.place(x=3,y=195)
menubar = Menu(window)
filemenu= Menu(menubar,tearoff=0)
menubar.add_command(label="Save",command=save)
menubar.add_command(label="Exit",command=exit)

window.config(menu=menubar)

window.mainloop()
    