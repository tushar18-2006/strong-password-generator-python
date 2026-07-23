import tkinter as tk
from tkinter import messagebox
import random
import string

# ----------------------------
# Strong Password Generator
# ----------------------------

PASSWORD_LENGTH = 16

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"

def generate_password():
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Input Required", "Please enter your name.")
        return

    # Clean the name (letters only)
    cleaned_name = "".join(c for c in name if c.isalpha())

    if len(cleaned_name) < 2:
        messagebox.showwarning(
            "Invalid Name",
            "Please enter at least 2 alphabetic characters."
        )
        return

    # Use first and last letter of the name
    base = [
        cleaned_name[0].upper(),
        cleaned_name[-1].lower()
    ]

    # Character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits

    # Ensure password has at least one of each category
    password = base + [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(SYMBOLS),
    ]

    all_characters = uppercase + lowercase + digits + SYMBOLS

    while len(password) < PASSWORD_LENGTH:
        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)

    password_var.set(final_password)


def copy_password():
    password = password_var.get()

    if not password:
        messagebox.showinfo("Nothing to Copy", "Generate a password first.")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo("Copied", "Password copied to clipboard!")


# ----------------------------
# GUI
# ----------------------------

root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("550x320")
root.resizable(False, False)
root.configure(bg="#F4F6F8")

title = tk.Label(
    root,
    text="Strong Password Generator",
    font=("Arial", 18, "bold"),
    bg="#F4F6F8",
    fg="#1F2937"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="#F4F6F8")
frame.pack(pady=10)

name_label = tk.Label(
    frame,
    text="Enter Your Name:",
    font=("Arial", 11),
    bg="#F4F6F8"
)
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

name_entry = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)
name_entry.grid(row=0, column=1, padx=5)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 11, "bold"),
    bg="#0F62FE",
    fg="white",
    width=20,
    command=generate_password
)
generate_btn.pack(pady=15)

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 14),
    width=35,
    justify="center",
    state="readonly",
    readonlybackground="white"
)
password_entry.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 11, "bold"),
    bg="#16A34A",
    fg="white",
    width=20,
    command=copy_password
)
copy_btn.pack(pady=10)

info = tk.Label(
    root,
    text="Generated password contains uppercase, lowercase, numbers and symbols.",
    font=("Arial", 9),
    bg="#F4F6F8",
    fg="gray"
)
info.pack(pady=10)

root.mainloop()