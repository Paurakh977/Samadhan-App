import sqlite3
import pygetwindow as gw
import time
from pywinauto import Application
import datetime

class ScreenTimeTracker:
    def __init__(self, db_name=r'C:\Users\pande\OneDrive\Desktop\dkc\app_screen_time.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS screen_time (
                            app_name TEXT ,
                            total_screen_time REAL,
                            Day TEXT
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS timeline (
                            app_name TEXT ,
                            time_opened datetime,
                            time_closed datetime,
                            Day
                        )''')
    
    def get_total_screen_time_today(self, present_day):
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(total_screen_time) FROM screen_time WHERE Day=?", (present_day,))
        total_screen_time_today = cursor.fetchone()[0]
        return total_screen_time_today

       
    def track_and_store_screen_time(self):
        active_window = gw.getActiveWindow()
        now = datetime.datetime.now()
        present_day = now.strftime("%A")
        current_time = now.strftime("%H:%M:%S")
        while True:
            active_window = gw.getActiveWindow()
            if active_window is not None:
                app_name = active_window.title
                if app_name != 'Main Window':  # Exclude details about the PyQt window
                    if "Google Chrome" in app_name or "Firefox" in app_name or "Microsoft Edge" in app_name:
                        tab_name = self.get_browser_tab_name(active_window)        
                    else:
                        tab_name = app_name.split("-")[-1].strip()

                    cursor = self.conn.cursor()
                    try:
                        # Check if a row exists for the current tab_name and present_day
                        cursor.execute("SELECT total_screen_time FROM screen_time WHERE app_name=? AND Day=?",
                                    (tab_name, present_day))
                        row = cursor.fetchone()

                        if row:
                            # If the row exists, update the screen time in that row
                            total_time = row[0] + 1  # Update every second
                            cursor.execute("UPDATE screen_time SET total_screen_time=? WHERE app_name=? AND Day=?",
                                        (total_time, tab_name, present_day))
                        else:
                            # If the row doesn't exist, insert a new row for the current tab_name and present_day
                            cursor.execute("INSERT INTO screen_time (app_name, total_screen_time, Day) VALUES (?, ?, ?)",
                                        (tab_name, 1, present_day))

                        # Check if a timeline entry exists for the current tab_name and if it's not closed yet
                        cursor.execute("SELECT * FROM timeline WHERE app_name=? AND time_closed IS NULL", (tab_name,))
                        row = cursor.fetchone()

                        if row:
                            cursor.execute("UPDATE timeline SET time_closed=? WHERE app_name=? AND time_closed IS NULL",
                                        (current_time, tab_name))
                        else:
                            cursor.execute("INSERT INTO timeline (app_name, time_opened, Day) VALUES (?, ?, ?)",
                                        (tab_name, current_time, present_day))

                        self.conn.commit()
                    finally:
                        cursor.close()

            time.sleep(1)  # Track every second
        # Track every second

    def get_browser_tab_name(self, window):
        title = window.title
        
        if " - Google Chrome" in title:

            if "- YouTube" in title:
                tab_name="Youtube"
                return tab_name
            else:   
                app = Application(backend='uia')
                app.connect(title_re=".*Chrome.*", found_index=0)
                element_name="Address and search bar"
                dlg = app.top_window()
                url = dlg.child_window(title=element_name, control_type="Edit").get_value()
                if "localhost" in url:
                    tab_name="localhost Server" 
                    return tab_name
                else:
                    tab_name= url.split(".com")[0]
                    return tab_name
        elif " - Mozilla Firefox" in title:
            if "- YouTube" in title:
                tab_name="Youtube"
                return tab_name
            else:    
                app = Application(backend='uia')
                app.connect(title_re=".*Chrome.*", found_index=0)
                element_name="Address and search bar"
                dlg = app.top_window()
                url = dlg.child_window(title=element_name, control_type="Edit").get_value()
                tab_name= url.split(".com")[0]
                return tab_name
        elif "Edge" in title:
            if "YouTube" in title:
                tab_name="Youtube"
                return tab_name
            else:    
                app = Application(backend='uia')
                app.connect(title_re=".*Microsoft​ Edge.*", found_index=0)
                dlg = app.top_window()
                wrapper = dlg.child_window(title="App bar", control_type="ToolBar")
                url = wrapper.descendants(control_type='Edit')[0]
                url=url.get_value()
                if "www" in url:
                    tab_name=url.split('www.')[1].split('.com')[0]
                    return tab_name
                elif ".com" in url:
                    tab_name=url.split('.com')[0].split('https://')[1] 
                    return tab_name   
                else:
                    tab_name='new tab'
                    return tab_name    
        else:
            return title   

def main():
    tracker = ScreenTimeTracker()
    tracker.track_and_store_screen_time()

if __name__ == "__main__":
    main()
