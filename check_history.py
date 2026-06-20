import sqlite3

conn = sqlite3.connect('history.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM history')
rows = cursor.fetchall()
print(rows)
conn.close()