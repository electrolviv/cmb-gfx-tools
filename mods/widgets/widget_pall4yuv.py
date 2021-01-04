from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtGui import QPaintEvent, QPainter, QColor
from PyQt5.QtWidgets import QWidget


class WidgetPalette4YUV(QWidget):

    def __init__(self):
        super(WidgetPalette4YUV, self).__init__()
        self.setFixedSize(QSize(800, 800))


    def paintEvent(self, a0: QPaintEvent):

        w = int(self.width() / 16)
        h = int(self.height() / 16)

        qp = QPainter()
        qp.begin(self)

        for j in range(16):
            for i in range(16):

                # Y = 128
                # U = 56 + (i * 9.5)
                # V = 38 + (j * 12)

                Y = int(128)
                U = int(60 + (i * 9))
                V = int(60 + ((15-j) * 10.2))

                r = Y + 1.4075 * (V - 128)
                g = Y - 0.3455 * (U - 128) - (0.7169 * (V - 128))
                b = Y + 1.7790 * (U - 128)

                clr = QColor( int(r), int(g), int(b))

                x, y = i * w, j * h

                qp.fillRect(x, y, w - 1, h - 1, clr)

                qp.setPen(Qt.white)
                qp.drawRect(x, y, w, h)

                qp.setPen(Qt.black)

                th = 12
                qp.drawText(QPoint(x+4, th + y +  4), "Y:%i" % Y )
                qp.drawText(QPoint(x+4, th + y + 18), "U:%i" % U )
                qp.drawText(QPoint(x+4, th + y + 32), "V:%i" % V )


        qp.end()


if __name__ == "__main__":

    import sys
    import os
    from PyQt5.QtWidgets import QApplication

    arr = [ "", "mods", "mods/widgets" ]
    realpath = os.path.realpath(__file__)
    rootpath = os.path.dirname(os.path.dirname(realpath))

    for pth in arr:
        rpath = rootpath + "/" + pth
        print(rpath)
        sys.path.append(rpath)

    app = QApplication([])

    wdg = WidgetPalette4YUV()
    wdg.show()
    sys.exit(app.exec())
