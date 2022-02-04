from PyQt5 import QtGui, QtCore, QtWidgets
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = QtWidgets.QWidget()
    ex.show()
    sys.exit(app.exec())
