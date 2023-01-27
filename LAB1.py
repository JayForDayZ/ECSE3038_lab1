def parallel(resistors):
    if not resistors or len(resistors)<2:
        return "Error!!"

    reciprocal = sum([1/res for res in resistors])
    resistance = 1/reciprocal
    return resistance
    
    print(parallel([330,400,200]))
