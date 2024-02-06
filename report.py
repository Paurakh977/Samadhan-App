# -*- coding: utf-8 -*-




# Form implementation generated from reading ui file 'ok.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.








import datetime
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np







class Weekly(QMainWindow):
   
    def __init__(self):
        super(Weekly, self).__init__()
        self.setupUi(self)
       
       
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 455)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"  border: none;\n"
"  background-color: transparent;\n"
"  color: #FFF; /* Specify a default color */\n"
"}\n"
"\n"
"#centralwidget {\n"
"  background-color: white\n"
";\n"
"}\n"
"\n"
"#side_menu {\n"
"  background-color: #071e26;\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  padding: 10px;\n"
"  background-color: #071e26;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"#main_body {\n"
"  background-color: #071e26;\n"
"  border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 70))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("\n"
"                font-family: \'Istok Web\';\n"
"                font-weight: 700;\n"
"                font-size: 20px;\n"
"         \n"
"\n"
"            ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons_folder/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.frame_2)
        self.side_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.side_menu)
        self.frame_4.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Home_button = QtWidgets.QPushButton(self.frame_4)
        self.Home_button.setMinimumSize(QtCore.QSize(0, 80))
        self.Home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Home_button.setStyleSheet("QPushButton {\n"
"                font-family: \'Istok Web\';\n"
"                font-weight: 700;\n"
"                font-size: 20px;\n"
"         \n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"background-color:rgb(5, 171, 232    );    \n"
"            }\n"
"        \"\"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons_folder/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_button.setIcon(icon1)
        self.Home_button.setIconSize(QtCore.QSize(20, 20))
        self.Home_button.setObjectName("Home_button")
        self.verticalLayout_3.addWidget(self.Home_button)
        self.Daily_button = QtWidgets.QPushButton(self.frame_4)
        self.Daily_button.setMinimumSize(QtCore.QSize(0, 80))
        self.Daily_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Daily_button.setStyleSheet("QPushButton {\n"
"                font-family: \'Istok Web\';\n"
"                font-weight: 700;\n"
"                font-size: 20px;\n"
"\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"background-color:rgb(5, 171, 232    );    \n"
"            }\n"
"        \"\"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons_folder/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Daily_button.setIcon(icon2)
        self.Daily_button.setIconSize(QtCore.QSize(20, 20))
        self.Daily_button.setObjectName("Daily_button")
        self.verticalLayout_3.addWidget(self.Daily_button)
        self.Weekly_button = QtWidgets.QPushButton(self.frame_4)
        self.Weekly_button.setMinimumSize(QtCore.QSize(0, 80))
        self.Weekly_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Weekly_button.setStyleSheet("QPushButton {\n"
"                font-family: \'Istok Web\';\n"
"                font-weight: 700;\n"
"                font-size: 20px;\n"
"\n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"background-color:rgb(5, 171, 232    );    \n"
"            }\n"
"        \"\"")
        self.Weekly_button.setIcon(icon2)
        self.Weekly_button.setIconSize(QtCore.QSize(20, 20))
        self.Weekly_button.setObjectName("Weekly_button")
        self.verticalLayout_3.addWidget(self.Weekly_button)
        self.Reminder_button = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Reminder_button.sizePolicy().hasHeightForWidth())
        self.Reminder_button.setSizePolicy(sizePolicy)
        self.Reminder_button.setMinimumSize(QtCore.QSize(20, 80))
        self.Reminder_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reminder_button.setStyleSheet("QPushButton {\n"
"                font-family: \'Istok Web\';\n"
"                font-weight: 700;\n"
"                font-size: 20px;\n"
"         \n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"background-color:rgb(5, 171, 232    );    \n"
"            }\n"
"        \"\"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons_folder/calendar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Reminder_button.setIcon(icon3)
        self.Reminder_button.setIconSize(QtCore.QSize(20, 20))
        self.Reminder_button.setObjectName("Reminder_button")
        self.verticalLayout_3.addWidget(self.Reminder_button)
        self.return_button = QtWidgets.QPushButton(self.frame_4)
        self.return_button.setMinimumSize(QtCore.QSize(0, 80))
        self.return_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_button.setStyleSheet("QPushButton {\n"
"                font-family: \'Istok Web\';\n"
"                font-weight: 700;\n"
"                font-size: 20px;\n"
"         \n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"background-color:rgb(5, 171, 232    );    \n"
"            }\n"
"        \"\"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons_folder/arrow-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.return_button.setIcon(icon4)
        self.return_button.setIconSize(QtCore.QSize(20, 20))
        self.return_button.setObjectName("return_button")
        self.verticalLayout_3.addWidget(self.return_button)       
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.gridLayout = QtWidgets.QGridLayout(self.main_body)
        self.gridLayout.setObjectName("gridLayout")
        self.pie_chart_frame = QtWidgets.QFrame(self.main_body)
        self.pie_chart_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.pie_chart_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pie_chart_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pie_chart_frame.setObjectName("pie_chart_frame")
        
        self.plot_most_used_apps_pie()
        
        self.gridLayout.addWidget(self.pie_chart_frame, 0, 0, 1, 1)
        self.bar_graph_frame = QtWidgets.QFrame(self.main_body)
        self.bar_graph_frame.setMinimumSize(QtCore.QSize(0, 200))
        self.bar_graph_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.bar_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bar_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bar_graph_frame.setObjectName("bar_graph_frame")
       
        self.setupBarGraphAnimation()  
       
        self.gridLayout.addWidget(self.bar_graph_frame, 0, 1, 1, 1)
        self.line_graph_frame = QtWidgets.QFrame(self.main_body)
        self.line_graph_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;")
        self.line_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.line_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_graph_frame.setObjectName("line_graph_frame")
        self.line_graph_frame.setMinimumHeight(420)
        self.gridLayout.addWidget(self.line_graph_frame, 1, 0, 1, 2)
        self.setupLineGraph()
        self.horizontalLayout.addWidget(self.main_body)
        self.main_body.raise_()
        self.side_menu.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "Samadhan App"))
        self.Home_button.setText(_translate("MainWindow", "Home"))
        self.Daily_button.setText(_translate("MainWindow", "Daily"))
        self.Weekly_button.setText(_translate("MainWindow", "Weekly"))
        self.Reminder_button.setText(_translate("MainWindow", "Reminder"))
        self.return_button.setText(_translate("MainWindow", "Return"))   
       
    def setupLineGraph(self):
    # Open the database connection
        conn = sqlite3.connect('app_screen_time.db')
        cursor = conn.cursor()

        top_3_apps = self.get_top_3_apps(cursor)  # Pass the cursor to get_top_3_apps method
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        line_colors = ['#9370DB', 'limegreen', 'skyblue']

        # Matplotlib setup
        self.fig_line, self.ax_line = plt.subplots(figsize=(6, 4))
        self.canvas_line = FigureCanvas(self.fig_line)
        layout = QtWidgets.QVBoxLayout(self.line_graph_frame)
        layout.addWidget(self.canvas_line)

        for i, app_info in enumerate(top_3_apps):
            app_name = app_info[0]
            app_usage = []
            for day in days_of_week:
                cursor.execute("SELECT total_screen_time FROM screen_time WHERE app_name=? AND Day=?", (app_name, day))
                total_time = cursor.fetchone()
                app_usage.append(total_time[0] if total_time else 0)

            # Plotting usage over the week with specified line color and 'o' markers
            self.ax_line.plot(days_of_week, app_usage, label=app_name, marker='o', color=line_colors[i])

        # Set title, labels, legend, and other plot configurations
        title_font = {'family': 'sans-serif', 'weight': 'bold', 'size': 16, 'color': 'black'}
        self.ax_line.set_title('Trend of Most Used Apps Over The Week', fontdict=title_font, loc='left')
        self.ax_line.set_ylabel('Total Screen Time', color='grey')
        self.ax_line.legend(loc='upper left', bbox_to_anchor=(0.7, 1.07), ncol=len(top_3_apps), frameon=False, facecolor='white', edgecolor='white')
        self.ax_line.spines['top'].set_visible(False)
        self.ax_line.spines['right'].set_visible(False)
        self.ax_line.spines['bottom'].set_visible(True)
        self.ax_line.spines['left'].set_visible(False)
        plt.tick_params(axis='both', colors='grey')
        plt.grid(axis='y', linestyle='-', alpha=0.7)
        self.canvas_line.draw()

        # Close the database connection
        conn.close()

    def get_top_3_apps(self, cursor):
        cursor.execute("SELECT app_name, SUM(total_screen_time) AS total_time FROM screen_time GROUP BY app_name ORDER BY total_time DESC LIMIT 3")
        top_3_apps = cursor.fetchall()
        return top_3_apps
    
    def setupBarGraphAnimation(self):
        self.conn = sqlite3.connect('app_screen_time.db')
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        layout = QtWidgets.QVBoxLayout(self.bar_graph_frame)  # Create a layout for bar_graph_frame
        layout.addWidget(self.canvas)  # Add the canvas widget to the layout
        self.ani = animation.FuncAnimation(self.fig, self.update_plot, interval=1000)  # Fix method name

         
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




    def get_screen_time_per_day(self):
        cursor = self.conn.cursor()

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


    def update_plot(self, i):
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
 # Annotate bars with total screen time
        for x, y, label in zip(days, total_screen_time, formatted_times):
            self.ax.text(x, y, label, ha='center', va='bottom')


    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update_plot, interval=1000)
        plt.show()
    
       
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
        layout = QtWidgets.QVBoxLayout()  # Create a new layout
        layout.addWidget(canvas)
        self.pie_chart_frame.setLayout(layout)          
        
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Weekly()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())












