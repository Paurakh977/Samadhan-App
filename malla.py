import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def plot_most_used_apps():
    # Connect to the database
    conn = sqlite3.connect('app_screen_time.db')
    cursor = conn.cursor()

    # Fetch data from the database and sort by total_screen_time
    cursor.execute("SELECT app_name, SUM(total_screen_time) FROM screen_time GROUP BY app_name")
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Calculate total screen time and filter apps with less than 5% usage
    total_time = sum(row[1] for row in data)
    labels = []
    sizes = []
    for row in data:
        if row[1] / total_time >= 0.05:
            labels.append(row[0])
            sizes.append(row[1])

    # Plotting 'Others' category for apps with less than 5% usage time
    other_apps_time = total_time - sum(sizes)
    if other_apps_time > 0:
        labels.append('Others')
        sizes.append(other_apps_time)

    # Determine the explode values for the slice with the highest percentage
    max_index = sizes.index(max(sizes))
    explode = [0.1 if i == max_index else 0 for i in range(len(labels))]

    # Plot the pie chart with unique colors
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, _, _ = ax.pie(sizes, labels=None, autopct='%1.1f%%', pctdistance=0.85, startangle=90, explode=explode, colors=plt.cm.tab20c(np.arange(len(labels))), wedgeprops=dict(width=0.4))

    # Set a title for the plot
    plt.title("Weekly App Usage Report", loc="left", fontsize=18, weight='light', color='#4A90E2', fontname='DejaVu Sans')

    # Create a legend without labels on the pie chart with adjusted bbox_to_anchor
    legend_without_labels = ax.legend(wedges, labels, title='', loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=len(labels), fontsize='small')

    # Add the legend without labels to the plot
    ax.add_artist(legend_without_labels)

    # Equal aspect ratio ensures that the pie chart is circular.
    ax.axis('equal')

    # Show the plot
    plt.show()

# Plot the pie chart with all applications used over the week and the "Others" category for apps with less than 5% usage
plot_most_used_apps()
