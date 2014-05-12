#!/usr/bin/python
from subprocess import Popen, PIPE
import web
import os
import re
from cgroup import *  
from types import MethodType
p1 = Popen(["./run.sh"], stdout=PIPE).communicate()
print p1
