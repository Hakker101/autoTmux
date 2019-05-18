'''
Automatic start of tmux with separate windows for each basic enumeration tool. Switching to nmap window and starts a initial scan.
'''
import sys
import os

class tmux:
    def __init__(self, name):
        self.name = name
    
    
    def create_session(self):
        return os.system('tmux -2 new-session -d -s %s'%(self.name))
    
    def create_std_windows(self):
        app_list = ['nmap','nikto','gobuster']
        for app in app_list:
            os.system('tmux new-window -t %s:1 -n %s'%(self.name, app))


    def attach_session(self):
        os.system('tmux select-window -t %s:1'%(self.name))
        os.system('tmux -2 attach-session -t %s'%(self.name))

class target:
    def __init__(self, t_name, t_domain, full_target):
        self.t_name = t_name
        self.t_domain = t_domain
        self.f_target = full_target


#t = target(sys.argv[1], sys.argv[2], sys.argv[1] + "." + sys.argv[2])
#x = tmux(t.t_name)
#x.create_session()
#x.create_std_windows()
#x.attach_session()

#starting nmap needs to get a method!!
#os.system('tmux send-keys "nmap -sV -sC -oA %s %s" C-m'%(target_name,full_target))

