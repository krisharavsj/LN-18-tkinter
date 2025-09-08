from tkinter import *
window= Tk()
window.geometry("300x150")

def handle_keypress(event):
    print(event.char)
window.bind("<h>",handle_keypress)

def handle_click(event):
    print("the button is clicked")
button=Button(text="click me!")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()