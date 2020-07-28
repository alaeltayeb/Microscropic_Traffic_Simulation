
#!/usr/bin/env python 
import matplotlib.pyplot as plt
import math
import numpy as np
import csv

# C:\Users\CSAM Extra\lab2_sumo_win>c:\Python27\python sumo_traci_test1.py
import os, subprocess, sys, socket, time, struct, random, math

# the path can be also declared manually in the operating system. Need to set the path to the sumo.Link?
# sys.path.append(os.path.join('c:', os.sep, 'whatever', 'path', 'to', 'sumo', 'tools'))
# in order to be able to import
sumo_path="C:\\sumo-1.0.1"
sys.path.append(os.path.join(sumo_path, 'tools'))
os.environ["SUMO_HOME"]= sumo_path

# import the traci module
import traci

# host and port definition
#host='127.0.0.1'
traci_port=8813 

# formulate the command to start sumo
sumo_exe ="C:\\sumo-1.0.1\\bin\\sumo-gui"

conf_file = "sumo.sumo1.cfg"
sumo_cmd=[sumo_exe, "-c", conf_file]
# start sumo as traci server
#traci.start(sumo_cmd)
sumoProcess = subprocess.Popen("%s -c %s" % (sumo_exe, conf_file), shell=True)

# initialize traci communication
traci.init(traci_port, 10)

#plot


# simulation loop
i = 1 
sim_time=3600
time_step=0.1 #0.1 sec
laststep = int(sim_time/time_step)+1
speedList = []
meanSpeed = []
meanSpeedPerMin = [] #mean of every 600 time_step

while i < laststep:
	# one simulation step
	traci.simulationStep()
	 # get the ID of all vehicles that are in the system
	IDList = traci.vehicle.getIDList()
	
       #mean speed of the vehicles currently in
        for veh_id in IDList:
            speedList.append(traci.vehicle.getSpeed(veh_id)) #Returns the speed in m/s
            if i <= 9000:
                del speedList[:]
            else:                    
                meanSpeed.append(np.mean(speedList))
                if len(meanSpeed)>600: #when mean speeds from one minute
                    meanSpeedPerMin.append(np.mean(meanSpeed)) #append the average to the list for means per min                   
                    #print(meanSpeedPerMin)
                    del meanSpeed[1:601]
                
                
            i = i + 1
            
                
traci.close()


print "test01"
x = range(45)
plt.scatter(x, meanSpeedPerMin)

plt.show()
dictionary = {
   "run5": meanSpeedPerMin
 }

#print(dictionary)

Write dictionary to csv file
with open('CarFollowing.csv', 'a') as f:  
    w = csv.DictWriter(f, dictionary.keys())
    w.writeheader()
    w.writerow(dictionary)


#:retab!
