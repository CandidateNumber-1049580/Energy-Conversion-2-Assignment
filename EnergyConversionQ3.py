import pandas as pd
import numpy as np

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

    # Finding location of first voltage reading greater than zero
    g = list(np.array(volts) > 0).index(True)  

    #Interpolating between readings above and below V = 0 to find current at V = 0
    Jsc = current[g] + ((volts[g]-0)/(volts[g]-volts[g-1]))*(current[g]-current[g-1])
       
    
    # b) Calcualting open circuit voltage, Voc
    # Voc is the voltage across the cell when the current is zero
    
    # Finding location of first current reading greater than zero
    f = list(np.array(current) > 0).index(True)  
    
    #Interpolating between readings above and below I = 0 to find voltage at I = 0
    Voc = volts[f] + ((current[f]-0)/(current[f]-current[f-1]))*(volts[f]-volts[f-1])

        
    # c) Calcualating fill factor, FF
        
    # FF is the ratio of the actual maximum obtainable power (Mp) to the product of the open-circuit voltage and short-circuit current
    # Mp can be found as the area of the largest rectangle which will fit in the IV curve

    #Defining empty vector
    fills = []
    
    # Adding the product of each current and voltage entry to the vector and locating the maximum
    for i in range(0,len(volts)):
        fills.append(volts[i]*current[i])
    Mop = max(fills)
    h = fills.index(Mop)
    
    # Finding the corresponding voltage and current at maximum power, and then calculating maximum power (mW/cm^2)
    Vmp = volts[h]
    Cmp = current[h]
    Mp = abs(Cmp*Vmp)
    
    #Finding theoretical maximum power and calculating the fill factor
    TMp = abs(Jsc*Voc)
    
    FF = Mp/TMp
    
   
    # d) Calculating power conversion efficiency, Pce
    # Pce is the fraction of energy from the sun converted into usable electricity by the cell 
    
    Pce = Mp/(Irrad)
    
    # Printing solutions 
    
    print('3 a) Jsc = ' + str(round(Jsc,4)) + ' mA/cm2 \n  b) Voc = ' + str(round(Voc,4)) + ' V \n  c) FF = ' + str(round(FF,4)) + ' \n  d) Pce = ' + str(round(Pce,4)))

# Calling fucntion       
cell_parameters(volts, current, Irrad)   


