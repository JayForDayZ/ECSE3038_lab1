def parallel(resistors):
    # Check if the list is empty or has less than 2 elements
    if not resistors or len(resistors) < 2:
        return "Invalid input: please provide a list of at least 2 resistors"
    
    # Calculate the reciprocal of the sum of the reciprocals of the resistors
    total_reciprocal = sum([1/resistor for resistor in resistors])
    effective_resistance = 1/total_reciprocal
    print("PARALLEL CALC BELOW")
    print (effective_resistance)

    return effective_resistance
    

parallel([330,1000,2200])

#Potential dividers

def potential_divider(voltage, resistors):
    if not resistors:
        return "invalid: ERROR!!"
    #calculates the total resistance
    total_resistance = sum(resistors)
    #Calculates the voltage drops
    voltage_drops = [voltage*(resistor/total_resistance) for resistor in resistors]
    print("POTENTIAL DIVIDER BELOW")
    print(voltage_drops)

    return voltage_drops

potential_divider(9, [3000,1000])

#Checking Someones body temperature
#Temperature_Check()

def temperature_check(temp, unit):
    if unit not in ['C', 'F']:
        print("Invalid Unit use either C for celcius or 'F' for Fahrenheit")

    elif unit == 'C':
        if temp < 35:
            print("Hyperthermic")
        elif temp > 38:
            print("Hyperthermic")
        else:
            print("Normal temperature")
    elif unit == 'F':
        if temp < 95:
            print ("hyperthermic")
        elif temp > 101:
            print ("hyperthermic")
        else:
            print("Normal Temperature")

temperature_check(36.5, 'C')



    




