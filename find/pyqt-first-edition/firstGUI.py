import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys
import find


def main():

    app = QApplication(sys.argv)
    form = QMainWindow()
    window = find.Ui_MainWindow()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec_())
if __name__ == '__main__':

    main()
