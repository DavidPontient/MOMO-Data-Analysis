import sqlite3

# Connect to (or create) the SQLite database
conn = sqlite3.connect('momo_data.db')
cursor = conn.cursor()

# Create a table for SMS transactions
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    sender TEXT,
    receiver TEXT,
    amount REAL,
    currency TEXT,
    transaction_type TEXT,
    reference TEXT,
    message TEXT
)
''')

print(" Database and table 'transactions' created successfully.")

# Save and close the connection
conn.commit()
conn.close()
