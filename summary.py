import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

class Daily():
    def piechart_daily():
        conn = sqlite3.connect('app_screen_time.db')
        cursor = conn.cursor()
        now = datetime.now()
        present_day = now.strftime("%A")
        cursor.execute('SELECT app_name, total_screen_time FROM screen_time WHERE day = ?', (present_day,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        app_names = [row[0] for row in rows]
        screen_times = [row[1] for row in rows]
        app_totals = {}
        for app_name, screen_time in zip(app_names, screen_times):
            app_totals[app_name] = app_totals.get(app_name, 0) + screen_time
        sorted_app_totals = sorted(app_totals.items(), key=lambda x: x[1], reverse=True)
        top_apps = sorted_app_totals[:4]
        others_total = sum(app[1] for app in sorted_app_totals[4:])
        labels = [app[0] for app in top_apps] + ['Others']
        sizes = [app[1] for app in top_apps] + [others_total]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(f'Top 4 Most Used Apps and Others for {present_day}')
        plt.show()

    
class Weekly():
    def screen_time_weekly_bar_graph():
        conn = sqlite3.connect('app_screen_time.db')
        cursor = conn.cursor()
        cursor.execute('SELECT day, SUM(total_screen_time) FROM screen_time GROUP BY day')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        # Filter out None values from the 'days' list
        days = [row[0] for row in rows if row[0] is not None]

        total_screen_times_seconds = [row[1] for row in rows if row[0] is not None]
        total_screen_times_minutes = [time_seconds / 60 for time_seconds in total_screen_times_seconds]

        plt.bar(days, total_screen_times_minutes, color='blue')
        plt.xlabel('Days of the Week')
        plt.ylabel('Total Screen Time (minutes)')
        plt.title('Screen Time for Each Day')
        plt.show()

    def most_apps_used_pie_chart():
        conn = sqlite3.connect('app_screen_time.db')
        cursor = conn.cursor()
        cursor.execute('SELECT app_name, SUM(total_screen_time) FROM screen_time GROUP BY app_name')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        sorted_apps = sorted(rows, key=lambda x: x[1], reverse=True)
        top_apps = sorted_apps[:5]
        others_total = sum(app[1] for app in sorted_apps[5:])
        labels = [app[0] for app in top_apps] + ['Others']
        sizes = [app[1] for app in top_apps] + [others_total]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Top 5 Most Used Apps and Others for the Week')
        plt.show()

    def usage_trend_line_graph():
        conn = sqlite3.connect('app_screen_time.db')
        cursor = conn.cursor()
        cursor.execute('SELECT day, app_name, SUM(total_screen_time) FROM screen_time GROUP BY day, app_name')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        sorted_apps = sorted(rows, key=lambda x: x[2], reverse=True)
        top_apps = {app[1]: [] for app in sorted_apps[:5]}
        for row in sorted_apps:
            if row[1] in top_apps:
                top_apps[row[1]].append(row[2] / 60)

        # Filter out None values from the 'days' list
        days = list(set(row[0] for row in sorted_apps if row[0] is not None))

        for app, usage in top_apps.items():
            plt.plot(days, usage, label=app)

        plt.xlabel('Days of the Week')
        plt.ylabel('Screen Time (minutes)')
        plt.title('Trend of Usage for Top 5 Apps in the Week')
        plt.legend()
        plt.show()

# Daily.piechart_daily()
# Weekly.screen_time_weekly_bar_graph()
# Weekly.most_apps_used_pie_chart()
# Weekly.usage_trend_line_graph()


