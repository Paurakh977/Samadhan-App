import sqlite3
import pygetwindow as gw
import time
from pywinauto import Application

class ScreenTimeTracker:
    def __init__(self, db_name='app_screen_time.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS screen_time (
                            app_name TEXT PRIMARY KEY,
                            total_screen_time REAL
                        )''')
        self.conn.commit()

    def track_and_store_screen_time(self):
        while True:
            active_window = gw.getActiveWindow()
            if active_window is not None:
                app_name = active_window.title
                
                if app_name != 'Main Window':  # Exclude details about the PyQt window
                    if "Google Chrome" in app_name or "Firefox" in app_name or "Microsoft​ Edge" in app_name:
                        tab_name = self.get_browser_tab_name(active_window)        
                    else:
                        tab_name = app_name.split("-")[-1]
                        tab_name = tab_name.strip()

                    cursor = self.conn.cursor()
                    cursor.execute("SELECT total_screen_time FROM screen_time WHERE app_name=?", (tab_name,))
                    row = cursor.fetchone()

                    if row:
                        total_time = row[0] + 1  # Update every second
                        cursor.execute("UPDATE screen_time SET total_screen_time=? WHERE app_name=?", (total_time, tab_name))
                    else:
                        cursor.execute("INSERT INTO screen_time (app_name, total_screen_time) VALUES (?, ?)", (tab_name, 1))

                    self.conn.commit()

            time.sleep(1)  # Track every second

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
            if "- YouTube" in title:
                tab_name="Youtube"
                return tab_name
            else:    
                app = Application(backend='uia')
                app.connect(title_re=".*Microsoft​ Edge.*", found_index=0)
                dlg = app.top_window()
                wrapper = dlg.child_window(title="App bar", control_type="ToolBar")
                url = wrapper.descendants(control_type='Edit')[0]
                tab_name=(url.get_value()).split("www.")[1]
                tab_name=tab_name.split(".com")[0]
                return tab_name
        elif "- Visual Studio Code" in title:
                title="Visual Studio Code"
                return title
        else:
            return title    

def main():
    tracker = ScreenTimeTracker()
    tracker.track_and_store_screen_time()

if __name__ == "__main__":
    main()
