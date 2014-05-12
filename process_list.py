#!/usr/bin/python
import os
import re
class MyProcess:
    def getList(self):    
        content = os.listdir("/proc");
        prog = re.compile('[0-9]')
        list = []
        for proc in content:
            result = prog.match(proc)
            if result  :
                list.append(proc)
        return list       
    

       
         