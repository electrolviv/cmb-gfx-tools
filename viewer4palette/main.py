#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
(C) electro-lviv 2020
"""


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

    from widget_pall4viewer import WidgetPalette4Viewer

    app = QApplication([])

    wdg = WidgetPalette4Viewer()
    wdg.setMinimumSize(900, 900)
    wdg.show()
    sys.exit(app.exec())

