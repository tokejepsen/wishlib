from PyQt4 import QtGui, QtCore
import os

file_dir = os.path.dirname(__file__)


def _setStyle(widget, force_style_factory=True):
    if force_style_factory:
        widget.setStyle(QtGui.QStyleFactory().create("plastique"))
    style_file = os.path.join(file_dir, "style",
                              "darkorange.stylesheet")
    with file(style_file) as f:
        stylesheet = f.read()
    widget.setStyleSheet(stylesheet)
    _setIcon(widget)


def _setIcon(widget):
    icon_file = os.path.join(file_dir, "images", "cs-icon.png")
    widget.setWindowIcon(QtGui.QIcon(icon_file))


class QWidget(QtGui.QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        # styling
        _setStyle(self, True)
        # garbage collection
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


class QProgressDialog(QtGui.QProgressDialog):

    def __init__(self, parent, label=""):
        super(QProgressDialog, self).__init__(parent)
        # progress dialog defaults
        self.setWindowTitle("Working...")
        self.setLabelText(label)
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(25)
        self.setCancelButton(None)
        self.setAutoClose(True)
        # styling
        _setStyle(self, False)
        # garbage collection
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


class QMenu(QtGui.QMenu):

    def __init__(self, parent):
        super(QMenu, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        _setStyle(self, False)


class QDialog(QtGui.QDialog):

    def __init__(self, parent):
        super(QDialog, self).__init__(parent)
        # dialog defaults
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.WindowMinimizeButtonHint)
        # styling
        _setStyle(self, True)
        # garbage collection
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


class QMainWindow(QtGui.QMainWindow):

    def __init__(self, parent):
        super(QMainWindow, self).__init__(parent)
        # styling
        _setStyle(self, True)
        # garbage collection
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
