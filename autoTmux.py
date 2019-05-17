'''
Automatic start of tmux with separate windows for each basic enumeration tool. Switching to nmap window and starts a initial scan.
'''
import sys
import os
#naming session to current directory, taking target and domain from argv1,2 
directory = os.getcwd()
target_name = sys.argv[1]
target_domain = sys.argv[2]
full_target = target_name + "." + target_domain
session_name = target_name

#Start a new tmux session and name it as current working directory
os.system('tmux -2 new-session -d -s %s'%(session_name))
# Set up windows for enumerations scripts 
os.system("tmux new-window -t %s:1 -n 'nmap'"%(session_name) )
os.system('tmux new-window -t %s:2 -n "nikto"'%(session_name) )
os.system('tmux new-window -t %s:3 -n "gobuster"'%(session_name) )

#switch to nmap window
os.system('tmux select-window -t %s:1'%(session_name))
#starting nmap
os.system('tmux send-keys "nmap -sV -sC -oA %s %s" C-m'%(target_name,full_target))
# Attach to session
os.system('tmux -2 attach-session -t %s'%(session_name))
