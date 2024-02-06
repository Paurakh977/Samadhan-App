# -*- coding: utf-8 -*-




# Form implementation generated from reading ui file 'ok.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.








import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas








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
        self.gridLayout.addWidget(self.line_graph_frame, 1, 0, 1, 2)
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
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.setText(_translate("MainWindow", "Report"))
        self.pushButton_5.setText(_translate("MainWindow", "Reminder"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
       
    def setupBarGraphAnimation(self):
        self.conn = sqlite3.connect('app_screen_time.db')
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        layout = QtWidgets.QVBoxLayout(self.bar_graph_frame)  # Create a layout for bar_graph_frame
        layout.addWidget(self.canvas)  # Add the canvas widget to the layout
        self.ani = animation.FuncAnimation(self.fig, self.update_plot, interval=1000)  # Fix method name




        self.setupPieChart()  




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
        cursor.execute("SELECT Day, SUM(total_screen_time) FROM screen_time GROUP BY Day")
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
        self.ax.grid(axis='y', linestyle='--', alpha=0.7)




        # Annotate bars with total screen time
        for x, y, label in zip(days, total_screen_time, formatted_times):
            self.ax.text(x, y, label, ha='center', va='bottom')




    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update_plot, interval=1000)
        plt.show()
       
    def setupPieChart(self):
        self.pie_fig, self.pie_ax = plt.subplots()
        self.pie_canvas = FigureCanvas(self.pie_fig)
        layout = QtWidgets.QVBoxLayout(self.pie_chart_frame)
        layout.addWidget(self.pie_canvas)
        self.pie_ani = animation.FuncAnimation(self.pie_fig, self.update_pie_chart, interval=1000)

    def update_pie_chart(self, i):
        self.pie_ax.clear()
        labels = []
        sizes = []

        cursor = self.conn.cursor()
        cursor.execute("SELECT app_name, SUM(total_screen_time) FROM screen_time GROUP BY app_name")

        data = cursor.fetchall()

        total_time = sum([row[1] for row in data])

        for row in data:
            if row[1] / total_time >= 0.05:
                labels.append(row[0])
                sizes.append(row[1])

        # Plotting 'Others' category for apps with less than 5% usage time
        other_apps_time = total_time - sum(sizes)
        if other_apps_time > 0:
            labels.append('Others')
            sizes.append(other_apps_time)

        self.pie_ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        self.pie_ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        self.pie_ax.set_title('Application Usage Distribution')

        self.pie_canvas.draw()

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Weekly()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())












