import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import maps

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        superlayout = QHBoxLayout()

        layout = QFormLayout()

        self.label = QLabel()
        pixmap = QPixmap('image\\mainmap-resized.png')
        self.label.setPixmap(pixmap)

        superlayout.addWidget(self.label)
        superlayout.addStretch()

        self.s_cb = QComboBox()
        self.t_cb = QComboBox()
        self.btn = QPushButton("시작")
        self.route = QLabel()

        bldlist = sorted(list(maps.building_number.keys()))

        self.s_cb.addItems(bldlist)
        self.t_cb.addItems(bldlist)

        self.btn.clicked.connect(self.navigate)

        layout.addRow("출발", self.s_cb)
        layout.addRow("도착", self.t_cb)
        layout.addRow(self.btn)
        layout.addRow(self.route)

        superlayout.addLayout(layout)

        self.setLayout(superlayout)
        self.setWindowTitle("Hanyang University Navigator")

    def navigate(self):
        src = maps.building_number[self.s_cb.currentText()]
        tgt = maps.building_number[self.t_cb.currentText()]
        rtn = maps.path_search(src, tgt)

        for i in range(len(rtn)): rtn[i] = str(rtn[i])
        way = " > ".join(rtn)
        self.route.setText(way)


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()