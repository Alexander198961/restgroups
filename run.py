#!/usr/bin/python

import web
from cgroup import *

urls = ("/groups", "ListofGroup",
        
)
app = web.application(urls, globals())

class ListofGroup: 
    def GET(self):
        mygroup = Mygroups()
        mygroup.group_list() 
        return mygroup.group_list()

web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()
