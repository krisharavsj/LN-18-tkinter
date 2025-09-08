import tkinter as tk
from datetime import date

def calc_age():
    d, m, y = int(day.get()), int(month.get()), int(year.get())
    t = date.today()
    age = t.year - y - ((t.month, t.day) < (m, d))
    result.config(text=f"Age: {age}")

window = tk.Tk()
window.title("Age Calculator")

tk.Label(window, text="Day").pack()
day = tk.Entry(window)
day.pack()

tk.Label(window, text="Month").pack()
month = tk.Entry(window)
month.pack()

tk.Label(window, text="Year").pack()
year = tk.Entry(window)
year.pack()

tk.Button(window, text="Calculate", command=calc_age).pack()
result = tk.Label(window, text="")
result.pack()

window.mainloop()
