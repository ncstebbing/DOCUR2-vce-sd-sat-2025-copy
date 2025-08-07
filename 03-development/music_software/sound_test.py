# sound test

import winsound
import time
import random

for i in range(50):
    if i != 0:
        time.sleep(1 / i)
        winsound.Beep(750 + 5 * i, int(1000/i))
    else:
        time.sleep(1)
        winsound.Beep(750, 1000)

winsound.Beep(1000, 5000)