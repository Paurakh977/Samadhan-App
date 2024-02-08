from datetime import datetime
from PyQt5.QtCore import QTimer
import sqlite3
from plyer import notification

# Establish connection to the SQLite database
conn = sqlite3.connect(r'C:\Users\pande\OneDrive\Desktop\dkc\app_screen_time.db')
cursor = conn.cursor()

def sendNotification(task):
    notification.notify(
        title=f"{task}",
        message=f"Your Uncomplete Task for today is: {task}",
        timeout=10
    )

def checkTasksAndSendNotification():
    today_date = datetime.now().strftime('%Y-%m-%d')
    query = "SELECT task FROM tasks WHERE date = ? AND completed = 'NO'"
    cursor.execute(query, (today_date,))
    tasks = cursor.fetchall()

    if tasks:
        for task in tasks:
            sendNotification(task[0])

# Function to send the first notification after 10 seconds
def sendFirstNotification():
    checkTasksAndSendNotification()

# Call the function to send the first notification immediately
sendFirstNotification()

# Schedule subsequent notifications every hour
QTimer.singleShot(3600000, checkTasksAndSendNotification)  # 1 hour = 3600000 milliseconds
