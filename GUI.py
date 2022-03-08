from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("1000x500")
Str1=StringVar()
Str2=StringVar()
label1=Label(window,text="Username",font=("ariel",12))
label2=Label(window,text="Password",font=("ariel",12))
t1=Entry(bd=10)
##t1.insert(1,'Enter Username:- ')
t2=Entry(bd=10)
##t2.insert(1,'Enter Password:- ')
def callback():
    txt1=t1.get()
    txt2=t2.get()
    print(txt1,txt2)
    if txt1==txt2:
        messagebox.showerror("Error","Username and Password can't be same")
    elif(txt1=={} and txt2==""8):
        messagebox.showinfo("no","noo")
    else:
         messagebox.showinfo("Valid","Successfully Submitted")
b=Button(window,text="Submit",bg="green",font=("ariel",12),command=callback)
label1.place(x=300,y=10)
t1.place(x=300,y=40)
label2.place(x=300,y=90)
t2.place(x=300,y=120)
b.place(x=325,y=180)
mainloop()
