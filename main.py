from PyQt5 import QtGui, QtCore, QtWidgets
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tmp = QtGui.QPixmap()
    QtGui.QPixmap.load(tmp, 'map.png')
    scene = QtWidgets.QGraphicsScene()
    scene.addPixmap(tmp)
    view = QtWidgets.QGraphicsView(scene)
    view.show()
    sys.exit(app.exec())
