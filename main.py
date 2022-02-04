from PyQt5 import QtGui, QtCore, QtWidgets
from get_map_image import get_map_image
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tmp = QtGui.QPixmap()
    tmp.loadFromData(get_map_image(input()))
    scene = QtWidgets.QGraphicsScene()
    scene.addPixmap(tmp)
    view = QtWidgets.QGraphicsView(scene)
    view.show()
    sys.exit(app.exec())
