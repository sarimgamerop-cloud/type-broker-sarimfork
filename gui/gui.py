import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("The Title")
root.geometry("400x300")  # width x height

start_button = tk.Button(root, text="Start",bg="blue", fg="white")
start_button.pack()
# Run the app

root.mainloop()
