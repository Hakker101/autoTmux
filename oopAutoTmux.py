#!/usr/bin/python3

import sys
import os
import argparse

parser = argparse.ArgumentParser(description = "Tmux startscript. Automatic start of tmux with separate windows for each basic enumeration tool of your choise. If flag -r is set it switches to window 0 and starts a initial scan on the provided ipadress.")
parser.add_argument('-l', '--window_list', action='append', required=True, help='The windows you want EX: -l nmap,nikto,dirbuster')
parser.add_argument('-i', '--ipadress', type = str, metavar='', required=True, help='Target ipadress')
parser.add_argument('-n', '--session_name', type = str, metavar='', required=True, help='The tmux session name')
parser.add_argument('-r', '--run_nmap', action='store_true', help='Set to start nmap automaticly')
args = parser.parse_args()


class tmux:
    def __init__(self, name, windows):
        self.name = name
        self.windows = windows
    
    # create tmux session with the name of --session_name argument
    def create_session(self):
        return os.system('tmux -2 new-session -d -s {0}'.format(self.name))
    
    # loop thru the list of window names from --windows argument and make a new window for each  
    def create_windows(self):
        #app_list = [str(app) for app in args.windows.split(',')]
        app_list = args.window_list
        for app in app_list:
            os.system('tmux new-window -t {0}:1 -n {1}'.format(self.name, app))

    # select window 0 and attach to the session
    def attach_session(self):
        os.system('tmux select-window -t {0}:0'.format(self.name))
        os.system('tmux -2 attach-session -t {0}'.format(self.name))

    # if --run_nmap flag is set then select window 0 and run a nmap scan 
    def start_nmap(self, ipadress):
        if args.run_nmap:
            os.system('tmux select-window -t {0}:0'.format(self.name))
            os.system('tmux send-keys -t {0} "nmap -sV -sC -oA {1} {2}" C-m'.format(self.name, self.name, ipadress))
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
    tmux_object.attach_session()

if __name__=='__main__':
    main()
