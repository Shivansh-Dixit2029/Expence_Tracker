open("expenses.txt", "a").close()

def expense():
    d = input("Date (DD-MM-YYYY): ")
    c = input("Category (Food/Travel/Shopping/Other): ")
    a = input("Amount: ")
    with open("expenses.txt", "a") as f:
        f.write(f"{d},{c},{a}\n")
    print("Added!\n")

def view():
    print("\n--- All Expenses ---")
    with open("expenses.txt", "r") as f:
        data_lines = f.readlines()
        if not data_lines:
            print("No records.\n")
            return
        for current_line in data_lines:
            items = current_line.strip().split(",")
            if len(items) == 3:
                D = items[0]
                C = items[1]
                A = items[2]
                print(f"{D} | {C} | ₹{A}")
            elif len(items) == 4:
                 D, C, A, N = items
                 print(f"{D} | {C} | ₹{A} (Old format, note: {N})")
    print()

def total_spent():
    total_sum = 0
    with open("expenses.txt", "r") as f:
        for each_line in f:
            data_parts = each_line.strip().split(",")
            if len(data_parts) >= 3:
                amount_val = data_parts[2]
                total_sum += float(amount_val) 
    print("\nTotal Money Spent:", total_sum, "\n") 

def monthly_summary():
    m_y = input("Enter month and year (MM-YYYY): ") 
    m_total = 0
    cat_totals = {} 
    with open("expenses.txt", "r") as f:
        found_data = False
        for L in f: 
            P = L.strip().split(",")
            if len(P) < 3:
                continue
            date = P[0]
            category = P[1]
            amount = P[2]
            parts = date.split("-")
            if len(parts) != 3:
                continue
            month_year = parts[1] + "-" + parts[2]
            if month_year == m_y:
                found_data = True
                amount_val = float(amount)        
                m_total += amount_val
                if category not in cat_totals:
                    cat_totals[category] = 0
                cat_totals[category] += amount_val
    if not found_data:
        print("No expenses for this month.\n")
        return
    print("\n--- Monthly Summary for", m_y, "---")
    print("Total spent:", m_total)
    print("Category-wise spending:")
    for cat, amt in cat_totals.items():
        print(f"{cat}: ₹{amt}")
    print()
while True:
    print("""
====== Expense Tracker ======
1. ➕ Log New Expense
2. 📖 View All Records
3. 💰 Calculate Total
4. 📊 Monthly Breakdown
5. 🚪 Exit Program
""")
    x = input("Choose: ")
    if x == "1":
        expense()
    elif x == "2":
        view()
    elif x == "3":
        total_spent()
    elif x == "4":
        monthly_summary()
    elif x == "5":
        break
    else:
        print("Invalid choice!\n")