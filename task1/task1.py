#Internship Assignment 2
#Monument Labs

#Author: Alexander Moreno
#Date: 5/26/2018
#Task 1

#UNIX Operating Systems are assumed


#imports
import subprocess
import time




#display data from runCommands
def displayReport(data):
    print("\nTime Statistics:\n")
    print("\t Minimum runtime: command \'%s\' at %0.4f seconds.\n" % (data[0][0],data[0][1]) )
    print("\t Maximum runtime: command \'%s\' at %0.4f seconds.\n" % (data[1][0],data[1][1]))
    print("\t Average runtime:  %0.4f seconds.\n" % data[2])
    print("\t Total elapsed time:  %0.4f seconds.\n" % data[3])
    

    
    



def runCommands(cmds):
    #Variables
    #cmdstimes=[]
    minTime= None
    minIndex = 0
    maxTime=None
    maxIndex = 0
    avgTime=0
    totalTime=0
    for cmd in cmds:
        #set up process
        start = time.time()
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

        #Wait for processes to finish
        while p.poll() is None:
            time.sleep(0)
        end = time.time()

        
        if minTime == None and maxTime == None:
            minTime = end-start
            maxTime = end-start
            minIndex = cmds.index(cmd)
            maxIndex = cmds.index(cmd)
            
        if (end-start) > maxTime:
            maxTime = end-start
            maxIndex = cmds.index(cmd)
        elif (end-start) < minTime:
            minTime = end-start
            minIndex = cmds.index(cmd)

        #add to total elapsed time
        totalTime += end-start
        #cmdstimes.append(end-start)
        #print(cmdstimes)
    #Process data
    avgTime = totalTime / len(cmds)

    return ([cmds[minIndex],minTime],[cmds[maxIndex],maxTime],avgTime,totalTime)
    

    
    
if __name__ == '__main__':
    
    #commands
    commands = [
        'sleep 3',
        'ls -l /',
        'find /',
        'sleep 4',
        'find /usr',
        'date',
        'sleep 5',
        'uptime'
        ]
    #run commands
    data = runCommands(commands)
    #display statistics for execution
    displayReport(data)
