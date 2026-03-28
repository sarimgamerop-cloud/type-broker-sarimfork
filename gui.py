import tkinter as tk
from tkinter import ttk
from main import types , fetch

# Fetch - (take screenshot, fetching text), type - (type the fetched text) , stop (emgergency stop) 
speed_value = 0.06 

root = tk.Tk()

root.title("The Title")
root.geometry("400x300")  # width x height

fetch = tk.Button(root, text="Fetch",bg="blue", fg="white",command=fetch)
fetch.grid()

value = tk.StringVar()
speed_value_entry = tk.Entry(root,textvariable=value)
speed_value_entry.grid()

speed_value = value.get()
print(speed_value)


start_typing = tk.Button(root, text="Start Typing",bg="blue", fg="white",command=types)
start_typing.grid()
root.mainloop()
