import tkinter as tk
from tkinter import messagebox
from auth import register_user, login_user
from membership import create_membership, view_memberships, get_membership_plans

class GymManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gym Management System")
        self.geometry("400x400")
        self.current_user = None
        self.membership_plans = get_membership_plans()
        self.create_login_page()
    
    def create_login_page(self):
        self.clear_frame()
        
        tk.Label(self, text="Login", font=("Arial", 20)).pack(pady=10)
        
        tk.Label(self, text="Username:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()
        
        tk.Button(self, text="Login", command=self.login).pack(pady=5)
        tk.Button(self, text="Register", command=self.create_register_page).pack()
    
    def create_register_page(self):
        self.clear_frame()
        
        tk.Label(self, text="Register", font=("Arial", 20)).pack(pady=10)
        
        tk.Label(self, text="Username:").pack()
        self.reg_username_entry = tk.Entry(self)
        self.reg_username_entry.pack()
        
        tk.Label(self, text="Password:").pack()
        self.reg_password_entry = tk.Entry(self, show="*")
        self.reg_password_entry.pack()
        
        tk.Button(self, text="Register", command=self.register).pack(pady=5)
        tk.Button(self, text="Back to Login", command=self.create_login_page).pack()
    
    def create_main_page(self):
        self.clear_frame()
        
        tk.Label(self, text="Welcome to the Gym Management System", font=("Arial", 20)).pack(pady=10)
        
        tk.Button(self, text="Create Membership", command=self.create_membership_page).pack(pady=5)
        tk.Button(self, text="View Memberships", command=self.view_memberships_page).pack(pady=5)
        tk.Button(self, text="Logout", command=self.create_login_page).pack(pady=5)
    
    def create_membership_page(self):
        self.clear_frame()
        
        tk.Label(self, text="Create Membership", font=("Arial", 20)).pack(pady=10)
        
        tk.Label(self, text="Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        
        tk.Label(self, text="Age:").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()
        
        tk.Label(self, text="Membership Type:").pack()
        self.membership_type_var = tk.StringVar(self)
        self.membership_type_var.set("Select a plan")
        self.membership_type_menu = tk.OptionMenu(self, self.membership_type_var, *self.membership_plans.keys(), command=self.update_price_label)
        self.membership_type_menu.pack()
        
        self.price_label = tk.Label(self, text="Price: $0")
        self.price_label.pack()
        
        tk.Button(self, text="Create", command=self.create_membership).pack(pady=5)
        tk.Button(self, text="Back to Main", command=self.create_main_page).pack()
    
    def update_price_label(self, membership_type):
        price = self.membership_plans.get(membership_type, 0)
        self.price_label.config(text=f"Price: ${price}")
    
    def view_memberships_page(self):
        self.clear_frame()
        
        tk.Label(self, text="View Memberships", font=("Arial", 20)).pack(pady=10)
        
        members = view_memberships()
        for member in members:
            tk.Label(self, text=f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}, Membership Type: {member[3]}").pack()
        
        tk.Button(self, text="Back to Main", command=self.create_main_page).pack()
    
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login_user(username, password):
            self.current_user = username
            self.create_main_page()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        if register_user(username, password):
            messagebox.showinfo("Success", "User registered successfully")
            self.create_login_page()
        else:
            messagebox.showerror("Error", "Username already exists")
    
    def create_membership(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        membership_type = self.membership_type_var.get()
        if membership_type == "Select a plan":
            messagebox.showerror("Error", "Please select a membership plan")
            return
        create_membership(name, int(age), membership_type)
        messagebox.showinfo("Success", "Membership created successfully")
        self.create_main_page()

if __name__ == "__main__":
    app = GymManagementApp()
    app.mainloop()
