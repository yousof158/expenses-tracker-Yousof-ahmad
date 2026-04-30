# 💰 Yousof's Expenses Tracker

A feature-rich desktop application built with Python and Tkinter to help you track your daily expenses. It automatically converts different currencies to a unified USD total using a live exchange rate API.

## ✨ Features
- **Interactive GUI:** Clean and user-friendly interface built with `Tkinter`.
- **Multi-Currency Support:** Add expenses in USD, EGP, EUR, SAR, GBP, CHF, or CAD.
- **Real-Time Conversion:** Integrates with `exchangerate-api.com` to instantly convert your expenses to a unified USD total.
- **Categorization:** Classify expenses (e.g., Grocery, Education, Electricity).
- **Payment Methods:** Track how you paid (Cash, Credit Card, InstaPay, etc.).
- **Smart Table:** View all entries in a scrollable, organized table with an auto-updating total row.
- **Security Best Practices:** API keys are secured using environment variables (`.env`).

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **GUI Framework:** Tkinter, ttk
- **Libraries:** `requests`, `tkcalendar`, `python-dotenv`

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yousof158/expenses-tracker-Yousof-ahmad.git
   cd expenses-tracker-Yousof-ahmad
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install requests tkcalendar python-dotenv
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your API key:
   ```
   API_KEY=your_api_key_here
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## 👨‍💻 Author

Yousof Ahmad Ibrahim Ramzy - Systems & Computer Engineering Student @ Al-Azhar University
