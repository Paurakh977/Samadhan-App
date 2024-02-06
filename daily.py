from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation

class daily_report(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 538)
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
        self.frame_4.setMinimumSize(QtCore.QSize(180, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
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
        self.main_body.setStyleSheet("padding:10px;")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.gridLayout = QtWidgets.QGridLayout(self.main_body)
        self.gridLayout.setObjectName("gridLayout")
        self.other_frame = QtWidgets.QFrame(self.main_body)
        self.other_frame.setMaximumSize(QtCore.QSize(450, 16777215))
        self.other_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius:7px;")
        self.other_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.other_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.other_frame.setObjectName("other_frame")
        self.gridLayout.addWidget(self.other_frame, 0, 1, 1, 1)
        self.pie_chart_frame = QtWidgets.QFrame(self.main_body)
        self.pie_chart_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius:7px;")
        self.pie_chart_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pie_chart_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pie_chart_frame.setObjectName("pie_chart_frame")
        self.gridLayout.addWidget(self.pie_chart_frame, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.main_body)
        self.main_body.raise_()
        self.side_menu.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Integrate pie chart into the pie_chart_frame
        self.pie_chart_canvas = FigureCanvas(plt.figure())
        self.gridLayoutPie = QtWidgets.QGridLayout(self.pie_chart_frame)
        self.gridLayoutPie.addWidget(self.pie_chart_canvas)

        self.ani = FuncAnimation(self.pie_chart_canvas.figure, self.update_plot, interval=1000)

    def update_plot(self, i):
        data = self.get_data()

        apps = [row[0] for row in data]
        counts = [row[1] for row in data]

        total_count = sum(counts)
        apps_to_include = []
        counts_to_include = []
        others_count = 0

        for app, count in zip(apps, counts):
            if count / total_count >= 0.05:
                apps_to_include.append(app)
                counts_to_include.append(count)
            else:
                others_count += count

        if others_count > 0:
            apps_to_include.append("Others")
            counts_to_include.append(others_count)

        ax = self.pie_chart_canvas.figure.gca()
        ax.clear()
        ax.pie(counts_to_include, labels=apps_to_include, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('Your Most Used Apps', pad=20)

    def get_data(self):
        conn = sqlite3.connect('app_screen_time.db')
        cursor = conn.cursor()
        cursor.execute("SELECT app_name, COUNT(*) FROM timeline GROUP BY app_name")
        data = cursor.fetchall()
        return data

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

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = daily_report()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

