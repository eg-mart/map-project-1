from PyQt5 import QtGui, QtCore, QtWidgets
from get_map_image import get_map_image, get_toponym
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.submit.clicked.connect(self.update_map)

    def setup_ui(self):
        box = QtWidgets.QVBoxLayout()
        coord_input = QtWidgets.QHBoxLayout()

        tmp = QtGui.QPixmap()
        tmp.loadFromData(get_map_image(0, 0))
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(tmp)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setDragMode(self.view.DragMode.ScrollHandDrag)
        box.addWidget(self.view)

        self.lattitude_input = QtWidgets.QLineEdit()
        self.longitude_input = QtWidgets.QLineEdit()

        long_lbl = QtWidgets.QLabel()
        long_lbl.setText('Долгота:')
        coord_input.addWidget(long_lbl)
        coord_input.addWidget(self.longitude_input)

        lat_lbl = QtWidgets.QLabel()
        lat_lbl.setText('Широта:')
        coord_input.addWidget(lat_lbl)
        coord_input.addWidget(self.lattitude_input)

        self.submit = QtWidgets.QPushButton()
        self.submit.setText('Поиск')
        coord_input.addWidget(self.submit)

        box.addLayout(coord_input)

        widget = QtWidgets.QWidget()
        widget.setLayout(box)
        self.setCentralWidget(widget)
    
    def update_map(self):
        tmp = QtGui.QPixmap()
        long = float(self.longitude_input.text())
        lat = float(self.lattitude_input.text())
        tmp.loadFromData(get_map_image(long, lat))
        self.scene.clear()
        self.scene.addPixmap(tmp)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
