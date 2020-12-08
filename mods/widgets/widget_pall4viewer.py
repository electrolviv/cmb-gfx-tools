from PyQt5.QtWidgets import QWidget, QGridLayout

from widget_pall4cell import WidgetPall4Cell


class WidgetPalette4Viewer(QWidget):

    def __init__(self):
        super().__init__()

        self.arr = []
        for i in range(16):
            self.arr.append(WidgetPall4Cell(i))

        self.setLayout(self.genlayout())
        self.setWindowTitle("4:4:4 Palette")


    def genlayout(self):
        lay = QGridLayout()

        for j in range(4):
            for i in range(4):
                idx = (j*4) + i
                lay.addWidget( self.arr[idx], j, i)

        return lay