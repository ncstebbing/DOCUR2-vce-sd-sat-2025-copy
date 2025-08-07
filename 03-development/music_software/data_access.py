# Data Access Layer for Music Software
# Ver 1.3.0
# MOSTLY FUNCTIONAL
# By Digby Curtis
# Needs a few minor tweaks and removing the test code but beyond that this is finished (I think)

# For math.pi and math.sin()
import math

wave_list = []

# The wave class, which bundles volume and frequency across multiple functions (allowing for piecewise)
class Wave():
    # The initialiser, with arrays for volume and frequency (due to having multiple for piecewise)
    def __init__(self, name, freq_array, vol_array):
        self.name = name
        self.frequency = freq_array
        self.volume = vol_array
        self.graph = []

        for i in range(len(self.frequency)):
            self.frequency[i] = self.frequency[i].strip(",")

        for i in range(len(self.volume)):
            self.volume[i] = self.volume[i].strip(",")

    # Determines where an x value lies within the array of frequencies and volumes
    # Inputs the inputted x value into that function
    def evaluate(self, freq_or_vol, x):

        in_domain = False

        if freq_or_vol == "frequency":

            # Has to repeat for every item to check all of the domains.
            for i in range(len(self.frequency)):

                # Accesses the domain and equation parts of each function in the frequency array
                domain = self.frequency[i].split(":")[1].split("<")
                equation = self.frequency[i].split(":")[0]

                # In case there is no upper boundary for a function
                if len(domain) < 3 and domain[0] != " x ":
                    domain.append("math.inf")

                # If pi is found within the domain, it is replaced with math.pi (doesn't make the user write math.pi)
                for p in range(len(domain)):
                    if domain[p].find("pi") != -1:
                        domain[p] = domain[p].replace("pi", "math.pi")

                # If the x value is within the domain of one of the functions, it will edit the equation to be possible to evaluate, then return it evaluated.
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
            
    def time_step(self, freq_or_vol, current_time):
        
        x = current_time
        if freq_or_vol == "frequency":
            y = self.evaluate("frequency", x)
        elif freq_or_vol == "volume":
            y = self.evaluate("volume", x)
        coordinates = str(x) + ", " + str(y)
        return(coordinates)

    # Used to save the volume and frequency properties into a csv (to be accessed and written back into its properties when reopened)
    def save(self, csv):
        csv = open(csv + ".csv", "at")
        freq_string = ""
        vol_string = ""
        for i in range(len(self.frequency)):
            freq_string += self.frequency[i] + ","

        for i in range(len(self.volume)):
            vol_string += self.volume[i] + ","

        csv.write(self.name + ",FREQUENCY," + freq_string + "VOLUME," + vol_string + "\n")
        csv.close()