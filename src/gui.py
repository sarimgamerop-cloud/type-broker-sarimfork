from PIL import Image
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# importing from Local Files 

from ocr_fetch import fetch


def guilayout(background_image_path=None):
    '''
    The whole tkinter GUI of the program 
    '''
    # imports inside of function because circular imports problem xD
    from main import types , clean_paragraph , start , solve_captcha
    # main gui code:
    root = tk.Tk()
    root.title("Type-Broker (EarlyDevelopment)")
    root.geometry("500x350")
    root.resizable(False, False) 

    # =========================
    # Background Setup
    # =========================
    if background_image_path:
        bg_image = Image.open(background_image_path)
        bg_image = bg_image.resize((500, 350), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # =========================
    # Style Setup for Modern Buttons
    # =========================
    style = ttk.Style(root)
    style.configure(
        "TButton",
        font=("Helvetica", 12, "bold"),
        foreground="white",
        background="#4CAF50",  # Modern green
        padding=10,
    )
    style.map("TButton", background=[("active", "#45a049")])  # Hover effect

    # =========================
    # Container Frame (for centering buttons)
    # =========================
    frame = tk.Frame(root, bg="", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Center frame in window

    # Start typing button
    start_typing = ttk.Button(
        frame,
        text="Start Typing",
        state=tk.DISABLED,
        command=lambda: types(clean_paragraph),
    )
    start_typing.grid(row=0, column=0, pady=10, sticky="ew")

    # Fetch button
    fetch_btn = ttk.Button(frame, text="Fetch", command=lambda: start(start_typing))
    fetch_btn.grid(row=1, column=0, pady=10, sticky="ew")

    # Solve Captcha button
    solve_cp = ttk.Button(frame, text="Solve Captcha", command=lambda: solve_captcha())
    solve_cp.grid(row=2, column=0, pady=10, sticky="ew")

    # Make buttons expand to fill frame width
    frame.grid_columnconfigure(0, weight=1)

    root.mainloop()


guilayout()