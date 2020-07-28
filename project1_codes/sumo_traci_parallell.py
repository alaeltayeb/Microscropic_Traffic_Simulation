#!/usr/bin/env python 

""" 
@file    VSLS_ma.py
@author  Xiaoliang Ma
@date    2018-10-08
@version $Id$ 

MCS via the TraCI interface. 
 
Copyright (C) 2009 DLR/TS, Germany 
All rights reserved 
""" 

import os, subprocess, sys, socket, time, struct, random, math, numpy
from multiprocessing import Process, cpu_count

def simulation(cmd) :
        traci.start(cmd)
        i = 1
        laststep = 18000
        
        while i <= laststep:
                traci.simulationStep( )
                IDList = traci.vehicle.getIDList()
                i=i+1
                if len(IDList):
                        print IDList

        traci.close()
        proc = os.getpid()
        print proc

# the path can be also declared manually in windows or linux as below
# sys.path.append(os.path.join('c:', os.sep, 'whatever', 'path', 'to', 'sumo', 'tools'))

if __name__ == '__main__' :
        if 'SUMO_HOME' in os.environ:
                sumo_path=os.environ['SUMO_HOME']
                sys.path.append(os.path.join(sumo_path, 'bin'))
        else:
                # sumo_path="/usr/share/sumo"
                sys.path.append(os.path.join(sumo_path, 'tools'))
                
        # import traci module
        import traci

        host='127.0.0.1'
        traci_port=8813
        #sumo_exe = "/usr/bin"
        #sumo_cmd= "/usr/bin/sumo_gui"
        # if "SUMO" in os.environ:
        #     	sumoExe = os.path.join(os.environ["SUMO"], "sumo")
        conf_file = "sumo_test.sumo.cfg"
        #sumo_cmd=["sumo-gui", "-c", conf_file]
        sumo_cmd=["sumo", "-c", conf_file]

        procs = []

#       print("Number of cpu : ", cpu_count())
#       Parallel
        max_process = cpu_count()
        for i in range(1, max_process) :
                proc = Process(target=simulation, args=(sumo_cmd,))
                procs.append(proc)
                proc.start()

        for proc in procs:
                proc.join()

        #sumoProcess = subprocess.Popen("%s -c %s" % (sumo_cmd, conf_file), shell=True, stdout=sys.stdout)

        # print vehicle data for this simulation
        #print dict_VehicleData
        # calculate emission per simulation
        #Emission_models.instEmissionModel.VTMicro(dict_VehicleData)

        #:retab!

