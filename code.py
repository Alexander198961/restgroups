#!/usr/bin/python

import web
from cgroup import *
import os
from subprocess import Popen, PIPE
from find_task import *
myGroups = Mygroups().group_list()
urls = ["/groups","ListofGroup" , "/groups/.*" , "GroupHandler" ]
	
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
		return myProcess.findTasks(group)
	else:
		return "not found"
	
web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()
