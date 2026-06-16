from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    date1 = data['date1']
    date2 = data['date2']
    
    dt1 = datetime.strptime(date1, '%d.%m.%Y')
    dt2 = datetime.strptime(date2, '%d.%m.%Y')
    
    days = (dt2 - dt1).days
    years = days // 365
    months = (days % 365) // 30
    weeks = ((days % 365) % 30) // 7
    remaining = ((days % 365) % 30) % 7
    
    return jsonify({
        'result': f'{years} лет, {months} месяцев, {weeks} недель, {remaining} дней'
    })

if __name__ == '__main__':
    app.run(debug=True)