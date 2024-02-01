from PyQt5 import QtCore, QtWidgets
import psutil
from pyqtgraph import PlotWidget, mkPen
from collections import deque
import platform
import sys

# GLOBALS
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class CPU_details(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CPU_details, self).__init__(parent)
        self.graph_widget = PlotWidget(title="CPU and RAM percent")
        self.setCentralWidget(self.graph_widget)

        self.cpu_percent = 0
        self.ram_percent = 0
        self.timestamp = 0
        self.graph_lim = 15
        self.deque_timestamp = deque([], maxlen=self.graph_lim + 20)
        self.deque_cpu = deque([], maxlen=self.graph_lim + 20)
        self.deque_ram = deque([], maxlen=self.graph_lim + 20)
        self.plot_cpu = None
        self.plot_ram = None

        self.current_timer_system_stat = QtCore.QTimer()
        self.current_timer_system_stat.timeout.connect(self.get_system_stat_percent)
        self.current_timer_system_stat.start(1000)

    def get_system_stat_percent(self):
        self.cpu_percent = psutil.cpu_percent()
        self.ram_percent = psutil.virtual_memory().percent
        self.update_usage()

    def update_usage(self):
        self.timestamp += 1

        self.deque_timestamp.append(self.timestamp)
        self.deque_cpu.append(self.cpu_percent)
        self.deque_ram.append(self.ram_percent)

        cpu_list = list(self.deque_cpu)
        ram_list = list(self.deque_ram)

        self.update_graph(cpu_list, ram_list)

    def update_graph(self, cpu_list, ram_list):
        if self.timestamp > self.graph_lim:
            x_min = min(self.deque_timestamp)
            x_max = max(self.deque_timestamp)
            x_range = [max(0, x_max - self.graph_lim), max(0, x_max)]
            self.graph_widget.setXRange(min(x_range), max(x_range))

        y_max = max(max(cpu_list), max(ram_list))
        self.graph_widget.setYRange(0, y_max + 10)

        self.set_plotdata(data_x=self.deque_timestamp, data_y_cpu=cpu_list, data_y_ram=ram_list)

    def set_plotdata(self, data_x, data_y_cpu, data_y_ram):
        if self.plot_cpu is None:
            self.plot_cpu = self.graph_widget.plot(pen=mkPen(color=(85, 170, 255), width=3), name="CPU")
        if self.plot_ram is None:
            self.plot_ram = self.graph_widget.plot(pen=mkPen(color=(255, 0, 127), width=3), name="RAM")

        self.plot_cpu.setData(data_x, data_y_cpu)
        self.plot_ram.setData(data_x, data_y_ram)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CPU_details()
    window.show()
    sys.exit(app.exec_())
