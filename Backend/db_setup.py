import sqlite3

def create_db():
    conn = sqlite3.connect('momo_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            date TEXT,
            message TEXT,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    print("Database and table created.")

