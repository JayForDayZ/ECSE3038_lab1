#1. Number one entailed the function parallel. This calculates the effective resistance of a network of 2 or more resistors. The function takes a list of numbers as input, which represent the individual resistor values.

When resistors are connected in parallel, the total resistance of the circuit is calculated using the reciprocal of the sum of the reciprocals of the individual resistors. Mathematically, this can be represented as:

1/Rt = 1/R1 + 1/R2 + 1/R3 + ... + 1/Rn

The function uses this formula to calculate the total resistance of the circuit, using the sum() function to calculate the sum of the reciprocals of the individual resistors, and then taking the reciprocal of that sum to get the total resistance.
#####################################

#2. Number two entailed the function Potential divider. This calculatesthe voltage drop across each resistor in a series circuit, given a voltage supply value and a list of resistance values.

The function takes two arguments:

    A number that represents the voltage supply value
    A list of numbers that represent the resistance values of the resistors connected in series

When resistors are connected in series, the voltage across each resistor is proportional to its resistance. Mathematically, this can be represented as:

Vr = (Vsupply * Rr) / Rt

Vr is across the resistor 
Rr is is the resistance of the resistor 
Rt is the total resistance of the circuit
Vsupply is the supply voltage 

#3. The 3rd function was to actually this was used to create parameters for a persons body temperatur in both Celcius and fahrenheit. The function uses an if-else loop to check the temperature against the normal range for the given unit of temperature. The normal range for body temperature is 98.6°F (37°C) but it can vary from person to person so you may use other limits as well. The function takes two arguments the temperature as well as the unit which is either 'C' or 'F'.

########################################################################################
The jokes on you hahah :)