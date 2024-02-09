from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import matplotlib.pyplot as plt
from io import BytesIO
from smtplib import SMTP

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import datetime
class PieChartEmailSender:
    def __init__(self, receiver_email):
        self.receiver_email = receiver_email
        self.conn = sqlite3.connect('app_screen_time.db')  # Establish database connection


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

    def plot_most_used_apps_pie(self):
        conn = sqlite3.connect('app_screen_time.db')
        cursor = conn.cursor()

        cursor.execute("SELECT app_name, SUM(total_screen_time) FROM screen_time GROUP BY app_name")
        data = cursor.fetchall()

        conn.close()

        total_time = sum(row[1] for row in data)
        labels = []
        sizes = []

        for row in data:
            if row[1] / total_time >= 0.05:
                labels.append(row[0])
                sizes.append(row[1])

        other_apps_time = total_time - sum(sizes)
        if other_apps_time > 0:
            labels.append('Others')
            sizes.append(other_apps_time)

        max_index = sizes.index(max(sizes))
        explode = [0.1 if i == max_index else 0 for i in range(len(labels))]

        fig = Figure(figsize=(8, 8))
        ax = fig.add_subplot(111)

        wedges, _, _ = ax.pie(sizes, labels=None, autopct='%1.1f%%', pctdistance=0.85, startangle=90,
                            explode=explode, colors=plt.cm.tab20c(np.arange(len(labels))),
                            wedgeprops=dict(width=0.4))
        total_time = self.format_time(total_time)
        total_time_text = f'Total Screen Time: {(total_time)} seconds'  # Format the total time text

        # Create text element to display total screen time at the center
        ax.text(1.5, -1.3, total_time_text, fontsize=10, weight='bold', color='black', ha='center', va='center')

        legend_without_labels = ax.legend(wedges, labels, title='', loc="upper center", bbox_to_anchor=(0.5, 1.15),
                                        ncol=len(labels), fontsize='small')
        ax.add_artist(legend_without_labels)
        ax.axis('equal')
        ax.text(-1.3, -1.25, "Weekly App Usage Report", fontsize=18, weight='bold', color='#4A90E2', fontname='DejaVu Sans', ha='center')

        canvas = FigureCanvas(fig)
        
        # Save the plot as BytesIO object
        image_stream = BytesIO()
        fig.savefig(image_stream, format='png')
        image_stream.seek(0)  # Reset the stream position to the beginning

        return image_stream

    def send_email_with_attachment(self):
        daily_pie_chart = self.plot_most_used_apps_pie()
        weekly_line_graph = self.setupLineGraph()  

        # Set up email parameters
        sender_email = "pandeypaurakhraj@gmail.com"
        subject = "App Usage Report"
        body = "Your weekly app usage report."

        # Create a message container - the correct MIME type is multipart/alternative
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = subject

        # Attach the text to the email
        msg.attach(MIMEText(body, 'plain'))

        # Attach the images
        image_attachment1 = MIMEImage(daily_pie_chart.read())
        image_attachment2 = MIMEImage(weekly_line_graph.read())

        image_attachment1.add_header('Content-Disposition', 'attachment', filename='pie_chart.png')
        image_attachment2.add_header('Content-Disposition', 'attachment', filename='line_graph.png')
        
        msg.attach(image_attachment1)
        msg.attach(image_attachment2)

        # Connect to Gmail's SMTP server
        server = SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, "wofe qapr tmzk pymt")

        # Send the email
        server.sendmail(sender_email, self.receiver_email, msg.as_string())

        # Disconnect from the server
        server.quit()

        print(f"Email with the pie chart attachment has been sent to {self.receiver_email}.")

    def setupLineGraph(self):
    # Open the database connection
        conn = sqlite3.connect('app_screen_time.db')
        cursor = conn.cursor()
        self.fig, self.ax = plt.subplots()


        top_3_apps = self.get_top_3_apps(cursor)  # Pass the cursor to get_top_3_apps method
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        line_colors = ['#9370DB', 'limegreen', 'skyblue']

        # Matplotlib setup
        fig_line, ax_line = plt.subplots(figsize=(6, 4))

        for i, app_info in enumerate(top_3_apps):
            app_name = app_info[0]
            app_usage = []
            for day in days_of_week:
                cursor.execute("SELECT total_screen_time FROM screen_time WHERE app_name=? AND Day=?", (app_name, day))
                total_time = cursor.fetchone()
                app_usage.append(total_time[0] if total_time else 0)

            # Plotting usage over the week with specified line color and 'o' markers
            ax_line.plot(days_of_week, app_usage, label=app_name, marker='o', color=line_colors[i])

        # Set title, labels, legend, and other plot configurations
        title_font = {'family': 'sans-serif', 'weight': 'bold', 'size': 16, 'color': 'black'}
        ax_line.set_title('Trend of Most Used Apps Over The Week', fontdict=title_font, loc='left')
        ax_line.set_ylabel('Total Screen Time', color='grey')
        ax_line.legend(loc='upper left', bbox_to_anchor=(0.7, 1.07), ncol=len(top_3_apps), frameon=False, facecolor='white', edgecolor='white')
        ax_line.spines['top'].set_visible(False)
        ax_line.spines['right'].set_visible(False)
        ax_line.spines['bottom'].set_visible(True)
        ax_line.spines['left'].set_visible(False)
        plt.tick_params(axis='both', colors='grey')
        plt.grid(axis='y', linestyle='-', alpha=0.7)

        # Draw the canvas and save the plot as BytesIO object
        canvas_line = FigureCanvas(fig_line)
        image_stream = BytesIO()
        fig_line.savefig(image_stream, format='png')
        image_stream.seek(0)  # Reset the stream position to the beginning

        # Close the database connection
        conn.close()

        return image_stream
    
    def get_screen_time_per_day(self):
        cursor = self.conn.cursor()  # Use the connection attribute

        conn = sqlite3.connect('app_screen_time.db')

        cursor = conn.cursor()

        # Get the current day of the week
        today = datetime.datetime.today().strftime('%A')

        # Define the order of days starting from Sunday
        days_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        # Find the index of the first available day in the database
        first_day_index = days_order.index(today)

        # Reorder the days to start from the first available day
        reordered_days = days_order[first_day_index:] + days_order[:first_day_index]

        # Generate the ORDER BY clause based on the reordered days
        order_by_clause = 'CASE Day '

        for i, day in enumerate(reordered_days, start=1):
            order_by_clause += f'WHEN \'{day}\' THEN {i} '

        order_by_clause += 'END'

        # Execute the SQL query with the dynamically generated ORDER BY clause
        cursor.execute(f"SELECT Day, SUM(total_screen_time) FROM screen_time GROUP BY Day ORDER BY {order_by_clause}")

        data = cursor.fetchall()
        return data

    def get_top_3_apps(self, cursor):
        cursor.execute("SELECT app_name, SUM(total_screen_time) AS total_time FROM screen_time GROUP BY app_name ORDER BY total_time DESC LIMIT 3")
        top_3_apps = cursor.fetchall()
        return top_3_apps
   
    def setupBarGraphAnimation(self):
        fig, ax = plt.subplots()
        self.ax.clear()
        data = self.get_screen_time_per_day()
        days = [row[0] for row in data]
        total_screen_time = [row[1] for row in data]
        formatted_times = [self.format_time(time) for time in total_screen_time]
        self.ax.bar(days, total_screen_time, color='skyblue', width=0.6)  # Adjust width as per your preference
        self.ax.set_xlabel('Day of the Week')
        self.ax.set_ylabel('Total Screen Time')
        self.ax.set_title('Total Screen Time per Day')
        self.ax.grid(alpha=0.5)
        for x, y, label in zip(days, total_screen_time, formatted_times):
            self.ax.text(x, y, label, ha='center', va='bottom')
        image_stream = BytesIO()
        fig.savefig(image_stream, format='png')
        image_stream.seek(0)  # Reset the stream position to the beginning

if __name__ == "__main__":
    sender = PieChartEmailSender(receiver_email="pandeypaurakhraj@gmail.com")
    sender.plot_most_used_apps_pie()
    sender.send_email_with_attachment()
