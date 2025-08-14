# Presentation Layer
# Ver 0.1.0

import sys
from PyQt5 import QtWidgets, uic

def screen():
    app = QApplication([])
    window = QWidget()

    window.show()
    app.exec_()

if __name__ == "__main__":
    screen()