import random
import string
from tkinter import *
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4.")
            return

        # Character sets
        characters = string.ascii_letters + string.digits + string.punctuation

        # Ensuring password strength with at least one of each
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        # Filling the remaining length with random characters
        password += random.choices(characters, k=length-4)
        random.shuffle(password)

        final_password = ''.join(password)
        result_label.config(text="Generated Password: " + final_password)
        copy_button.config(state=NORMAL)
        result_label.password = final_password

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.password)
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# UI Design
root = Tk()
root.title("Password Generator")
root.geometry("400x300")

Label(root, text="Enter Password Length:").pack()
length_entry = Entry(root)
length_entry.pack()

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = Label(root, text="", fg="blue", wraplength=350)
result_label.pack()

copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=DISABLED)
copy_button.pack()

root.mainloop()
