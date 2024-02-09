from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys

class TableExample(QWidget):
    def __init__(self, list1, list2):
        super().__init__()

        self.setWindowTitle('Lists in Table Example')
        self.setGeometry(100, 100, 400, 200)

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2'])

        # Set the border and grid to 0
        self.table_widget.setStyleSheet("QTableWidget { border: 0; gridline-color: white; }")

        self.populate_table(list1, list2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def populate_table(self, list1, list2):
        # Assuming lists are of the same length
        if len(list1) != len(list2):
            print("Error: Lists must have the same length.")
            return

        # Set row count based on the length of the lists
        self.table_widget.setRowCount(len(list1))

        for row, (item1, item2) in enumerate(zip(list1, list2)):
            item1_widget = QTableWidgetItem(str(item1))
            item2_widget = QTableWidgetItem(str(item2))

            self.table_widget.setItem(row, 0, item1_widget)
            self.table_widget.setItem(row, 1, item2_widget)

def main():
    app = QApplication(sys.argv)

    # Example lists
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c', 'd']

    window = TableExample(list1, list2)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
