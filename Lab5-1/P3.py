""" 
Darin Khamsawat
683040489-2
P3
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("450x650")
root.configure(bg="white")

# ===== Main Frame =====
main_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=380, height=600)

# ===== Title =====
title_label = tk.Label(
    main_frame,
    text="Adult and Child BMI Calculator",
    font=("Arial", 14, "bold"),
    bg="#a0522d",
    fg="white",
    pady=8
)
title_label.pack(fill="x")

# ===== Age Category =====
age_frame = tk.Frame(main_frame, bg="white")
age_frame.pack(pady=15)

tk.Label(age_frame, text="Calculate BMI for", bg="white").grid(row=0, column=0, padx=5)

age_combo = ttk.Combobox(
    age_frame,
    values=["Adult Age 20+", "Child / Teen 2-19"],
    state="readonly",
    width=18
)
age_combo.current(0)
age_combo.grid(row=0, column=1)

# ===== Weight Section =====
weight_frame = tk.Frame(main_frame, bg="white")
weight_frame.pack(pady=10)

tk.Label(weight_frame, text="Weight:", bg="white").grid(row=0, column=0, padx=5)

weight_entry = tk.Entry(weight_frame, width=10)
weight_entry.grid(row=0, column=1, padx=5)

weight_unit = ttk.Combobox(
    weight_frame,
    values=["kg", "pounds"],
    state="readonly",
    width=10
)
weight_unit.current(0)
weight_unit.grid(row=0, column=2)

# ===== Height Section =====
height_frame = tk.Frame(main_frame, bg="white")
height_frame.pack(pady=10)

tk.Label(height_frame, text="Height:", bg="white").grid(row=0, column=0, padx=5)

height_entry1 = tk.Entry(height_frame, width=10)
height_entry1.grid(row=0, column=1, padx=5)

height_unit = ttk.Combobox(
    height_frame,
    values=["cm", "meters", "feet"],
    state="readonly",
    width=10
)
height_unit.current(0)
height_unit.grid(row=0, column=2)

# Optional inches box (for feet)
height_entry2 = tk.Entry(height_frame, width=10)
height_entry2.grid(row=1, column=1, pady=5)

tk.Label(height_frame, text="(inches if feet selected)", bg="white").grid(row=1, column=2)

# ===== Buttons =====
button_frame = tk.Frame(main_frame, bg="white")
button_frame.pack(pady=20)

clear_btn = tk.Button(button_frame, text="Clear", width=12)
clear_btn.grid(row=0, column=0, padx=20)

calculate_btn = tk.Button(button_frame, text="Calculate", width=12)
calculate_btn.grid(row=0, column=1, padx=20)

# ===== Answer Section =====
answer_frame = tk.LabelFrame(main_frame, text="Answer:", bg="white", width=320, height=250)
answer_frame.pack(pady=10)
answer_frame.pack_propagate(False)

bmi_label = tk.Label(answer_frame, text="BMI =", font=("Arial", 12), bg="white")
bmi_label.pack(pady=10)

adult_bmi_label = tk.Label(answer_frame, text="Adult BMI", font=("Arial", 11, "bold"), bg="white")
adult_bmi_label.pack()

# ===== BMI Table =====
table_frame = tk.Frame(answer_frame, bg="white")
table_frame.pack(pady=10)

# Headers
tk.Label(table_frame, text="BMI", width=12, relief="solid").grid(row=0, column=0)
tk.Label(table_frame, text="Status", width=15, relief="solid").grid(row=0, column=1)

# Rows
rows = [
    ("≤ 18.4", "Underweight"),
    ("18.5 - 24.9", "Normal"),
    ("25.0 - 39.9", "Overweight"),
    ("≥ 40.0", "Obese"),
]

for i, (bmi, status) in enumerate(rows):
    tk.Label(table_frame, text=bmi, width=12, relief="solid").grid(row=i+1, column=0)
    tk.Label(table_frame, text=status, width=15, relief="solid").grid(row=i+1, column=1)

root.mainloop()