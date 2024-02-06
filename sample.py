import sys
import pygetwindow as gw
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class AppMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Application Monitor')
        self.setGeometry(100, 100, 1000, 600)  # Larger window size


        self.conn = sqlite3.connect('app_screen_time.db')
        self.create_table()


        layout = QVBoxLayout(self)
        self.setLayout(layout)


        self.bar_graph_frame = QFrame(self)
        layout.addWidget(self.bar_graph_frame)


        self.bar_graph_layout = QVBoxLayout(self.bar_graph_frame)
        self.bar_graph_frame.setLayout(self.bar_graph_layout)


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data_and_plot)
        self.timer.start(1000)  # Update every second


    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS screen_time (
                            app_name TEXT PRIMARY KEY,
                            total_screen_time REAL
                        )''')
        self.conn.commit()


    def track_and_store_screen_time(self):
        active_window = gw.getActiveWindow()
        if active_window is not None:
            app_name = active_window.title


            if app_name != 'Application Monitor':  # Exclude details about the PyQt window
                if "Google Chrome" in app_name or "Firefox" in app_name or "Edge" in app_name:
                    tab_name = self.get_browser_tab_name(active_window)
                else:
                    tab_name = app_name


                cursor = self.conn.cursor()
                cursor.execute("SELECT total_screen_time FROM screen_time WHERE app_name=?", (tab_name,))
                row = cursor.fetchone()


                if row:
                    total_time = row[0] + 1  # Update every second
                    cursor.execute("UPDATE screen_time SET total_screen_time=? WHERE app_name=?", (total_time, tab_name))
                else:
                    cursor.execute("INSERT INTO screen_time (app_name, total_screen_time) VALUES (?, ?)", (tab_name, 1))


                self.conn.commit()


    def get_browser_tab_name(self, window):
        title = window.title
        if " - Google Chrome" in title:
            tab_name = title.split(" - Google Chrome")[0]
            if "- YouTube" in tab_name:
                tab_name = "YouTube"
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram"
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"
            return tab_name
        elif " - Mozilla Firefox" in title:
            tab_name = title.split(" - Mozilla Firefox")[0]
            if "- YouTube" in tab_name:
                tab_name = "YouTube"
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram"
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"
            return tab_name
        elif " - Microsoft Edge" in title:
            tab_name = title.split(" - Microsoft Edge")[0]
            if "- YouTube" in tab_name:
                tab_name = "YouTube"
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram"
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"
            return tab_name
        else:
            return title    




    def format_time(self, seconds):
        if seconds >= 3600:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{hours}h {minutes}m"
        elif seconds >= 60:
            minutes = seconds // 60
            return f"{minutes}m"
        else:
            return f"{seconds}s"


    def update_data_and_plot(self):
        self.track_and_store_screen_time()
        self.plot_graph()


    def plot_graph(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM screen_time WHERE app_name != 'Application Monitor' ORDER BY total_screen_time DESC LIMIT 5")
        data = cursor.fetchall()


        apps = [row[0] for row in data]
        times = [row[1] for row in data]


        formatted_times = [self.format_time(time) for time in times]


        fig, ax = plt.subplots(figsize=(15, 10))  # Larger figure size
        bars = ax.bar(apps, times, color='skyblue')
        ax.set_xlabel('Tabs/Applications', fontsize=14)
        ax.set_ylabel('Total Screen Time', fontsize=14)
        ax.set_title('Top Tabs/Applications by Total Screen Time', fontsize=16)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.yticks(fontsize=12)


        # Annotate bars with total time spent
        for bar, time in zip(bars, formatted_times):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{time}', ha='center', va='bottom', fontsize=12)


        plt.tight_layout()
       
        # Clear the previous layout
        for i in reversed(range(self.bar_graph_layout.count())):
            self.bar_graph_layout.itemAt(i).widget().setParent(None)


        # Embed the Matplotlib figure into the PyQt5 application
        canvas = FigureCanvas(fig)
        self.bar_graph_layout.addWidget(canvas)
        canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = AppMonitor()
    monitor.show()
    sys.exit(app.exec_())



