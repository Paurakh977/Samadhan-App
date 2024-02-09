import sqlite3
import datetime
import time

# Connect to the SQLite database
conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\samdhan\Samadhan-App\app_screen_time.db')
cursor = conn.cursor()

# Get the current time without milliseconds
initial_time = datetime.datetime.now().strftime('%I:%M:%S %p')
current_time = initial_time
today = datetime.datetime.now().strftime('%A')
# Insert the current time as time_opened and time_closed
cursor.execute('''INSERT INTO timeline (time_opened, time_closed, Day)
                  VALUES (?, ?, ?)''', (initial_time, current_time, today))

# Save (commit) the changes
conn.commit()

def timeliner():
   
        # Update time_closed every second
        current_time = datetime.datetime.now().strftime('%I:%M:%S %p')
        cursor.execute('''UPDATE timeline SET time_closed =? WHERE time_opened =? ''',
                       (current_time, initial_time))
        print(current_time)
        # Save (commit) the changes
        conn.commit()
        time.sleep(1)  # Wait for 1 second before the next update
    

if __name__=='__main__':
    while True:
        timeliner()


