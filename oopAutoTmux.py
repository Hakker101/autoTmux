#!/usr/bin/python3

import sys
import os
import argparse

parser = argparse.ArgumentParser(description = "Tmux startscript. Automatic start of tmux with separate windows for each basic enumeration tool of your choise. Has starter options for nmap, nikto and gobuster separately or all at ones.")
parser.add_argument('-l', '--window_list', action='append', required=False, help='The windows you want EX: -l nmap,nikto,dirbuster')
parser.add_argument('-i', '--ipadress', type = str, metavar='', required=True, help='Target ipadress')
parser.add_argument('-n', '--session_name', type = str, metavar='', required=True, help='The tmux session name')
parser.add_argument('-r', '--run_nmap', action='store_true', help='Set to start nmap automaticly')
parser.add_argument('-a', '--run_all', action='store_true', help='Set to start nmap, nikto and gobuster all at ones')
args = parser.parse_args()


class tmux:
    def __init__(self, name, windows):
        self.name = name
        self.windows = windows
    
    # create tmux session with the name of --session_name argument
    def create_session(self):
        return os.system('tmux -2 new-session -d -s {0}'.format(self.name))
    
    # loop thru the list of window names from --window_list argument and make a new window for each item in list  
    # if args.run_all is set then discard window list and make another set of windows
    def create_windows(self):
        if not args.run_all:
            app_list = args.window_list
            for app in app_list:
                os.system('tmux new-window -t {0}:1 -n {1}'.format(self.name, app))
        else:
            return

    # select window 0 and attach to the session
    def attach_session(self):
        os.system('tmux select-window -t {0}:0'.format(self.name))
        os.system('tmux -2 attach-session -t {0}'.format(self.name))

    # if --run_nmap flag is set then select window 0 and run a nmap scan 
    def start_nmap(self, ipadress):
        if args.run_nmap:
            if not args.run_all:
                os.system('tmux select-window -t {0}:0'.format(self.name))
                os.system('tmux send-keys -t {0} "nmap -sV -sC -oA {1} {2}" C-m'.format(self.name, self.name, ipadress))
        else:
            return
    
    
    def start_all(self, ipadress):
        if args.run_all:
            
            app_list = ['nmap', 'nikto', 'gobuster']
            
            for app in app_list:
                    os.system('tmux new-window -t {0}:1 -n {1}'.format(self.name, app))

            for app in app_list:
                if app == 'nmap':
                    os.system('tmux select-window -t {0}:1'.format(self.name))
                    os.system('tmux send-keys -t {0} "nmap -sV -sC -oA {1} {2}" C-m'.format(self.name, self.name, ipadress))
                    print('HOLA AMIGOS!!')
                elif 'nikto' in app:
                    os.system('tmux select-window -t {0}:2'.format(self.name))
                    os.system('tmux send-keys -t {0} "nikto -host {1} " C-m'.format(self.name,'http://' + ipadress))
                elif 'gobuster' in app:
                    os.system('tmux select-window -t {0}:3'.format(self.name))
                    os.system('tmux send-keys -t {0} "gobuster -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -u {1} -o {2}" C-m'.format(self.name,'http://' + ipadress, self.name + '.gbuster'))
        else:
            return



class target:
    def __init__(self, t_ipadress):
        self.t_ipadress = t_ipadress

    
def main():
    t = target(args.ipadress)
    tmux_object = tmux(args.session_name, args.window_list)
    tmux_object.create_session()
    tmux_object.create_windows()
    tmux_object.start_nmap(args.ipadress)
    tmux_object.start_all(args.ipadress)
    tmux_object.attach_session()

if __name__=='__main__':
    main()
