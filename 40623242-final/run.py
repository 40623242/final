import sys
from PyQt5 import QtWidgets
from ui.dialog import Dialog

app = QtWidgets.QApplication(sys.argv)
win = Dialog()
win.show()
sys.exit(app.exec())
