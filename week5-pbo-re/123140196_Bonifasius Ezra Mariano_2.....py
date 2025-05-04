import tkinter as tk
from tkinter import messagebox
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Bonifasius")
        self.root.geometry("300x250")

        # Buat tampilan GUI login
        self.create_login_widgets()

    def create_login_widgets(self):
        # Label dan Entry untuk Username
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        # Label dan Entry untuk Password
        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Tombol Login dan Register
        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.open_register_window).pack(pady=5)

        # Status label
        self.status_label = tk.Label(self.root, text="", fg="red")
        self.status_label.pack(pady=5)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.validate_user(username, password):
            self.status_label.config(text="Login Berhasil!", fg="green")
            self.open_welcome_window(username)
        else:
            self.status_label.config(text="Username atau Password salah!", fg="red")

    def validate_user(self, username, password):
        if not os.path.exists("users.txt"):
            return False

        with open("users.txt", "r") as file:
            for line in file:
                user, pw = line.strip().split(":", 1)
                if user == username and pw == password:
                    return True
        return False

    def open_welcome_window(self, username):
        welcome_window = tk.Toplevel(self.root)
        welcome_window.title("Selamat Datang")
        welcome_window.geometry("250x100")
        tk.Label(welcome_window, text=f"Selamat Datang, {username}!").pack(pady=20)

    def open_register_window(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register Akun")
        register_window.geometry("300x200")

        tk.Label(register_window, text="Username Baru").pack(pady=5)
        username_entry = tk.Entry(register_window)
        username_entry.pack(pady=5)

        tk.Label(register_window, text="Password Baru").pack(pady=5)
        password_entry = tk.Entry(register_window, show="*")
        password_entry.pack(pady=5)

        def register_user():
            username = username_entry.get()
            password = password_entry.get()

            if not username or not password:
                messagebox.showerror("Error", "Username dan Password tidak boleh kosong.")
                return

            # Cek jika sudah ada
            if self.validate_user(username, password):
                messagebox.showwarning("Peringatan", "Akun sudah terdaftar!")
                return

            with open("users.txt", "a") as file:
                file.write(f"{username}:{password}\n")

            messagebox.showinfo("Sukses", "Registrasi berhasil!")
            register_window.destroy()

        tk.Button(register_window, text="Daftar", command=register_user).pack(pady=10)


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
