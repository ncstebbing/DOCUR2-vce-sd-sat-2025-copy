# Presentation Layer
# Ver 0.1.0
from PyQt5.QtWidgets import *

def screen():
    app = QApplication([])
    window = QWidget()

    window.show()
    app.exec_()

if __name__ == "__main__":
    screen()