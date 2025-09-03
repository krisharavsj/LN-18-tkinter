import tkinter as tk

root = tk.Tk()
root.title("Multiplying")
root.geometry("300x150")

num1 = tk.Entry(root)
num2 = tk.Entry(root)
num1.grid(row=0, column=1, padx=10, pady=10)
num2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="First number:").grid(row=0, column=0)
tk.Label(root, text="Second number:").grid(row=1, column=0)

res = tk.StringVar()
tk.Label(root, textvariable=res).grid(row=3, column=0, columnspan=2)

def do_mul():
    try:
        a = float(num1.get())
        b = float(num2.get())
        res.set("Result = " + str(a * b))
    except:
        res.set("Oops, not a number!")

tk.Button(root, text="answer", command=do_mul).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
