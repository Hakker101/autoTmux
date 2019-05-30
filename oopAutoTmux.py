'''
Automatic start of tmux with separate windows for each basic enumeration tool of your choise. Switching to nmap window and starts a initial scan on the provided ipadress.
'''
import sys
import os
import argparse

parser = argparse.ArgumentParser(description = "Tmux startscript")
parser.add_argument('-w', '--windows', type = str, metavar='', required=True, help='A comma separated list of window names you want ex: "window1,window2,window3"')
parser.add_argument('-i', '--ipadress', type = str, metavar='', required=True, help='Target ipadress')
parser.add_argument('-n', '--session_name', type = str, metavar='', required=True, help='The tmux session name')
args = parser.parse_args()


class tmux:
    def __init__(self, name, windows):
        self.name = name
        self.windows = windows
    
    
    def create_session(self):
        return os.system('tmux -2 new-session -d -s %s'%(self.name))
    
    def create_windows(self):
        app_list = [str(app) for app in args.windows.split(',')]
        for app in app_list:
            os.system('tmux new-window -t %s:1 -n %s'%(self.name, app))


    def attach_session(self):
        os.system('tmux select-window -t %s:1'%(self.name))
        os.system('tmux -2 attach-session -t %s'%(self.name))


    #def start_nmap(self):
    #    app_list = [str(app) for app in args.windows.split(',')]
    #    index = 0
    #    for app in app_list:
    #        if app == 'nmap':
    #            #os.system('tmux select-window -t %:%'%(self.name,index))
    #            #os.system('tmux send-keys "nmap -sV -sC -oA %s %s" C-m'%(self.name, self.t_adress))
    #        else:
    #            index += 1

class target:
    def __init__(self, t_ipadress):
        self.t_ipadress = t_ipadress

    
def main():
    t = target(args.ipadress)
    tmux_object = tmux(args.session_name, args.windows)
    tmux_object.create_session()
    tmux_object.create_windows()
    tmux_object.attach_session()

if __name__=='__main__':
    main()
