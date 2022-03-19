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

# READ VMSTAT
# https://medium.com/@damianmyerscough/vmstat-explained-83b3e87493b3
