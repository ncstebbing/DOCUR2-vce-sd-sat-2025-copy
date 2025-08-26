# Presentation Layer
# Ver 1.1.0
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
        manifest_wave(bl.wave_array[i], i)

    play_button = QPushButton("Play", window)
    play_button.clicked.connect(bl.play)
    play_button.move(1000,200)

    stop_button = QPushButton("Stop", window)
    stop_button.clicked.connect(bl.stop)
    stop_button.move(700, 200)

    # Draws a graph over 10 seconds
    for f in range(len(bl.wave_array)):
        for i in range(1000):
            draw_point(i * 0.01, bl.wave_array[f].evaluate("frequency", i * 0.01))

    window.show()
    app.exec_()

# Had to name it something new and manifest is one of the first synonyms for show
def manifest_wave(wave, num):
    title_button = QLabel(window)
    title_button.setText(wave.name + "(x)")
    title_button.resize(200, 200)
    title_button.move(50, 25 + 100 * num)

    equation = QLineEdit(window)
    equation.resize(150, 50)
    equation.move(100, 100 + 100 * num)

    domain = QLineEdit(window)
    domain.resize(150, 50)
    domain.move(300, 100 + 100 * num)


def draw_point(x, y):
    point = QLabel(window)
    point.setText(".")
    point.resize(100, 100)

    x_dilate = 100
    y_dilate = -0.5

    x_translate = 750
    y_translate = 600

    for i in range(len(y)):
        point.move(int(float(x) * x_dilate) + x_translate, int(float(y[i]) * y_dilate) + y_translate)

if __name__ == '__main__':
    screen()