# Business Logic
# Ver 0.2.0

import math
import data_access_1_2_1 as da

def ex_request():
    func_array = []
    for i in range(2):
        valid = False
        while valid == False:
            p_func = input("Please input a function: ")
            save_freq = p_func
            p_func = p_func.lower()
            try:
                if p_func == "n/a":
                    p_func = "0"

                if "pi" in p_func:
                    p_func = p_func.replace("pi", "math.pi")

                if "sin" in p_func:
                    p_func = p_func.replace("sin", "math.sin")

                if "cos" in p_func:
                    p_func = p_func.replace("cos", "math.cos")

                if "tan" in p_func:
                    p_func = p_func.replace("tan", "math.tan")

                if "x" in p_func:
                    p_func = p_func.replace("x", "((math.e ** 2) / (math.pi ** 2))")

                eval(p_func)
                p_func = save_freq
                valid = True
            except:
                if valid == False:
                    print("Please try again.")

        valid = False
        while valid == False:
            p_domain = input("Please input the domain for your function: ")
            save_domain = p_domain
            p_domain = p_domain.lower()
            try:
                if "n/a" in p_domain:
                    p_domain = "0 < x < math.inf"

                if p_domain in "pi":
                    p_domain.replace("pi", "math.pi")

                p_domain.split("<")
                if len(p_domain) < 3 and p_domain[0] != " x ":
                    p_domain.append("math.inf")

                if len(p_domain) < 3 and p_domain[0] == " x ":
                    p_domain.insert("0", 0)

                p_domain[0] < p_domain[2]
                p_domain = save_domain
                valid = True
            except:
                if valid == False:
                    print("Please try again.")

        func_array.append(p_func + " : " + p_domain)
    return(func_array)

wave_array = []

def make_wave():
    print("Please input the equations and domains for your frequencies.")
    print("")
    frequencies = ex_request()
    print("Please input the equations and domains for your volumes.")
    print("")
    volumes = ex_request()
    if len(wave_array) != 0:
        new_wave = "f" + str(int(wave_array[-1].replace("f", "")) + 1)
    else:
        new_wave = "f1"
    wave = da.Wave(new_wave, frequencies, volumes)
    wave_array.append(wave)

for i in range(2):
    make_wave()


