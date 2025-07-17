# Data Access Layer for Music Software
# Ver 0.1
# CURRENTLY NON-FUNCTIONAL
# By Digby Curtis

# For math.pi and math.sin()
import math

# Examples to be used by the Wave class
sample_frequency = {
    "y = sin(pi * x) : 0 < x < 2",
    "y = pi * x - 2 * pi : 2 < x < 3",
    "y = (2 - pi/2) * (x - 3) + pi : 3 < x < 5",
    "y = -4/5 * (x - 5) + 4 : 5 < x < 10"
}

sample_volume = {
    "y = 4/5 * x + 1 : 0 < x < 5",
    "y = 1/2 * x + 5/2 : 5 < x < 7",
    "y = -x + 13 : 7 < x < 10"
}


# The wave class, which bundles volume and frequency across multiple functions (allowing for piecewise)
class Wave():
    # The initialiser, with arrays for volume and frequency (due to )
    def __init__(self, freq_array, vol_array):
        self.frequency = freq_array
        self.volume = vol_array

    # The code for inputting a function and time and outputting a y-value
    def input_function(self, equation, x):
        return("X")


f1 = Wave(sample_frequency, sample_volume)