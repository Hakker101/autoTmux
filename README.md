# autoTmux
automatic tmux session. Separate windows for all applications and autostarts a nmap scan (-sV -sC -oA ) 

Example: ./oopAutoTmyx.py -r -n sessionName -i 10.10.10.137 -l 'nmap, nikto, gobuster'
This will start a tmux session named sessionName with -r flag set to automaticly run nmap on the -i ipadress. The -l takes a list and creates a separate window for each item. 
