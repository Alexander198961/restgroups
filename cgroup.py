#!/usr/bin/python
import os
import re
class Mygroups:
    def group_list(self):
        file = open("/proc/cgroups")
 	lines = file.readlines();
	groupArray = []
	for line in lines:
   	 	world =  line.split()[0]
    		pattern = "^#" 
    		prog = re.compile(pattern)
    		result = prog.match(world)
    		if result is None:
        		groupArray.append(world)
   
	file.close() 
	return groupArray
         
       
 #print (test.group_list())



    
        
