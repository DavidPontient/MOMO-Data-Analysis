import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()

# Create the transactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT,
    type TEXT,
    amount INTEGER,
    date TEXT,
    sender TEXT,
    receiver TEXT,
    category TEXT,
    body TEXT,
    readable_date TEXT,
    transaction_id TEXT             
)
''')

#Incase the more important fields dont exist, make them exist then.
cursor.execute('CREATE INDEX IF NOT EXISTS idx_category ON transactions(category)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_date ON transactions(date)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_amount ON transactions(amount)')

# Commit and close connection
conn.commit()
conn.close()

print("Database setup completed.")


