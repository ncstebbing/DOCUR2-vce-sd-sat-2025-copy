# Presentation Layer
# Ver 1.0.0
# It crashes when it is run

from PyQt5.QtWidgets import *
import business_logic as bl

bl.initialise()

def screen():
    global window

    app = QApplication([])
    window = QWidget()
    window.resize(1920, 1080)
    for i in range(len(bl.wave_array)):
        manifest_wave(bl.wave_array[i])

    play_button = QPushButton("Play", window)
    play_button.clicked.connect(bl.play)
    play_button.move(1000,200)

    stop_button = QPushButton("Stop", window)
    stop_button.clicked.connect(bl.stop)
    stop_button.move(700, 200)

    equation = QLineEdit(window)
    equation.resize(150, 50)
    equation.move(1000, 100)

    domain = QLineEdit(window)
    domain.resize(150, 50)
    domain.move(700, 100)

    window.show()
    app.exec_()

# Had to name it something new and manifest is one of the first synonyms for show
def manifest_wave(wave):
    title_button = QLabel(window)
    title_button.setText(wave.name)


def draw_point(x, y):
    placeholder = 0

if __name__ == '__main__':
    screen()