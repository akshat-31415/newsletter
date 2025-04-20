import sqlite3

conn = sqlite3.connect('emails.db')
c = conn.cursor()

c.execute("SELECT * FROM subscribers")
rows = c.fetchall()

print("Subscribers:")
for row in rows:
    print(row)

conn.close()