'''
vmstat command output parsing:
watching a column in a linux cmd ( collect x samples and report when columns value > y

'''

# https://gist.github.com/brainyl/052dbe1d9a999f0e6c8635ceb9636ffa
# A python script that monitors a given column from vmstat and logs the output once a certain value has been exceeded

import sys

'''
vmstat 1 | python script.py --column=10 --max_value=200 --column_count=5
'''

def get_arg(args: str):
    return int(args.split('=')[1])

args = sys.argv[1:]
column = get_arg(args[0])
max_value = get_arg(args[1])
column_count = get_arg(args[2])

i=0
count = 0
for line in iter(sys.stdin.readline, ''):
    if i < 2:
        # print the headings
        print(line)
    else:
        # get the values for each heading ignoring the last character which is a new line \n
        values = [int(item) for item in line[:-1].split(' ') if item]

        # if the count has exceeded the column count  print the line and exit
        if count >= column_count:
            print(line)
            exit()
        # keep incrementing the count if the value exceeds the max consecutively else reset count to 0
        if values[column] > max_value:
            count += 1
        else:
            count = 0
    i += 1

##############################################################################################################
# READ VMSTAT
# https://medium.com/@damianmyerscough/vmstat-explained-83b3e87493b3

##############################################################################################################
# zip (parsing vmstat output)
#The following script parses the output of the 'vmstat 1 1' command.

#!/usr/bin/env python

import os
'''
$ vmstat 1 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0     36 9343440 139596 4079320    0    0   185    52  358  274  6  3 89  1  0
'''
lines = os.popen( 'vmstat 1 1').readlines()
dct = dict( zip( lines[-2].split(), lines[-1].split()))

print( "dct", dct)

''' 
output: 
dct {'wa': '1', 'sy': '3', 'b': '0', 'us': '6', 'bo': '52', 'cache': '4079320', 'bi': '185', 
'free': '9341332', 'st': '0', 'si': '0', 'r': '0', 'so': '0', 'swpd': '36', 'in': '358', 
'cs': '274', 'id': '89', 'buff': '139588'}
'''

##############################################################################################################
# https://stackoverflow.com/questions/52837267/subprocess-check-output-process-returning-the-same-output-when-run-in-loop

while True:
    output = subprocess.check_output("vmstat|tail -1", shell=True).decode('utf-8');
    m = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+\d+\s+\d+$", output)
    print('US', int(m.group(1)))
    print('SY', int(m.group(2)))
    # us: Time spent running non-kernel code. (user time, including nice time)
    # sy: Time spent running kernel code. (system time)
    usage=int(m.group(1))+int(m.group(2))
    if usage>CPU:
        ...
    else:
        print "cpu usage is below threshold"
