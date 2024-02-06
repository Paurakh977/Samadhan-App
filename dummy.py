import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('app_screen_time.db')
cursor = conn.cursor()

# Create the screen_time table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS screen_time (
        app_name TEXT,
        total_screen_time INTEGER,
        Day TEXT
    )
''')

# List of dummy app names
app_names = ['App1', 'App2', 'App3', 'App4', 'App5']

# Insert dummy data into the screen_time table
for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
    for app_name in app_names:
        total_screen_time = random.randint(1, 100)  # Random screen time between 1 and 100 minutes
        cursor.execute('INSERT INTO screen_time VALUES (?, ?, ?)', (app_name, total_screen_time, day))

# Commit changes and close the database connection
conn.commit()
conn.close()

print("Dummy data inserted successfully.")  
