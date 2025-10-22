from db import get_connection
import matplotlib.pyplot as plt

def monthly_summary(month):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount) 
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        GROUP BY category
    """, (month,))
    rows = cursor.fetchall()

    if not rows:
        print(f"No expenses found for {month}")
    else:
        print(f"\n📅 Monthly Summary for {month}")
        print("-" * 30)
        total = 0
        for category, amount in rows:
            print(f"{category}: ₹{amount}")
            total += amount
        print("-" * 30)
        print(f"Total Spent: ₹{total}")
    conn.close()


def monthly_chart(month):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount) 
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        GROUP BY category
    """, (month,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print(f"No data found for {month}")
        return

    categories = [r[0] for r in rows]
    amounts = [r[1] for r in rows]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color='skyblue', edgecolor='black')
    plt.title(f"Expense Breakdown for {month}")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def monthly_pie_chart(month):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        GROUP BY category
    """, (month,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print(f"No data found for {month}")
        return

    categories = [r[0] for r in rows]
    amounts = [r[1] for r in rows]

    plt.figure(figsize=(7, 7))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(f"Expense Distribution for {month}")
    plt.tight_layout()
    plt.show()
