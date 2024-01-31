```python
import tkinter as tk
from tkinter import messagebox
from email_creator.account_generator import create_account
from email_creator.config import load_config
from email_creator.utils import validate_email

class EmailAccountCreationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Account Creation App")
        self.config = load_config()

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        # Number of accounts label and entry
        self.num_accounts_label = tk.Label(self.main_frame, text="Number of Accounts:")
        self.num_accounts_label.grid(row=0, column=0, sticky="w")
        self.num_accounts_entry = tk.Entry(self.main_frame)
        self.num_accounts_entry.grid(row=0, column=1)

        # Start button
        self.start_button = tk.Button(self.main_frame, text="Start Creation", command=self.start_creation)
        self.start_button.grid(row=1, column=0, columnspan=2, pady=5)

    def start_creation(self):
        num_accounts = self.num_accounts_entry.get()
        if not num_accounts.isdigit() or int(num_accounts) <= 0:
            messagebox.showerror("Error", "Please enter a valid number of accounts.")
            return

        num_accounts = int(num_accounts)
        for _ in range(num_accounts):
            email, password = create_account(self.config)
            if validate_email(email):
                messagebox.showinfo("Success", f"Account created successfully: {email}")
            else:
                messagebox.showerror("Error", "Failed to create account.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailAccountCreationApp(root)
    root.mainloop()
```