#!/usr/bin/python
import os
from cgroup import *
from process_list import MyProcess
from mytype import *

    
  
myTasks = MyProcess().getList()
class FindTask:
    
    tasks =[]
    def getListofTask(self):
            return self.tasks
    def findTasks(self, cgroupName):
        file = "/cgroup/"+cgroupName + "/tasks"
        f = open(file)
        lines = f.readlines()
        
        f.close()
        diffElements =[]
        myFileList=[]
        for line in  lines:
             elem = line.strip()
             myFileList.append(elem)
        myDiff=set(myFileList).intersection(myTasks)
        for elem in myDiff:
            print elem
           
                    
task =  FindTask()
myTasksList = task.findTasks('memory/http')
#print task.getListofTask()
#print myTasksList      
            
#findTasks('memory/http')             
             

        
#      if processId in open        

#  (myLinuxPath.getFinalPath())
           