import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()

# Create the transactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    amount INTEGER,
    date TEXT,
    sender TEXT,
    receiver TEXT,
    transaction_id TEXT
)
''')

# Commit and close connection
conn.commit()
conn.close()

print("Database setup completed.")


