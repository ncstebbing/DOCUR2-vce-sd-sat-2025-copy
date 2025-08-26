# Business Logic
# Ver 2.1.3

import math
import data_access as da
import time
import threading
import winsound

def l_search(array, item):
    found = False
    for i in range(len(array)):
        if array[i] == item:
            found = True
            return(i)
    if found == False:
        return(-1)

def wipe_file(file):
    delete = open(file + ".csv", "wt")
    delete.close()    

def ex_request(func_num):
    func_array = []
    for i in range(func_num):
        valid = False
        while valid == False:
            p_func = input("Please input a function: ")
            save_freq = p_func
            p_func = p_func.lower()
            try:
                if p_func == "n/a":
                    p_func = "0"
                    save_freq = p_func

                if "pi" in p_func:
                    p_func = p_func.replace("pi", "math.pi")

                if "sin" in p_func:
                    p_func = p_func.replace("sin", "math.sin")

                if "cos" in p_func:
                    p_func = p_func.replace("cos", "math.cos")

                if "tan" in p_func:
                    p_func = p_func.replace("tan", "math.tan")            

                p_func = list(p_func)

                for i in range(len(p_func)):
                    # NUMBERx and xNUMBER
                    if p_func[i].isalpha() and p_func[i + 1].isnumeric():
                        p_func.insert(i + 1, "*")
                    elif p_func[i + 1].isalpha() and p_func[i].isnumeric():
                        p_func.insert(i + 1, "*")

                    # NUMBER() and ()NUMBER
                    elif p_func[i].isnumeric() and p_func[i + 1] == "(":
                        p_func.insert(i + 1, "*")
                    elif p_func[i + 1].isnumeric() and p_func[i] == ")":
                        p_func.insert(i + 1, "*")

                    # x() and ()x
                    elif p_func[i] == "x" and p_func[i + 1] == "(":
                        p_func.insert(i + 1, "*")
                    elif p_func[i + 1] == "x" and p_func[i] == ")":
                        p_func.insert(i + 1, "*")

                p_func = "".join(p_func)

                if "x" in p_func:
                    p_func = p_func.replace("x", "((math.e ** 2) / (math.pi ** 2))")

                eval(p_func)
                p_func = save_freq

                p_func = list(p_func)

                for i in range(len(p_func)):
                    # NUMBERx and xNUMBER
                    if p_func[i].isalpha() and p_func[i + 1].isnumeric():
                        p_func.insert(i + 1, "*")
                    elif p_func[i + 1].isalpha() and p_func[i].isnumeric():
                        p_func.insert(i + 1, "*")

                    # NUMBER() and ()NUMBER
                    elif p_func[i].isnumeric() and p_func[i + 1] == "(":
                        p_func.insert(i + 1, "*")
                    elif p_func[i + 1].isnumeric() and p_func[i] == ")":
                        p_func.insert(i + 1, "*")

                    # x() and ()x
                    elif p_func[i] == "x" and p_func[i + 1] == "(":
                        p_func.insert(i + 1, "*")
                    elif p_func[i + 1] == "x" and p_func[i] == ")":
                        p_func.insert(i + 1, "*")

                p_func = "".join(p_func)
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
                    save_domain = p_domain

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

def make_wave(num_freq, num_vol):
    global wave_array
    print("")
    print("Please input the equations and domains for your frequencies.")
    print("")
    frequencies = ex_request(num_freq)
    print("")
    print("Please input the equations and domains for your volumes.")
    print("")
    volumes = ex_request(num_vol)
    if len(wave_array) != 0:
        new_wave = "f" + str(int(wave_array[-1].name.replace("f", "")) + 1)
    else:
        new_wave = "f1"
    wave = da.Wave(new_wave, frequencies, volumes)
    wave_array.append(wave)

def access_store(project):
    global wave_array
    wave_array = []
    project_store = open(project + ".csv", "rt")
    ws = project_store.read()
    project_store.close()

    ws = ws.split("\n")

    for i in range(len(ws)):
        current_line = ws[i].split(",")
        name = current_line[0]
        start_freq = l_search(current_line, "FREQUENCY")
        start_vol = l_search(current_line, "VOLUME")
        end_vol = len(current_line)

        frequencies = []

        for i in range(start_freq + 1, start_vol):
            frequencies.append(current_line[i] + ",")
        
        volumes = []

        for i in range(start_vol + 1, end_vol):
            if i != (end_vol - 1):
                volumes.append(current_line[i] + ",")

        wave = da.Wave(name, frequencies, volumes)
        wave_array.append(wave)

def open_project():
    which_project = input("Which project would you like to open? ")
    #which_project = "wave_store"

    try:
        wp = open(which_project + ".csv", "rt")
        wp.close()
        access_store(which_project)
    except:
        print("That project was not found, please make new waves.")
        wave_array = []
        for i in range(2):
            make_wave(2, 2)
        wipe_file(which_project)
        for i in range(len(wave_array)):
            wave_array[i].save(which_project)

def run_step():
    freq_coords = []
    vol_coords = []
    freq_plot_string = ""
    vol_plot_string = ""

    for i in range(len(wave_array)):
        freq_coords.append(wave_array[i].time_step("frequency", (time.time() - start_time)))
        vol_coords.append(wave_array[i].time_step("volume", (time.time() - start_time)))

    for i in range(len(freq_coords)):
        freq_plot_string += (freq_coords[i] + "\n")
    for i in range(len(vol_coords)):
        vol_plot_string += (vol_coords[i] + "\n")

    freq_plot = open("freq_plot.csv", "at")
    freq_plot.write(freq_plot_string)
    freq_plot.close()

    vol_plot = open("vol_plot.csv", "at")
    vol_plot.write(vol_plot_string)
    vol_plot.close()

    for i in range(len(freq_coords)):
        freq_at_t = freq_coords[i].split(",")[1]
        vol_at_t = vol_coords[i].split(",")[1]

        freq_at_t = freq_at_t.strip()
        vol_at_t = vol_at_t.strip()

        freq_at_t = freq_at_t.split("\n")

        vol_at_t = round(float(vol_at_t))
        
        for i in range(len(freq_at_t)):
            freq_at_t[i] = round(float(freq_at_t[i]))
            play_sound(freq_at_t[i], vol_at_t)

def play_sound(freq, vol):
    def play_nosleep():
        if freq > 37 and freq < 10000:
            winsound.Beep(freq, 900)
    audio_thread = threading.Thread(target = play_nosleep)
    audio_thread.start()

def initialise():
    global playing_sound

    open_project()

    wipe_file("freq_plot")
    wipe_file("vol_plot")

    playing_sound = False

def stop():
    global playing_sound
    playing_sound = False

# Input may not go below 1000
def play():
    global playing_sound
    global start_time

    playing_sound = True

    time_array = []
    error_string = ""

    # Setting up time
    start_time = time.time()

    while playing_sound:
        time_array.append(time.time() - start_time)
        run_step()
        time_array.append(time.time() - start_time)
        error_string += str(time.time() - start_time) + "," + str(time_array[-1] - time_array[-2]) + "\n"
