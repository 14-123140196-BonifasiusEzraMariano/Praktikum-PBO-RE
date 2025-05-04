import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Bonifasius")
        self.root.geometry("300x200")

        self.correct_username = "bonifasius.123140196"
        self.correct_password = "2004-06-01"

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=5)

        self.status_label = tk.Label(self.root, text="", fg="red")
        self.status_label.pack(pady=5)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == self.correct_username and password == self.correct_password:
            self.status_label.config(text="Login Berhasil!", fg="green")
            self.open_welcome_window()
        else:
            self.status_label.config(text="Username atau Password salah!", fg="red")

    def open_welcome_window(self):
        welcome_window = tk.Toplevel(self.root)
        welcome_window.title("Selamat Datang")
        welcome_window.geometry("250x100")
        tk.Label(welcome_window, text="Selamat Datang, Bonifasius!").pack(pady=20)



if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
