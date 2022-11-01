def bRange(start,stop,step,modifier="x"):
    x = start
    flags = []
    result = []

    while x <= stop:
        try:
            temp = eval(modifier)
        except ZeroDivisionError:
            temp = "ZeroDivisonError"
            flags.append(temp + " for " + str(x))
        
        result.append(temp)
        x += step

    print(flags)
    return result
