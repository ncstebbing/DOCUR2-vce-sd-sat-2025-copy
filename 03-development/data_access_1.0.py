# Data Access Layer for Music Software
# Ver 1.0
# MOSTLY FUNCTIONAL
# By Digby Curtis
# Needs a few minor tweaks and removing the test code but beyond that this is finished (I think)

# For math.pi and math.sin()
import math
import time

# Examples to be used by the Wave class
sample_frequency = [
    "sin(pi * x) : x < 2/4",
    "pi * x - 2 * pi : 2 < x < 3 * pi",
    "(2 - pi/2) * (x - 3) + pi : 3 * pi < x < 15",
    "4/5 * (x - 5) + 16 - 5 * pi : 15 < x"
]

sample_volume = [
    "4/5 * x + 1 : 0 < x < 5",
    "1/2 * x + 5/2 : 5 < x < 7",
    "-x + 13 : 7 < x < 10"
]

wave_list = []

# The wave class, which bundles volume and frequency across multiple functions (allowing for piecewise)
class Wave():
    # The initialiser, with arrays for volume and frequency (due to having multiple for piecewise)
    def __init__(self, freq_array, vol_array):
        self.frequency = freq_array
        self.volume = vol_array

    # Determines where an x value lies within the array of frequencies and volumes
    # Inputs the inputted x value into that function
    def evaluate(self, freq_or_vol, x):

        in_domain = False

        if freq_or_vol == "frequency":
            for i in range(len(self.frequency)):
                domain = self.frequency[i].split(":")[1].split("<")
                equation = self.frequency[i].split(":")[0]
                # In case there is no upper boundary for a function
                if len(domain) < 3 and domain[0] != " x ":
                    domain.append("math.inf")

                # If pi is found within the domain, it is replaced with math.pi (doesn't make the user write math.pi)
                for p in range(len(domain)):
                    if domain[p].find("pi") != -1:
                        domain[p] = domain[p].replace("pi", "math.pi")

                if domain[0] != " x ":
                    if eval(domain[0]) < x and x < eval(domain[2]):
                        in_domain = True
                        if equation.find("x") != -1:
                            equation = equation.replace("x", str(x))
                        if equation.find("pi") != - 1:
                            equation = equation.replace("pi", "math.pi")
                        if equation.find("sin") != -1:
                            equation = equation.replace("sin", "math.sin")
                        if equation.find("cos") != -1:
                            equation = equation.replace("cos", "math.cos")
                        if equation.find("tan") != -1:
                            equation = equation.replace("tan", "math.tan")
                        if eval(equation) > 0:
                            return(eval(equation))
                        else:
                            return(0)
                elif x < eval(domain[1]):
                    in_domain = True
                    if equation.find("x") != -1:
                        equation = equation.replace("x", str(x))
                    if equation.find("pi") != - 1:
                        equation = equation.replace("pi", "math.pi")
                    if equation.find("sin") != -1:
                        equation = equation.replace("sin", "math.sin")
                    if equation.find("cos") != -1:
                        equation = equation.replace("cos", "math.cos")
                    if equation.find("tan") != -1:
                        equation = equation.replace("tan", "math.tan")
                    if eval(equation) > 0:
                        return(eval(equation))
                    else:
                        return(0)
                    
        if freq_or_vol == "volume":
            for i in range(len(self.volume)):
                domain = self.volume[i].split(":")[1].split("<")
                equation = self.volume[i].split(":")[0]

                                # In case there is no upper boundary for a function
                if len(domain) < 3 and domain[0] != " x ":
                    domain.append("math.inf")

                # If pi is found within the domain, it is replaced with math.pi (doesn't make the user write math.pi)
                for p in range(len(domain)):
                    if domain[p].find("pi") != -1:
                        domain[p] = domain[p].replace("pi", "math.pi")

                if domain[0] != " x ":
                    if eval(domain[0]) < x and x < eval(domain[2]):
                        in_domain = True
                        if equation.find("x") != -1:
                            equation = equation.replace("x", str(x))
                        if equation.find("pi") != - 1:
                            equation = equation.replace("pi", "math.pi")
                        if equation.find("sin") != -1:
                            equation = equation.replace("sin", "math.sin")
                        if equation.find("cos") != -1:
                            equation = equation.replace("cos", "math.cos")
                        if equation.find("tan") != -1:
                            equation = equation.replace("tan", "math.tan")
                        if eval(equation) > 0:
                            return(eval(equation))
                        else:
                            return(0)
                elif x < eval(domain[1]):
                    in_domain = True
                    if equation.find("x") != -1:
                        equation = equation.replace("x", str(x))
                    if equation.find("pi") != - 1:
                        equation = equation.replace("pi", "math.pi")
                    if equation.find("sin") != -1:
                        equation = equation.replace("sin", "math.sin")
                    if equation.find("cos") != -1:
                        equation = equation.replace("cos", "math.cos")
                    if equation.find("tan") != -1:
                        equation = equation.replace("tan", "math.tan")
                    if eval(equation) > 0:
                        return(eval(equation))
                    else:
                        return(0)
                    
        if not in_domain:
            # If it isn't in the domain then there shouldn't be frequency or volume
            return(0)
            
    def time_step(self):
        # NOT DONE
        x = time.time() - start_time
        y = self.evaluate("frequency", x)
        coordinates = str(x) + ", " + str(y)
        graph.append(coordinates)


f1 = Wave(sample_frequency, sample_volume)
wave_list.append(f1)

# Setting up time
start_time = time.time()

graph = []

print("Program running.")

for i in range(200):
    f1.time_step()
    time.sleep(1/10)

graph_file = open("music-graph-csv.csv", "wt")

graph_string = ""

for i in range(len(graph)):
    graph_string += (graph[i] + "\n")
 

graph_file.write(graph_string)

graph_file.close()

print("Program done.")


    