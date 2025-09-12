from tkinter import *
window=Tk()
window.geometry("300x500")
window.title("main window")

def topWindow():
    top_win=Toplevel()
    top_win.geometry("180x120")
    top_win.title("top window")

    l=Label(top_win,text="sub-window")
    l.pack()
    top_win.mainloop()

l2=Label(window,text="main-window")
button=Button(window,text="click for new window!", command=topWindow)
l2.pack()
button.pack()
window.mainloop()