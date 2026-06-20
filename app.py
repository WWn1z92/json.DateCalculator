import sqlite3
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history')
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    date1 = data['date1']
    date2 = data['date2']

    if not date1 or not date2:
        return jsonify({'error': 'введи обе даты'})

    try:
        dt1 = datetime.strptime(date1, '%d.%m.%Y')
        dt2 = datetime.strptime(date2, '%d.%m.%Y')
    except ValueError:
        return jsonify({'error': 'неправильный формат даты'})

    days = (dt2 - dt1).days
    years = days // 365
    months = (days % 365) // 30
    weeks = ((days % 365) % 30) // 7
    remaining = ((days % 365) % 30) % 7

    result = f'{years} лет, {months} месяцев, {weeks} недель, {remaining} дней'

    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO history (date1, date2, result) VALUES (?, ?, ?)',
                   (date1, date2, result))
    conn.commit()
    conn.close()

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)