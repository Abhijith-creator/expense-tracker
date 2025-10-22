from db import get_connection

def add_expense(amount, category, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
                   (amount, category, description))
    conn.commit()
    conn.close()
    print("✅ Expense added successfully!")

def view_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    print("\nID | Amount | Category | Description | Date")
    print("-" * 50)
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")
    conn.close()

def delete_expense(exp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (exp_id,))
    conn.commit()
    conn.close()
    print("🗑️ Expense deleted!")
