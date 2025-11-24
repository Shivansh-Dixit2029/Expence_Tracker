# Expence_Tracker
Expense tracker built in Python , It logs daily financial entries (date, category, amount) to a plain text file (expenses.txt) for persistent, portable storage. It provides  functions to view all records, calculate total spent, and can generate a category-wise summary for any specific month.

Features:-
1. ➕ Log New Expense: Quickly record transactions with Date, Category (e.g., Food, Travel), and Amount.
2. 📖 View All Records: Displays a comprehensive list of every logged expense.
3. 💰 Calculate Grand Total: Computes and displays the sum of all amounts recorded in the system.
4. 📊 Monthly Breakdown: Analyzes expenses for a user-specified month and year (MM-YYYY) and presents totals grouped by category.

Technologies used:-
1. Python 3
2. File Handling ('read','write','append')
3. Basic string manipulation

Steps to Install & Run the Project:-
1.Open your terminal or command prompt.
2.Navigate to the directory where you saved the file.
3.Run the application -python Exp_Tracker.py

Instructions For testing:-
TC-01: Initialization,Run the script for the first time.,"The expenses.txt file is created, and the main menu is displayed."

TC-02: Add Expense,"Choose 1 (Add Expense), enter: 01-11-2025, Food, 500.","The console prints ""Added!"" and the line 01-11-2025,Food,500\n is written to expenses.txt."

TC-03: Add Second Expense,"Choose 1, enter: 15-11-2025, Travel, 250.50.",A second line is written to expenses.txt.

TC-04: View Records,Choose 2 (View Expenses).,The console lists both entries with the format: `DD-MM-YYYY

TC-05: Total Spent,Choose 3 (Total Spent).,"The console prints the sum: ""Total Money Spent: 750.5"" (500 + 250.50)."

TC-06: Monthly Summary,"Choose 4 (Monthly Summary), enter month: 11-2025.","The console displays: Total spent: 750.5 and category breakdown: Food: ₹500, Travel: ₹250.5."

TC-07: No Records,"Choose 4, enter a month with no data (e.g., 12-2025).","The console prints ""No expenses for this month."""
<img width="1526" height="958" alt="Screenshot 2025-11-24 223711" src="https://github.com/user-attachments/assets/5a61e445-7fd2-498a-ad00-d01500580eab" />
