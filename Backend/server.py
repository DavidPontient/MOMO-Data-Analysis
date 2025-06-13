from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import os

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def serve_index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('frontend', path)

@app.route('/data')
def get_data():
    category = request.args.get('category', 'All')
    conn = sqlite3.connect('momo_data.db')
    c = conn.cursor()
    if category == 'All':
        c.execute("SELECT sender, date, message, category FROM transactions")
    else:
        c.execute("SELECT sender, date, message, category FROM transactions WHERE category = ?", (category,))
    rows = c.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            'sender': row[0],
            'date': row[1],
            'message': row[2],
            'category': row[3]
        })
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
