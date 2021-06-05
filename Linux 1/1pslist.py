#Gabriel Sohn, Ellias Miller
import os
import subprocess
exit = ""
FILE = input("Enter file address: ")
subprocess.call("./vol.py -f " + FILE + " linux.pslist", shell=True)
while exit != 'quit':

    PID = input("Enter Process or name or quit: ")
    exit = PID
    if exit != 'quit' and exit != '' and exit != None:
        subprocess.call("./vol.py -f " + FILE + " linux.pslist | grep " + PID, shell=True)
        print("Malfind search: ")
        subprocess.call("./vol.py -f " + FILE + " linux.malfind | grep " + PID, shell=True)
