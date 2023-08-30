import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_var.set(generated_password)


win = tk.Tk()
win.title("Password Generator")


length_label = tk.Label(win, text="Password Length:")
length_label.pack(pady=20)

length_entry = tk.Entry(win)
length_entry.pack()


generate_button = tk.Button(win, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)


password_var = tk.StringVar()
password_label = tk.Label(win, textvariable=password_var)
password_label.pack()


win.mainloop()
 