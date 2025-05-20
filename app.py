import sqlite3

# Step 1: Connect to DB
conn = sqlite3.connect('my_db.db')
cursor = conn.cursor()

# Step 2: Table create
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT
)
                         
''')

cursor.execute("INSERT INTO students (name, age, email) VALUES ('Ayesha', 20, 'l7ZV7@example.com')")
cursor.execute("INSERT INTO students (name, age, email) VALUES ('Bilal', 21, 'zTtJF@example.com')")


conn.commit()
conn.close()