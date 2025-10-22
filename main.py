from expense_ops import add_expense, view_expenses, delete_expense
from report import monthly_summary, monthly_chart, monthly_pie_chart
import db

def main_menu():
    db.create_table()
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Monthly Bar Chart")
        print("6. Monthly Pie Chart")
        print("7. Exit")

        choice = input("\nEnter choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(amount, category, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            exp_id = int(input("Enter Expense ID to delete: "))
            delete_expense(exp_id)

        elif choice == '4':
            month = input("Enter month (YYYY-MM): ")
            monthly_summary(month)

        elif choice == '5':
            month = input("Enter month (YYYY-MM): ")
            monthly_chart(month)

        elif choice == '6':
            month = input("Enter month (YYYY-MM): ")
            monthly_pie_chart(month)

        elif choice == '7':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main_menu()
