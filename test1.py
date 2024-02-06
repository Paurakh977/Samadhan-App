import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours >= 1:
        return f"{int(hours)} h {int(minutes)} min {int(seconds)} sec"
    elif minutes >= 1:
        return f"{int(minutes)} min {int(seconds)} sec"
    else:
        return f"{int(seconds)} sec"

def fetch_apps_used_today(cursor, today_day_of_week):
    cursor.execute("SELECT app_name, SUM(total_screen_time) FROM screen_time WHERE Day = ? GROUP BY app_name", (today_day_of_week,))
    return cursor.fetchall()

def update(frame):
    today_day_of_week = datetime.now().strftime('%A')
    data = fetch_apps_used_today(cursor, today_day_of_week)

    if not data:
        print(f"No data available for {today_day_of_week}.")
        return

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

    plt.clf()
    wedges, _, _ = plt.pie(sizes, labels=None, autopct='%1.1f%%', pctdistance=0.85, startangle=90, explode=[0.1 if i == sizes.index(max(sizes)) else 0 for i in range(len(labels))], colors=plt.cm.tab20c(np.arange(len(labels))), wedgeprops=dict(width=0.4))
    centre_circle = Circle((0, 0), 0.6, color='white', linewidth=1.25)
    plt.gca().add_artist(centre_circle)

    total_time_str = format_time(total_time)
    plt.text(0, 0, total_time_str, ha='center', va='center', fontsize=14, color='#4A90E2')

    plt.title(f"Apps Used on {today_day_of_week}", loc="left", fontsize=18, weight='light', color='#4A90E2', fontname='DejaVu Sans')

    legend_without_labels = plt.legend(wedges, labels, title='', loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=len(labels), fontsize='small')
    plt.gca().add_artist(legend_without_labels)

    plt.axis('equal')

conn = sqlite3.connect('app_screen_time.db')
cursor = conn.cursor()

ani = FuncAnimation(plt.gcf(), update, interval=1000)
plt.show()

conn.close()
