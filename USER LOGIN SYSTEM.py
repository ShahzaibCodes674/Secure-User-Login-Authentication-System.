import os
import json
import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

users = []

def load_data():
    global users
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except:
        users = []

def save_data():
    with open("users.json", "w") as file:
        json.dump(users, file)

def generate_pdf():
    if not os.path.exists("users"):
        os.makedirs("users")

    file_path = "users/users.pdf"
    c = canvas.Canvas(file_path, pagesize = letter)

    y = 750
    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, 800, f"User List")
    
    for u in users:

        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = 750

        c.setFont("Helvetica", 10)
        line = f"{u['Username']} | {u['Password']}"
        c.drawString(50, y, line)
        y -= 20

    c.save()
    messagebox.showinfo(f"Success", "PDF generated")


def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror(f"Error", "Username and password required!")
        return
    
    user = {
        "Username": username,
        "Password": password
    }
    
    users.append(user)
    save_data()
    messagebox.showinfo("Added", "User added!")

    clear_fields()

def login_user():
    username = username_entry.get()
    password = password_entry.get()

    for u in users:
        if u["Username"] == username and u["Password"] == password:
            messagebox.showinfo(f"Success", "User login successfully!")
            return
        clear_fields()
            
    messagebox.showerror(f"Error", "User not found!")

def search_user():
    username = username_entry.get()
    resultbox.delete(0, tk.END)

    for u in users:
        if u["Username"] == username:
            resultbox.insert(tk.END, f"{u['Username']} | {u['Password']}")
            messagebox.showinfo(f"Complete", "User found!")
            return

    messagebox.showerror(f"Error", "User not found!")

def delete_user():
    username = username_entry.get()

    for u in users:
        if u["Username"] == username:
            users.remove(u)
            save_data()
            messagebox.showinfo("Deleted", "User deleted!")
            return
    
    messagebox.showerror(f"Error", "User not found!")

def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def show_all():
    resultbox.delete(0, tk.END)
    for u in users:
        resultbox.insert(tk.END, f"{u['Username']} | {u['Password']}")

# ..... GUI .....
bg = "#2C2F33"
fg = "#FFFFFF"


root = tk.Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.configure(bg="black")
btn_color = "#112C91"

root.title("USER LOGIN SYSTEM")
tk.Label(root, text = "USER LOGIN SYSTEM", bg="#2c2c3e", fg="white", font=("Arial", 20, "bold")).grid(row = 0, column = 0, columnspan = 2, pady = 5)
root.geometry("700x400")

# INPUTS
input_frame = tk.Frame(root, bg="#2c2c3e")
input_frame.grid(row=1, column=0, padx=20, pady=20)

tk.Label(input_frame, text = "Username", bg="#2c2c3e", fg="white", font=("Arial", 10)).grid(row = 1 , column = 0, padx = 10, pady = 8)
username_entry = tk.Entry(input_frame, bg="#3a3a4f", fg="white", insertbackground="white")
username_entry.grid(row = 1, column = 1, padx = 10, pady = 8)

tk.Label(input_frame, text = "Password", bg="#2c2c3e", fg="white", font=("Arial", 10)).grid(row = 2, column = 0, padx = 10, pady = 8)
password_entry = tk.Entry(input_frame, show = "*", bg="#3a3a4f", fg="white", insertbackground="white")
password_entry.grid(row = 2, column = 1, padx = 10, pady = 8)
    
# BUTTONS
button_frame = tk.Frame(root, bg="#2c2c3e")
button_frame.grid(row=2, column=0, padx=5, pady=5)

btn_reg = tk.Button(button_frame, text = "Register User", width=15, font=("Arial", 10), command = register_user, bg="#4a90e2", fg="white", activebackground="#357abd")
btn_reg.grid(row = 4, column = 0, padx = 5, pady = 5)

btn_login = tk.Button(button_frame, text = "Login User", width=15, font=("Arial", 10), command = login_user, bg="#4a90e2", fg="white", activebackground="#357abd")
btn_login.grid(row = 4, column = 1, padx = 5, pady = 5)

btn_search = tk.Button(button_frame, text = "Search User", width=15, font=("Arial", 10), command = search_user, bg="#4a90e2", fg="white", activebackground="#357abd")
btn_search.grid(row = 5, column = 0, padx = 5, pady = 5)

btn_delete = tk.Button(button_frame, text = "Delete User", width=15, font=("Arial", 10), command = delete_user, bg="#4a90e2", fg="white", activebackground="#357abd")
btn_delete.grid(row = 5, column = 1, padx =5, pady = 5)

btn_exp = tk.Button(button_frame, text = "Export PDF", width=15, font=("Arial", 10), command = generate_pdf, bg="#4a90e2", fg="white", activebackground="#357abd")
btn_exp.grid(row = 6, column = 0, padx = 5, pady = 5)

btn_all = tk.Button(button_frame, text = "Show All", width=15, font=("Arial", 10), command = show_all, bg="#4a90e2", fg="white", activebackground="#357abd")
btn_all.grid(row = 6, column = 1, padx = 5, pady = 5)

# OUTPUT
resultbox = tk.Listbox(root, width = 40, height = 15)
resultbox.grid(row = 1, column = 1, rowspan = 6, padx = 10)

load_data()
root.mainloop()

    
