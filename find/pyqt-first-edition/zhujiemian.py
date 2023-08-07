# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhujiemian.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
from no_pyqt import find



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")

        self.horizontalLayout.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.lineEdit.returnPressed.connect(lambda:self.updateit())
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def updateit(self):
        context=self.lineEdit.text()
        lines,files,filedata,dirdata=find.search(context)
        # 设置数据层次结构，4行4列
        self.model = QStandardItemModel(lines, 3)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['文件名', '绝对路径', '标签'])

        # 添加数据
        for row in range(files):
            for column in range(3):
                item = QStandardItem(str(filedata[row][column]))
                # 设置每个位置的文本值
                self.model.setItem(row, column, item)

        for row in range(lines-files):
            for column in range(2):
                item = QStandardItem(str(dirdata[row][column]))
                # 设置每个位置的文本值
                self.model.setItem(row+files, column, item)
        # QTableView 绑定 数据
        self.tableView.setModel(self.model)
        # 水平方向标签拓展剩下的窗口部分，填满表格
        self.tableView.horizontalHeader().setStretchLastSection(True)
        # 水平方向，表格大小拓展到适当的尺寸
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)






def main():

    app = QApplication(sys.argv)
    form = QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec_())

main()