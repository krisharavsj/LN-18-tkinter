from tkinter import *
window= Tk()
window.geometry("300x150")

frame= Frame(master=window,height=800,width=500,bg="#d0efff")
lb1=Label(frame,text="full name",bg="#3895D3",fg='white',width=12)
lb2=Label(frame,text="e-mail ID",bg="#3895D3",fg='white',width=12)
lb3=Label(frame,text="enter password",bg="#3895D3",fg='white',width=12)
name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame)

def display():
    name=name_entry.get()
    greet="hey!"+name
    message="\n congratulations for your new account"
    textbox.insert(END,greet)
    textbox.insert(END,message)