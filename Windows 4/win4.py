#Gabriel Sohn, Ellias Miller
import os
import subprocess
exit = ""
#windows.pslist_brief
#windows.malfind_brief
FILE = input("Enter file address: ")
subprocess.call("./vol.py -f " + FILE + " windows.pslist_brief > File1.txt", shell=True)
subprocess.call("./vol.py -f " + FILE + " windows.malfind_brief > File2.txt", shell=True)

# Open File in Read Mode
file_1 = open('File1.txt', 'rb')
out_1 = open('out.txt', 'x')
#def recur(file)

###################################################################################################
print("Comparing files ", " @ " + 'File1.txt', " # " + 'File2.txt', sep='\n')

d = {}
count = 0
#file_1_line = file_1.readline()
#print(file_1_line)

for line in file_1:
    count += 1
    count2 = 0
    line.rstrip()

    #(pid, val, extra) = line.split(b'\t')
    if count <= 4:
        continue
    else:
        file_2 = open('File2.txt', 'rb')
        pid = line.split(b'\t')
        out_1.write(pid[0].decode("utf-8"))
        out_1.write(line.decode("utf-8"))
        line2 = file_2.readline()

        while line2:
            line2 = file_2.readline()
            count2 += 1
            line2.rstrip()

            if count2 <= 4:
                continue
            pid2 = line2.split(b'\t')
            if pid[0] == pid2[0]:
                #print("hello")
                out_1.write(line2.decode("utf-8"))
                #print(pid[0] +  pid2[0])
                #d[line].append(line2.decode(""utf-8""))
            else:
                continue
        file_2.close()
file_1.close()
out_1.close()
out = open("out.txt", "r")
for line in out:
    print(line)
out.close()
