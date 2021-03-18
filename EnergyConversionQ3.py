import pandas as pd
import numpy as np
from scipy import interpolate

# importing current-voltage excel data into dataframe

data = pd.read_excel('GaAs Solar Cell IV.xlsx')

#Splitting data into two vectors 

volts = data['Voltage (V)']
current = data['Current density (mA/cm2)']

# Defining irradiation on cell

Irrad = 100 # mW/cm2


# Defining function 

def cell_parameters(volts, current, Irrad):
    
    
    # a) Calculating short circuit current density, Jsc
    # Jsc is the current/area through the cell when the voltage across it is zero

    #Interpolating between readings to find current at V = 0
    j = interpolate.interp1d(volts, current, kind = 'cubic') 
    Jsc = float(j(0))
    
       
    
    # b) Calcualting open circuit voltage, Voc
    # Voc is the voltage across the cell when the current is zero
    
    #Interpolating between readings to find voltage at I = 0    
    k = interpolate.interp1d(current, volts, kind = 'cubic') 
    Voc = float(k(0))
    

        
    # c) Calcualating fill factor, FF     
    # FF is the ratio of the actual maximum obtainable power (Mp) to the product of the open-circuit voltage and short-circuit current
    # Mp can be found as the area of the largest rectangle which will fit in the IV curve

    #Defining empty maximum power vector
    fills = []
    
    # Adding the product of each current and voltage entry to the vector and locating the maximum
    for i in range(0,len(volts)):
        fills.append(volts[i]*-current[i])
    Mop = max(fills)
    
    h = fills.index(Mop)
    
    # Finding the corresponding voltage and current at maximum power, and then calculating maximum power (mW/cm^2)
    Vmp = volts[h]
    Cmp = current[h]
    
    
    #Finding theoretical maximum power and calculating the fill factor
    TMp = abs(Jsc*Voc)
    
    FF = Mop/TMp
    
    # d) Calculating power conversion efficiency, Pce
    # Pce is the percentage of energy from the sun converted into usable electricity by the cell 
    
    Pce = Mop/(Irrad)*100
    
    # Printing solutions 
       
    print('3 a) Jsc = ' + str(round(Jsc,4)) + ' mA/cm2 \n  b) Voc = ' + str(round(Voc,4)) + ' V \n  c) FF = ' + str(round(FF,4)) + ' \n  d) Pce = ' + str(round(Pce,4)) + ' %')

# Calling fucntion       
cell_parameters(volts, current, Irrad)   


