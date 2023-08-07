import sys
from PyQt5.QtWidgets import QTableView, QWidget, QApplication, QVBoxLayout, QDesktopWidget, QAbstractItemView, \
    QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.model = None
        self.init_data()
        self.init_ui()
        self.connect()

    def init_data(self):
        max_row = 3
        max_col = 4
        self.model = QStandardItemModel(max_row, max_col)
        for row in range(0, max_row):
            for col in range(0, max_col):
                value = str(row) + '----' + str(col)
                self.model.setItem(row, col, QStandardItem(value))

        col_titles = ['列标题1', '列标题2', '列标题3', '列标题4']
        self.model.setHorizontalHeaderLabels(col_titles)

    def init_ui(self):
        self.setWindowTitle('QTableView Test')

        top_layout = QVBoxLayout()

        table_view_layout = QVBoxLayout()
        self.table_view = QTableView()
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_view.setModel(self.model)
        table_view_layout.addWidget(self.table_view)
        top_layout.addLayout(table_view_layout)

        self.setLayout(top_layout)

        self.table_view.setCurrentIndex(self.model.index(2, 0))

    def connect(self):
        self.table_view.clicked.connect(self.table_view_clicked)

    def table_view_clicked(self, index):
        table_row = index.row()
        item = self.model.item(table_row, 0)
        vale = item.text()
        QMessageBox.information(self, '提示', '单击{value}'.format(value=vale))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())