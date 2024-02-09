import sqlite3
import time
import threading

class Check:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS timeline (
                            app_name TEXT,
                            time_opened TEXT,
                            time_closed TEXT,
                            Day TEXT
                        )''')
        self.conn.commit()

    def record_start_time(self, tab_name, current_time, present_day):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO timeline (app_name, time_opened, Day) VALUES (?, ?, ?)",
                    (tab_name, current_time, present_day))
        self.conn.commit()
        cursor.close()

    def record_end_time(self, tab_name, current_time):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE timeline SET time_closed=? WHERE app_name=? AND time_closed IS NULL",
                    (current_time, tab_name))
        self.conn.commit()
        cursor.close()

    def update_time_closed(self, tab_name):
        while True:
            current_time = time.strftime('%H:%M:%S')
            cursor = self.conn.cursor()
            cursor.execute("UPDATE timeline SET time_closed=? WHERE app_name=? AND time_closed IS NULL",
                           (current_time, tab_name))
            self.conn.commit()
            cursor.close()
            time.sleep(1)  # Update time_closed every second

# Example usage:
def main():
    db = Check("app_screen_time.db")
    current_time = time.strftime('%H:%M:%S')
    present_day = time.strftime('%A')
    print(current_time)

    db.record_start_time("YourProgram", current_time, present_day)

    update_thread = threading.Thread(target=db.update_time_closed, args=("YourProgram",))
    update_thread.daemon = True  # Set the thread as a daemon so it stops when the main program exits
    update_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        current_time = time.strftime('%H:%M:%S')
        db.record_end_time("YourProgram", current_time)

if __name__ == "__main__":
    main()
