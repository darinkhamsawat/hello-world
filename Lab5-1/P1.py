""" 
Darin Khamsawat
683040489-2
P1
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login UI")
root.geometry("420x620")
root.configure(bg="#f5f5f5")

# ===== Main Card =====
main_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="solid",
    highlightbackground="#5dade2",
    highlightthickness=2
)
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=540)

# ===== Title =====
title_label = tk.Label(
    main_frame,
    text="LOGIN",
    font=("Arial", 16, "bold"),
    bg="white"
)
title_label.pack(anchor="w", padx=30, pady=(25, 20))

# ===== Email =====
tk.Label(main_frame, text="Email", bg="white").pack(anchor="w", padx=30)
email_entry = tk.Entry(main_frame, width=30, bd=1, relief="solid")
email_entry.pack(pady=8)

# ===== Password =====
tk.Label(main_frame, text="Password", bg="white").pack(anchor="w", padx=30)
password_entry = tk.Entry(main_frame, width=30, show="*", bd=1, relief="solid")
password_entry.pack(pady=8)

# ===== Remember Me =====
remember_var = tk.IntVar()
remember_check = tk.Checkbutton(
    main_frame,
    text="Remember me?",
    variable=remember_var,
    bg="white"
)
remember_check.pack(anchor="w", padx=30, pady=5)

# ===== Login Button =====
login_button = tk.Button(
    main_frame,
    text="LOGIN",
    bg="#e75480",
    fg="white",
    width=25,
    relief="flat",
    pady=6
)
login_button.pack(pady=15)

# ===== Forgot Password =====
forgot_label = tk.Label(
    main_frame,
    text="Forgot Password?",
    fg="gray",
    bg="white"
)
forgot_label.pack(anchor="e", padx=30)

# ===== OR Divider =====
divider_frame = tk.Frame(main_frame, bg="white")
divider_frame.pack(pady=15, fill="x", padx=30)

tk.Frame(divider_frame, bg="gray", height=1).pack(side="left", expand=True, fill="x", padx=5)
tk.Label(divider_frame, text="OR", bg="white").pack(side="left")
tk.Frame(divider_frame, bg="gray", height=1).pack(side="left", expand=True, fill="x", padx=5)

# ===== Social Buttons =====
social_frame = tk.Frame(main_frame, bg="white")
social_frame.pack(pady=10)

tk.Button(social_frame, text="G", width=3, relief="solid").grid(row=0, column=0, padx=10)
tk.Button(social_frame, text="f", width=3, relief="solid").grid(row=0, column=1, padx=10)
tk.Button(social_frame, text="in", width=3, relief="solid").grid(row=0, column=2, padx=10)

# ===== Sign Up =====
signup_frame = tk.Frame(main_frame, bg="white")
signup_frame.pack(pady=25)

tk.Label(signup_frame, text="Need an account? ", bg="white").pack(side="left")
tk.Label(signup_frame, text="SIGN UP", fg="#2e86c1", bg="white").pack(side="left")

root.mainloop()