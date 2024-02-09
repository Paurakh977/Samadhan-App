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
    
    

    query = '''
    SELECT app_name, SUM(total_screen_time) AS total_time
    FROM screen_time
    WHERE Day = ?
    GROUP BY app_name
    ORDER BY total_time DESC
    LIMIT 10;
'''

    # Execute the query with the current day as a parameter
    cursor.execute(query, (current_day,))
    results = cursor.fetchall()

    # Print the top 10 results
    if results:
        print("Top 10 most used apps:")
        for app, total_time in results:
            if total_time > 60:
                hours = int(total_time / 60)
                minutes = int(total_time % 60)
                print(f"{app}: {hours}h {minutes}m")
            else:
                print(f"{app}: {total_time} minutes")
    else:
        print(f"No screen time data found for {current_day}")

    # Close the connection
    conn.close()


daily_summary()