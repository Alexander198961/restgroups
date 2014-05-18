#!/usr/bin/python

import web
from cgroup import *
import os
from subprocess import Popen, PIPE
from find_task import *
def cpu_usage_for_proccess(id):
	cmd = "ps aux | awk '{ if( $2 ==" + str(id) + ") print $3 }'"
    	cpu_usage = os.popen(cmd).read().rstrip('\n');
	return cpu_usage
myGroups = Mygroups().group_list()
urls = ["/groups","ListofGroup" , "/groups/.*" , "GroupHandler" ]
dict = {}	
app = web.application(urls, globals())
class ListofGroup:
    def GET(self):
        return myGroups
        # return web.ctx.env['REQUEST_URI']

class GroupHandler:
    def GET(self):
        uri = web.ctx.env['REQUEST_URI']
        group = uri.split('/')[2]
	if myGroups.count(group):
		myProcess = FindTask()
  		myList = myProcess.findTasks(group)
		for process in myList:
			cpu_usage = cpu_usage_for_proccess(process)
                	dict[process] = cpu_usage
		return dict
	else:
		return "not found"
	
web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()
