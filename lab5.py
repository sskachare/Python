print("===== Monthly Expense Tracker =====")
# Step 1: Enter the number of initial expenses
n = int(input("Enter the number of expenses: "))

expenses = []
total = 0
# Step 2: Record initial expenses using for loop
for i in range(n):
    amount = float(input(f"Enter expense {i + 1}: "))
    expenses.append(amount)
    total += amount        # Accumulation logic
# Step 3: Continue until the user chooses to exit
while True:
    print("\n----- Expense Tracker Menu -----")
    print("1. Show All Expenses")
    print("2. Show Total Expense")
    print("3. Add New Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nExpense List:")
        for i in range(len(expenses)):
            print(f"Expense {i + 1}: {expenses[i]}")

    elif choice == 2:
        print("Total Monthly Expense =", total)

    elif choice == 3:
        new_expense = float(input("Enter new expense: "))
        expenses.append(new_expense)
        total += new_expense      # Accumulation logic
        print("Expense added successfully.")

    elif choice == 4:
        print("Thank you for using the Monthly Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")