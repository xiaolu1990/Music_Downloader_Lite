#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Docstring

"""

__author__ = "Zhangshun.Lu"
__license__ = "MIT License"
__version__ = "0.0.1"

from Application.__main__ import MainWindow
from PySide6 import QtWidgets
import qt_material
import sys

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()

qt_material.apply_stylesheet(window, theme='light_pink.xml')

window.show()

sys.exit(app.exec())
