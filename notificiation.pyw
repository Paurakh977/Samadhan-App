from datetime import datetime
from PyQt5.QtCore import QTimer
import sqlite3,time
from plyer import notification
from main import PieChartEmailSender
conn = sqlite3.connect('app_screen_time.db')
cursor = conn.cursor()
cursor.execute("SELECT email FROM users LIMIT 1")
reciver_email= cursor.fetchone()[0]
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

def sendFirstNotification():
    checkTasksAndSendNotification()


def sendNotification_for_screen_time(message):
    notification.notify(
        title="Screen Time Limit Reached",
        message=message,
        timeout=10
    )

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

def checkScreenTimeAndSendNotification():
    today_day = datetime.now().strftime('%A')
    query = "SELECT total_screen_time FROM screen_time WHERE Day = ?"
    cursor.execute(query, (today_day,))
    total_screen_time_records = cursor.fetchall()

    if total_screen_time_records:
        total_screen_time_today = sum(record[0] for record in total_screen_time_records)
        total_screen_time_today_hours = seconds_to_hours(total_screen_time_today)
        if total_screen_time_today_hours > 2:  # 4 hours
            message = f"your screen time today reached : {int(total_screen_time_today_hours)} hours\n please take a break"
            
            sendNotification_for_screen_time(message.title())


while True:
    
    checkScreenTimeAndSendNotification()
    time.sleep(5)
    sendFirstNotification()
    time.sleep(5)
    pc = PieChartEmailSender(reciver_email)
    pc.send_email_with_attachment()
    time.sleep(30)    