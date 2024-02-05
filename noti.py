from plyer import notification
import time

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=3  
    )

if __name__ == "__main__":
    while True:
        send_notification("Notification", "This is a notification pauri dada!")
        time.sleep(5)  
