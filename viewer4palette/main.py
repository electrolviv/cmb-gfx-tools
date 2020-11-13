#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
(C) electro-lviv 2020
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class WidgetPall4Cell(QWidget):

    def __init__(self, r : int):
        super().__init__()

        self.w = int(192/16)
        self.h = int(192/16)

        self.setFixedSize( self.w * 16, self.h * 16)
        self.r = r


    def paintEvent(self, a0: QPaintEvent) -> None:

        qp = QPainter()
        qp.begin(self)

        for j in range(16):
            for i in range(16):

                r = (self.r << 4 ) | self.r
                g = (j << 4) | j
                b = (i << 4) | i

                flagw = (r == g) and (g == b)
                flagw = False

                clr = QColor(r, g, b)
                x, y = i*self.w, j*self.h
                w, h = self.w - 1, self.h - 1
                qp.fillRect(x, y, w, h, clr)
                if flagw:
                    qp.setPen(Qt.white)
                    qp.drawRect(x, y, w-1, h-1)


        qp.end()



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


if __name__ == "__main__":

    # from mods.widget_pixeditor import WidgetPixelEditor

    app = QApplication([])
    wdg = WidgetPalette4Viewer()
    wdg.setMinimumSize(900, 900)
    wdg.show()
    sys.exit(app.exec())

