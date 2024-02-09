import sqlite3
import datetime

def daily_summary():
    conn = sqlite3.connect(r'C:\Users\LENOVO\Desktop\samdhan\Samadhan-App\app_screen_time.db')
    cursor = conn.cursor()

    current_day = datetime.datetime.now().strftime('%A')

    query = '''
        SELECT MIN(time_opened) AS least_time_opened, MAX(time_closed) AS greatest_time_closed
        FROM timeline
        WHERE Day = ?
    '''

    cursor.execute(query, (current_day,))
    
    result = cursor.fetchone()

    if result:
        least_time_opened, greatest_time_closed = result
        print(f"Device first opened in {current_day} on: {least_time_opened}")
        if result[1]: 
            print(f"Device was last closed today {current_day} on: {greatest_time_closed}")
            
    
    else:
        print(f"No data found for {current_day}")
    
    
    query = """
    SELECT * FROM screen_time where Day = ? 
    group by app_name 
    order by total_screen_time DESC
    LIMIT 5;
    """

    # Execute the query with the current day as a parameter
    cursor.execute(query, (current_day,))
    results = cursor.fetchall()

    # Print the top 10 results
    if results:
        print("Top 5 most used apps:")
        application = []
        time = []
        for app, total_time, day in results:
            application.append(app)
            if total_time >= 3600:
                hours = total_time // 3600
                minutes = (total_time % 3600) // 60
                app_time = f"{hours}h {minutes}m"
                time.append(app_time)
            elif total_time >= 60:
                minutes = total_time // 60
                app_time = f"{minutes}m"
                time.append(app_time)
            else:
                app_time = f"{total_time}s"
                time.append(app_time)
        
    else:
        print(f"No screen time data found for {current_day}")

    # Close the connection
    conn.close()
    return application, time, greatest_time_closed,least_time_opened

print(daily_summary()[2])