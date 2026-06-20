import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY,
    date1 TEXT,
    date2 TEXT,
    result TEXT
)''')

conn.commit()

cursor.execute('''INSERT INTO history (date1, date2, result)
    VALUES ('30.01.2008', '12.12.2021', '13 лет')''')

cursor.execute("UPDATE history SET result = '19 лет' WHERE id = 1")
conn.commit()

conn.commit()

cursor.execute('SELECT * FROM history')
rows = cursor.fetchall()
print(rows)

cursor.execute('SELECT * FROM history WHERE id = 1')
row = cursor.fetchone()
print(row)

cursor.execute('DELETE FROM history WHERE id = 3')
conn.commit()

cursor.execute('SELECT * FROM history')
rows = cursor.fetchall()
print(rows)
 
 

conn.close()

conn = sqlite3.connect('history.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM history')
rows = cursor.fetchall()
print(rows)
conn.close()

print("готово")