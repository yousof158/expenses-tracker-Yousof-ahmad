import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import requests
import os
from dotenv import load_dotenv


load_dotenv() 
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yousof's Expenses Tracker 💰")
        self.root.geometry("700x650")
        
        # المتغيرات الخاصة بالتطبيق
        self.total_usd = 0.0
<<<<<<< HEAD
        self.api_key = os.getenv("API_KEY")
=======
        self.api_key = "7385506094a67e1d498d14ab" 
>>>>>>> 9fcf6cba7505ecd33530a69cb954ad2875133e1e
        self.base_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/"

        # --- تهيئة الـ GUI ---
        self.setup_ui()

    def setup_ui(self):
        # 1. قسم الإدخال (Input Section)
        input_frame = tk.LabelFrame(self.root, text="Add New Expense", font=("Arial", 12, "bold"), padx=10, pady=10)
        input_frame.pack(fill="x", padx=20, pady=10)

        # Amount
        tk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.amount_entry = tk.Entry(input_frame, font=("Arial", 11))
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Currency
        tk.Label(input_frame, text="Currency:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        currencies = ["USD", "EGP", "EUR", "SAR", "GBP", "CHF", "CAD"]
        self.curr_combo = ttk.Combobox(input_frame, values=currencies, state="readonly", width=10)
        self.curr_combo.current(0)
        self.curr_combo.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Category
        tk.Label(input_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        categories = ['Life Expenses', 'Electricity', 'Gas', 'Rental', 'Grocery', 'Savings', 'Education', 'Charity']
        self.categ_combo = ttk.Combobox(input_frame, values=categories, state="readonly")
        self.categ_combo.current(0)
        self.categ_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Payment Method
        tk.Label(input_frame, text="Payment:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        pay_methods = ["Cash", "Credit Card", "Paypal", "InstaPay", "Mobile Wallet"]
        self.pay_method_combo = ttk.Combobox(input_frame, values=pay_methods, state="readonly", width=15)
        self.pay_method_combo.current(0)
        self.pay_method_combo.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        # Date
        tk.Label(input_frame, text="Date:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.date_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Add Button
        add_btn = tk.Button(input_frame, text="Add Expense ➕", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.add_expense)
        add_btn.grid(row=3, column=0, columnspan=4, pady=15, sticky="ew")

        # 2. جدول العرض (Display Table)
        display_frame = tk.Frame(self.root)
        display_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("amount", "currency", "category", "method", "date")
        self.tree = ttk.Treeview(display_frame, columns=columns, show="headings", height=15)

        # تعريف الأعمدة
        headers = ["Amount", "Currency", "Category", "Payment Method", "Date"]
        for col, header in zip(columns, headers):
            self.tree.heading(col, text=header)
            self.tree.column(col, anchor="center", width=100)

        # شريط التمرير (Scrollbar)
        scrollbar = ttk.Scrollbar(display_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # سطر الإجمالي (Initial Total Row)
        self.tree.insert("", "end", iid="total_row", values=("0.00", "USD", "TOTAL", "---", "---"), tags=("total",))
        self.tree.tag_configure("total", background="#e3f42a", foreground="black", font=("Arial", 10, "bold"))

    def get_conversion_rate(self, currency_code):
        """جلب سعر الصرف من الـ API"""
        try:
            url = self.base_url + currency_code
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data['conversion_rates'].get("USD")
            else:
                return None
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def add_expense(self):
        raw_amount = self.amount_entry.get()
        
        # Validation Check
        try:
            amount = float(raw_amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error ❌", "Please enter a valid positive number for Amount!")
            return

        currency_from = self.curr_combo.get()
        
        # Fetch Data (Show loading logic could go here)
        rate = self.get_conversion_rate(currency_from)

        if rate is None:
            messagebox.showerror("Network Error 🌐", "Could not fetch exchange rates. Check internet connection.")
            return

        # Update Logic
        converted_value = amount * rate
        self.total_usd += converted_value

        # Insert into Table
        values = (amount, currency_from, self.categ_combo.get(), self.pay_method_combo.get(), self.date_entry.get_date())
        self.tree.insert("", 0, values=values) # Add to top

        # Update Total Row
        self.tree.item("total_row", values=(f"{self.total_usd:.2f}", "USD", "TOTAL", "---", "---"))

        # Clear Entry
        self.amount_entry.delete(0, "end")
        messagebox.showinfo("Success ✅", "Expense added successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    # تطبيق ثيم بسيط لتحسين الشكل
    style = ttk.Style()
    style.theme_use('clam') 
    
    app = ExpenseTrackerApp(root)
    root.mainloop()
