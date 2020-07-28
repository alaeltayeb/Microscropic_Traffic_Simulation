# -*- coding: utf-8 -*-

import math
import random as random
import matplotlib.pyplot as plt




#inv CDF(U) = -log(1-U)
"""
def typefunction():
    list = ["Car", "ACC"];
    ind=0
    if random.random()>0.5:
        ind=1
    return list[ind]
"""    
                  

def GenerationACCCar(rate, maxtime, routeid="r1"):
    tdep = 0.0
    seqvi = []
    IDveh = 0 # ID = typeArry[]
    while tdep <= maxtime:

        tint = -math.log(random.random())/rate
        tdep = tdep + tint
        IDveh = IDveh + 1
        veh_type= "Car"#typefunction()
        seqvi.append('<vehicle depart="{}" id="veh{}" route="{}" type="{}"/>'.format(tdep, IDveh, routeid, veh_type))    
    return seqvi

print GenerationACCCar(0.0833, 36000,"r1")


def writeToFile(strList, filename):
    with open(filename, 'a') as filehandle:
        for str in strList:
            filehandle.write(str + '\n')

      


if __name__ == "__main__":
    # Example of usage

    seq1 = GenerationACCCar(0.0833, 36000, "r1") # Note: remember to change your rate to the correct time units!
    writeToFile(seq1, "sumo.rou1.xml")


 

#seqv = PoissonRV(0.083, 36000) 





