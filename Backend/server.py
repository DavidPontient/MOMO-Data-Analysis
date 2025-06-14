from flask import Flask, send_from_directory, jsonify
import sqlite3
import os

app = Flask(__name__, static_folder='frontend')

DB_PATH = 'transactions.db'  # Make sure this matches your database file name

# Serve the HTML, CSS, JS files from the frontend folder
@app.route('/')
def serve_dashboard():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('frontend', path)

# Route to get all transaction data as JSON
@app.route('/data')
def get_transaction_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, type, amount, date, sender, receiver, transaction_id FROM transactions")
    rows = cursor.fetchall()
    conn.close()

    transactions = [
        {
            'id': row[0],
            'type': row[1],
            'amount': row[2],
            'date': row[3],
            'sender': row[4],
            'receiver': row[5],
            'transaction_id': row[6]
        }
        for row in rows
    ]

    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True)
