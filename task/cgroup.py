#!/usr/bin/python
import os
class Mygroups:
    def group_list(self):
        f = os.popen('lscgroup')
        out =f.read()
        string = str(out)
        list = string.splitlines()
        return list 
       
mygroups = Mygroups()
print (mygroups.group_list())
 #print (test.group_list())



    
        
