# Andrea M. Stojanovski
# Project 2 Type 2
# Q and A interface

def QandA():
    print("Information on security assumptions of Digital Signature Schemes:")
    print("Hashed RSA: RSA + Random oracle")
    print("Schnorr: DL")
    print("DSA: Related to DL over ZP")
    print("EC DSA: Related to DL over EC")
    print("Tree-based Lamport: One-way Hash Functions")
    print("El-gamal: Related to Dl over EC")
    print("DSS: ")

    schemes = { # dictionary of schemes locally to make sure they are initialized to 0
        "Hashed RSA" : 0,
        "Schnorr": 0,
        "DSA": 0,
        "EC DSA": 0,
        "Tree-based Lamport": 0,
        "El-Gamal": 0,
        "DSS": 0,
        "ED DSA": 0}

    scheme_list = ["Hashed RSA",
                   "Schnorr",
                   "DSA",
                   "EC DSA",
                   "Tree-based Lamport",
                   "El-Gamal",
                   "DSS",
                   "ED DSA"]

    def check_list(scheme_list):
        if len(scheme_list) == 1:
            print("Use " + scheme_list)
            for i in sorted(schemes):
                print("Alternative options (in order of most preferred)")
                print((i, schemes[i]), end = "")

    # ask about runtime
    print("Importance of runtime efficiency of scheme:")
    print("A. Not important / Unsure")
    print("B. Important")
    print("C. Very important")
    runtime = input()

    if runtime == "C":
        schemes["EC DSA"] += 1 # very efficient
        schemes["Tree-based Lamport"] += 1 # very efficient
        schemes["El-Gamal"] -= 1 # less efficient

        for i in range(0,len(scheme_list)-1):
            if scheme_list[i] != "EC DSA" and scheme_list[i] != "Tree-based Lamport":
                scheme_list.pop(i) # remove those that do no apply
        check_list()
    elif runtime == "B":
        schemes["El-gamal"] -= 1  # less efficient
        # don't add point for inefficient
        for i in range(0,len(scheme_list)-1):
            if scheme_list[i] == "El-gamal":
                scheme_list.pop(i) # remove those that do no apply
        check_list()
    # elif runtime = "A": do nothing
    # elif runtime = "D": do nothing

    # ask about key and signature length
    print("Select importance of short key and signature length:")
    print("A. Important")
    print("B. Not a priority / Unsure")
    keyandsig = input()

    if keyandsig == "A":
        schemes["DSS"] += 1  # very short
        schemes["Tree-based Lamport"] += 1  # very short
        schemes["ED DSA"] += 1  # very short

        for i in range(0,len(scheme_list)-1):
            if scheme_list[i] != "EC DSA" and scheme_list[i] != "Tree-based Lamport" and scheme_list[i] != "DSS":
                scheme_list.pop(i)  # remove those that do no apply
        check_list()
    # elif keyandsig = "B": do nothing

    print("Importance of quantum computing safety:")
    print("A. Important")
    print("B. Not important / Unsure")
    quantum = input()

    if quantum == "A":
        schemes["Schnorr"] += 1  # safe

        for i in range(0,len(scheme_list)-1):
            if scheme_list[i] != "Schnorr":
                scheme_list.pop(i)  # remove those that do no apply
        check_list()
    # elif quantum = "B": do nothing

QandA()
"""
while len(scheme_list) > 1:
    # keep asking more
    if len(scheme_list) = 1:
        print(scheme_list[0] + " fits the given specification best.")
        print("Alternative options (in order of most preferred)")
        # order schemes by points
        for each in scheme: # print the shcemes in order of most points
            if each.key == scheme_list[0]: # the selected method
                # return nothing
            else:
                print(scheme)

# method with minium numbeer questions asked

"""
