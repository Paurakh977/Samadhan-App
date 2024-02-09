import sqlite3
import datetime
import time

# Connect to the SQLite database
conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\samdhan\Samadhan-App\app_screen_time.db')
cursor = conn.cursor()

# Get the current time without milliseconds
initial_time = datetime.datetime.now().replace(microsecond=0)
current_time = initial_time

# Insert the current time as time_opened and time_closed
cursor.execute('''INSERT INTO timeline (time_opened, time_closed, Day)
                  VALUES (?, ?, ?)''', (initial_time, current_time, current_time.strftime('%A')))

# Save (commit) the changes
conn.commit()

def timeliner():
    try:
        # Update time_closed every second
        current_time = datetime.datetime.now().replace(microsecond=0)
        print('hello')
        cursor.execute('''UPDATE timeline SET time_closed =? WHERE time_opened =? ''',
                       (current_time, initial_time))
        print(current_time)
        # Save (commit) the changes
        conn.commit()
        time.sleep(1)  # Wait for 1 second before the next update
    except KeyboardInterrupt:
        pass  # Catch Ctrl+C to exit the loop

if __name__=='__main__':
    while True:
        timeliner()

# Close the connection after exiting the loop
conn.close()
