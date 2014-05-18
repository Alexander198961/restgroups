Please read this article about Apache settings 

http://webpy.org/cookbook/fastcgi-apache
place code to dir for example /var/www/myapp/
Note for run this application You need check Your SELINUX settings and turn
off it

REST call  examples:
1 list available cgroups http://127.0.0.1/groups
2 list the tasks (PIDs) for a given cgroup  http://127.0.0.1/groups/cpu
3 place a process into a cgroup   http://127.0.0.1/groups/Your_group_name
returns dictonary in this way: processId => cpu usage
 
