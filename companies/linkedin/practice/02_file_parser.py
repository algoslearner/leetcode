'''
Parse /var/log/syslog and extract values.

Dec  3 00:02:54 Mac Google Chrome Helper[69194]: Couldn't set selectedTextBackgroundColor from default ()
Dec  3 00:03:05 Mac Safari[68992]: KeychainGetICDPStatus: keychain: -25300
Dec  3 00:03:05 Mac Safari[68992]: KeychainGetICDPStatus: status: off
Dec  3 00:03:06 Mac com.apple.xpc.launchd[1] (com.apple.WebKit.Networking.AC8ED90D-0AC0-4666-B213-8BE93DE51E8C[68993]): Service exited with abnormal code: 1
Dec  3 00:03:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367
Dec  3 00:03:08 Mac garcon[68729]: host connection <NSXPCConnection: 0x7fc9d8f1eda0> connection from pid 68708 invalidated
Dec  3 00:03:08 Mac WindowServer[68664]: CGXGetConnectionProperty: Invalid connection 20367
Write a script which parses /var/log/messages and generates a CSV with two columns: minute, number_of_messages in sorted time order.

minute,number_of_messages
Dec  3 00:02,1
Dec  3 00:03,6
'''

'''
Extract the program name from the field between the hostname and the log message and output those values in columns.

minute,number_of_messages,Google Chrome Helper,Safari,com.apple.xpc.launchd,WindowServer,garcon
Dec  3 00:02,1,0,0,0,0
Dec  3 00:03,0,2,1,2,1
I think the key part of this problem is regular expression. For the first task, I used the following regular expression:

^(.*? \d+ \d+\:\d+).*
Then use re.match(regexp, line).groups() to extract minute.
collections.Counter can count objects.
For the second task, the regular expression is:

^(.*? \d+ \d+\:\d+)\:\d+ .*? (.*?)\: .*
The second task also has to find all programs in the log file.
'''

# https://www.mejorcodigo.com/p/109322.html

#!/usr/bin/env python

import re

msg_per_min = {}
found_programs = set()

output = {}
regex = re.compile(r'^(\w+ \d+ \d+:\d+):\d+ \w+ (\w+).*$')

with open("input.txt", "r") as file:
	for line in file:
		cols = line.split(":")
		
		# extract minute, number of messages per minute
		min = str(cols[0] + ":" + cols[1])
		msg_per_min[min] = msg_per_min.get(min,0) + 1
		
		# extract program name, count per minute
		match = regex.match(line)
		if match:
			minute = match.group(1)
			program = match.group(2)
			found_programs.add(program)
			if minute and program:
				if minute in output and program in output[minute]:
					output[minute]["total_count"] += 1
					output[minute][program] += 1
				elif minute in output and program not in output[minute]:
					output[minute]["total_count"] += 1
					output[minute][program] = 1
				else:
					output[minute] = dict()
					output[minute]["total_count"] = 1
					output[minute][program] = 1
		
			
# print(msg_per_min)
title1 = 'minute,number_of_messages'
for min,count in msg_per_min.items():
	output1 = str(min) + ',' + str(count)
	print(output1)


title2 = 'minute,total_count,' + ','.join(found_programs)
for min in output.keys():
	output2 = min + "," + str(output[min]["total_count"])
	for p in found_programs:
		count = output[min].get(p,0)
		output2 += ","+ str(count)
	print(output2)
#for k, v in output.items():
    #print("{0} {1}".format(k, v))

	
'''
output:

Dec  3 00:02,1
Dec  3 00:03,6
Jan 20 03:25,2
Jan 20 03:26,2
Jan 20 03:30,2
Jan 20 05:03,1
Jan 20 05:20,1
Jan 20 05:22,6
Jan 20 03:25,2,0,1,0,0,0,0,0,1
Jan 20 03:26,2,2,0,0,0,0,0,0,0
Jan 20 03:30,2,0,0,0,0,0,2,0,0
Jan 20 05:03,1,0,0,0,1,0,0,0,0
Jan 20 05:20,1,0,0,1,0,0,0,0,0
Jan 20 05:22,6,0,0,0,0,1,0,5,0
'''
