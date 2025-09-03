from tkinter import *
window= Tk()
window.geometry("300x150")

frame= Frame(master=window,height=800,width=500,bg="#d0efff")
digits=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]
for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame=Frame(master=window,relief=SUNKEN,borderwidth=1)
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=digits[i][j],bg="#d0efff")
        label.pack(padx=3,pady=3)
window.mainloop()