# Presentation Layer
# Ver 0.2.0
# It crashes when it is run

from PyQt5.QtWidgets import *
import business_logic as bl

def screen():
    global window

    app = QApplication([])
    window = QWidget()
    window.resize(1920, 1080)
    for i in range(len(bl.wave_array)):
        manifest_wave(bl.wave_array[i])

    play_button = QPushButton("Play", window)
    play_button.clicked.connect(bl.play)

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