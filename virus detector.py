from tkinter import *
window= Tk()
window.geometry("300x150")

def message():
    messagebox.showwarning("ALERT!", "stop virus found!")
button=Button(window,text="scan for virus", command=message)
button.place(x=40,y=80)
window.mainloop()