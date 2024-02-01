# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ok.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
import welbeings_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pygetwindow as gw
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import sqlite3
import datetime


class Ui_MainWindow(object):
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
"padding:20px\n;"
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignTop)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignTop)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(20, 80))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
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
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignTop)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
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
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.gridLayout = QtWidgets.QGridLayout(self.main_body)
        self.gridLayout.setObjectName("gridLayout")
        self.bar_graph_frame = QtWidgets.QFrame(self.main_body)
        self.bar_graph_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"margin-right:35px;")
        self.bar_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bar_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bar_graph_frame.setObjectName("bar_graph_frame")
        self.bar_graph_layout = QVBoxLayout(self.bar_graph_frame)
        self.bar_graph_frame.setLayout(self.bar_graph_layout)
        
        self.conn = sqlite3.connect('app_screen_time.db')
        self.create_table()
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.update_data_and_plot)
        self.timer.start(1000)
        
        self.gridLayout.addWidget(self.bar_graph_frame, 0, 0, 2, 1)
        self.tasks_frame = QtWidgets.QFrame(self.main_body)
        self.tasks_frame.setMaximumSize(QtCore.QSize(166767, 400))
        self.tasks_frame.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"border-radius:7px;")
        self.tasks_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tasks_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tasks_frame.setObjectName("tasks_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tasks_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Task_1 = QtWidgets.QLabel(self.tasks_frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Task_1.setFont(font)
        self.Task_1.setText("Meeting at 7:15 AM 1st FEB")
        self.Task_1.setStyleSheet("background-color: #071e26;\n"
"border:5px solid white;\n"
"border-radius:7px;\n"
"font-family:Times New Roman;\n"
"color:white;\n"
"font-weight:600;")
        self.Task_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Task_1.setObjectName("Task_1")
        self.verticalLayout_6.addWidget(self.Task_1)
        self.Task_2 = QtWidgets.QLabel(self.tasks_frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Task_2.setFont(font)
        self.Task_2.setStyleSheet("background-color: #071e26;\n"
"border:1px solid white;\n"
"border-radius:5px;\n"
"font-family:Times New Roman;\n"

"font-weight:600;")
        self.Task_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Task_2.setObjectName("Task_2")
        self.verticalLayout_6.addWidget(self.Task_2)
        self.Task_3 = QtWidgets.QLabel(self.tasks_frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Task_3.setFont(font)
        self.Task_3.setStyleSheet("background-color: #071e26;\n"
"border:1px solid white;\n"
"border-radius:5px;\n"
"font-family:Times New Roman;\n"

"font-weight:600;")
        self.Task_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Task_3.setObjectName("Task_3")
        self.verticalLayout_6.addWidget(self.Task_3)
        self.gridLayout.addWidget(self.tasks_frame, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.tasks_frame, 0, 1, 1, 1)
        
        self.extra_frame = QtWidgets.QFrame(self.main_body)
        self.extra_frame.setStyleSheet("background-color: transparent;\n"
"border-radius:7px;")
        self.extra_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.extra_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extra_frame.setObjectName("extra_frame")
        self.extra_frame.setMaximumWidth(680)
        self.extra_frame.setMinimumHeight(600)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.extra_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.extra_frame)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 120))
        self.lcdNumber.setStyleSheet("background-color: #071e26;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_5.addWidget(self.lcdNumber)
        from graph_ import CPU_details
        
        self.CPU_DETAILS_FRAME = QtWidgets.QFrame(self.extra_frame)
        self.CPU_DETAILS_FRAME.setStyleSheet("padding:0px;")
        self.CPU_DETAILS_FRAME.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CPU_DETAILS_FRAME.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CPU_DETAILS_FRAME.setMaximumHeight(390)
        self.verticalLayout_5.addWidget(self.CPU_DETAILS_FRAME)

        # Create an instance of CPU_details widget
        self.cpu_details_widget = CPU_details(parent=self.CPU_DETAILS_FRAME)
        # Add CPU_details widget to CPU_DETAILS_FRAME layout
        self.cpu_details_widget = CPU_details(parent=self.CPU_DETAILS_FRAME)  # Pass CPU_DETAILS_FRAME as the parent
        self.verticalLayout_5.addWidget(self.cpu_details_widget)
        layout = QtWidgets.QVBoxLayout(self.CPU_DETAILS_FRAME)
        layout.addWidget(self.cpu_details_widget)
        
        
        self.gridLayout.addWidget(self.extra_frame, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.main_body)
        self.timer=QTimer()
        self.timer.timeout.connect(self.lcd_number)
        self.timer.start(1000)
        self.lcd_number()
        self.main_body.raise_()
        self.side_menu.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menu_expanded = False

        # Connect the button click event to the toggle_menu function
        self.pushButton.clicked.connect(self.toggle_menu)

        # Set up the animation for the side menu
        self.side_menu_animation = QtCore.QPropertyAnimation(self.side_menu, b"maximumWidth")
        self.side_menu_animation.setDuration(300)

        # Set up the central widget animation for overlay effect
        self.central_widget_animation = QtCore.QPropertyAnimation(self.centralwidget, b"geometry")
        self.central_widget_animation.setDuration(300)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def toggle_menu(self):
        # Toggle the menu state
        self.menu_expanded = not self.menu_expanded

        # Define the target width for the side menu
        target_width = 200 if self.menu_expanded else 0

        # Update the side menu animation
        self.side_menu_animation.setEndValue(target_width)
        self.side_menu_animation.start()

        # Update the central widget animation for overlay effect
        if self.menu_expanded:
            self.central_widget_animation.setEndValue(QtCore.QRect(200, 0, 586, 370))
        else:
            self.central_widget_animation.setEndValue(QtCore.QRect(0, 0, 586, 370))
        self.central_widget_animation.start()
        
    def lcd_number(self):
        time = datetime.datetime.now()
        formatted_time = time.strftime("%I:%M:%S %p")
        self.lcdNumber.setDigitCount(11)
        # self.lcd_number.set
        self.lcdNumber.display(formatted_time)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS screen_time (
                            app_name TEXT PRIMARY KEY,
                            total_screen_time REAL
                        )''')
        self.conn.commit()

    def track_and_store_screen_time(self):
        active_window = gw.getActiveWindow()
        if active_window is not None:
            app_name = active_window.title

            if app_name != 'Main Window':  # Exclude details about the PyQt window
                if "Google Chrome" in app_name or "Firefox" in app_name or "Microsoft​ Edge" in app_name:
                    tab_name = self.get_browser_tab_name(active_window)
                elif "Visual" in app_name:
                    tab_name = "Visual Studio"
                else:
                    tab_name = app_name

                cursor = self.conn.cursor()
                cursor.execute("SELECT total_screen_time FROM screen_time WHERE app_name=?", (tab_name,))
                row = cursor.fetchone()

                if row:
                    total_time = row[0] + 1  # Update every second
                    cursor.execute("UPDATE screen_time SET total_screen_time=? WHERE app_name=?", (total_time, tab_name))
                else:
                    cursor.execute("INSERT INTO screen_time (app_name, total_screen_time) VALUES (?, ?)", (tab_name, 1))

                self.conn.commit()

    def get_browser_tab_name(self, window):
        title = window.title
        
        if " - Google Chrome" in title:
            tab_name = title.split(" - Google Chrome")[0]
            if "- YouTube" in tab_name:
                tab_name = "YouTube" 
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram" 
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"    
            return tab_name
        elif " - Mozilla Firefox" in title:
            tab_name = title.split(" - Mozilla Firefox")[0]
            if "- YouTube" in tab_name:
                tab_name = "YouTube" 
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram" 
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"      
            return tab_name
        elif "Edge" in title:
            tab_name = title.split(" - Microsoft Edge")[0]
            if "- YouTube" in tab_name: 
                tab_name = "YouTube" 
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram" 
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"       
            return tab_name
        elif "- Visual Studio Code" in title:
                title="Visual Studio Code"
                return title
        else:
            return title    

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

    def update_data_and_plot(self):
        self.track_and_store_screen_time()
        self.plot_graph()

    def plot_graph(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM screen_time WHERE app_name != 'Application Monitor' ORDER BY total_screen_time DESC LIMIT 5")
        data = cursor.fetchall()

        apps = [row[0] for row in data]
        times = [row[1] for row in data]

        formatted_times = [self.format_time(time) for time in times]

        # Close all previous figures
        plt.close('all')

        fig, ax = plt.subplots(figsize=(8, 9))  # Larger figure size
        bars = ax.bar(apps, times, color='skyblue')
        ax.set_xlabel('Tabs/Applications', fontsize=10)
        ax.set_ylabel('Total Screen Time', fontsize=10)  # Adjusted font size for y-label
        ax.set_title('Top Tabs/Applications by Total Screen Time', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=10)  # Adjusted font size for x-ticks
        plt.yticks(fontsize=10)  # Adjusted font size for y-ticks

        # Annotate bars with total time spent
        for bar, time in zip(bars, formatted_times):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{time}', ha='center', va='bottom', fontsize=12)

        plt.tight_layout()

        # Clear the previous layout
        for i in reversed(range(self.bar_graph_layout.count())):
            self.bar_graph_layout.itemAt(i).widget().setParent(None)

        # Embed the Matplotlib figure into the PyQt5 application
        canvas = FigureCanvas(fig)
        self.bar_graph_layout.addWidget(canvas)
        canvas.draw()

  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "Samadhan App"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.setText(_translate("MainWindow", "Report"))
        self.pushButton_5.setText(_translate("MainWindow", "Reminder"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
import icons_rc
    

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
