import sqlite3

def run_sql_code(sql_code, db_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.executescript(sql_code)
        conn.commit()
        print("SQL code executed successfully.")
    except sqlite3.Error as e:
        print(f"Error executing SQL code: {e}")
    finally:
        conn.close()

# Example SQL code
sql_code = """
DELETE FROM timeline

"""

# Replace 'your_database_name.db' with the actual name of your SQLite database file
db_name = 'app_screen_time.db'

# Run the SQL code
run_sql_code(sql_code, db_name)
