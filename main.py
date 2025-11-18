userinput = input("kilometers or miles")
if userinput == "k":
    userinput = float(input("How many kilometers do you want to go?"))
    convert = userinput * 0.621371 
    print("That's", convert, "miles")
    time = userinput/15 * 60
    print("your time in minutes: ", time)
    compA = time * 0.15 + 1
    compB = 2.50 + (.12 * (time - 5))
    compC = time * 0.06 + 5 
    print(compA)
    print(compB)
    print(compC)
    if compA < compB and compA < compC:
        print("use company A, the cost is: ", compA)
    elif compB < compC and compB < compA:
        print("use company B, the cost is: ", compB)
    elif compC < compA and compC < compB:
        print("use company C, the cost is: ", compC)
elif userinput == "m":
    userinput = float(input("How many miles do you want to go?"))
    convert2 = userinput * 1.60934
    print("That's", convert2, "kilometers")
    time = userinput/15 * 60
    print("your time in minutes: ", time)
    compA = time * 0.15 + 1
    compB = 2.50 + (.12 * (time - 5))
    compC = time * 0.06 + 5 
    print(compA, "company A")
    print(compB, "company B")
    print(compC, "company C")
    if compA < compB and compA < compC:
        print("use company A, the cost is: ", compA)
    elif compB < compC and compB < compA:
        print("use company B, the cost is: ", compB)
    elif compC < compA and compC < compB:
        print("use company C, the cost is: ", compC)
