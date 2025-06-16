from flask import Flask, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__, static_folder='../frontend')

DB_PATH = os.path.join(os.path.dirname(__file__), 'transactions.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/data')
def get_transactions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    
    transactions = []
    for row in rows:
        transactions.append({
            'id': row['id'],
            'type': row['type'],
            'amount': row['amount'],
            'date': row['date'],
            'sender': row['sender'],
            'receiver': row['receiver'],
            'category': row['category'],
            'body': row['body'],
            'readable_date': row['readable_date'],
            'transaction_id': row['transaction_id']
        })

    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True)
