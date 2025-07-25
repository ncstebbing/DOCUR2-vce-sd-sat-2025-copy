# Business Logic
# Ver 0.1.0

frequencies = []

volumes = []

for i in range(4):
    invalid = False
    while invalid == False:
        p_freq = input("Please input a function: ")
        save_freq = p_freq
        try:
            if "pi" in p_freq:
                p_freq = p_freq.replace("pi", "math.pi")
            if "sin" in p_freq:
                print("FOUND")
                p_freq = p_freq.replace("sin", "math.sin")
            if "cos" in p_freq:
                p_freq = p_freq.replace("cos", "math.cos")
            if "tan" in p_freq:
                p_freq = p_freq.replace("pi", "math.tan")
            if "x" in p_freq:
                p_freq = p_freq.replace("x", "(math.e ** 2 / math.pi ** 2)")
            eval(p_freq)
            p_freq = save_freq
            invalid = True
        except:
            print("Please try again.")

    invalid = False
    while invalid == False:
        p_domain = input("Please input the domain for your function:")
        save_domain = p_domain
        try:
            if p_domain.find("pi"):
                p_domain.replace("pi", "math.pi")
            p_domain.split("<")
            if len(p_domain) < 3 and p_domain[0] != " x ":
                p_domain.append("math.inf")
            if len(p_domain) < 3 and p_domain[0] == " x ":
                p_domain.insert("0", 0)
            p_domain[0] < p_domain[2]
            p_domain = save_domain
            invalid = True
        except:
            print("Please try again.")

    frequencies.append(p_freq + " : " + p_domain)

for i in range(4):
    p_vol = input("Please input a function: ")
    p_domain = input("Please input the domain for your function: ")
    volumes.append(p_vol + " : " + p_domain)
