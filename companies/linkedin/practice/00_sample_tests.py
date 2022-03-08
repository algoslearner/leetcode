# Write a program which prints out all numbers between 1 and 100. When the program would print out a number exactly divisible by 4, print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn" instead.

def print_linkedin():
    for i in range(101):  #12
        if i % 4 == 0 and i % 6 == 0:
            print("LinkedIn")
        elif i % 6 == 0:
            print("In")
        elif i % 4 == 0:
            print("Linked")
        else:
            print (i)
        
def print_linkedin():
  for i in range(101):  #12
    if i % 4:
      print("Linked",)
    if i % 6 == 0:
      print("in",)
    print ("\n")

        

# Below, see a sample of /var/log/messages.
# ---------- begin sample log extract ----------
# Jan 20 03:25:08 fakehost logrotate: ALERT exited abnormally with [1]
# Jan 20 03:25:09 fakehost run-parts(/etc/cron.daily)[20447]: finished logrotate
# Jan 20 03:26:21 fakehost anacron[28969]: Job 'cron.daily' terminated
# Jan 20 03:26:22 fakehost anacron[28969]: Normal exit (1 job run)
# Jan 20 03:30:01 fakehost CROND[31462]: (root) CMD (/usr/lib64/sa/sa1 1 1)
# Jan 20 03:30:01 fakehost CROND[31461]: (root) CMD (/var/system/bin/sys-cmd -F > /dev/null 2>&1)
# Jan 20 05:03:03 fakehost ntpd[3705]: synchronized to time.faux.biz, stratum 2
# Jan 20 05:20:01 fakehost rsyslogd: [origin software="rsyslogd" swVersion="5.8.10" x-pid="20438" x-info="http://www.rsyslog.com"] start
# Jan 20 05:22:04 fakehost cs3[31163]:  Q: ".../bin/rsync -LD ": symlink has no referent: "/var/syscmds/fakehost/runit_scripts/etc/runit/service/superImportantService/run"#012Q: ".../bin/rsync -LD ": rsync error: some files/attrs were not transferred (see previous errors) (code 23) at main.c(1039) [sender=3.0.6]
# Jan 20 05:22:04 fakehost cs3[31163]:  I: Last 2 quoted lines were generated by "/usr/local/bin/rsync -LD --recursive --delete --password-file=/var/syscmds/modules/rsync_password /var/syscmds/fakehost syscmds@fakehost::syscmds_rsync"
# Jan 20 05:22:08 fakehost cs3[31163]:  Q: ".../sbin/sv restart": ok: run: /export/service/cool-service: (pid 32323) 0s
# Jan 20 05:22:08 fakehost cs3[31163]:  I: Last 1 quoted lines were generated by "/sbin/sv restart /export/service/cool-service"
# Jan 20 05:22:09 fakehost cs3[31163]:  R: cs3:  The cool service on fakehost does not appear to be communicating with the cool service leader.  Automating a restart of the cool service in attempt to resolve the communication problem.
# Jan 20 05:22:37 fakehost ACCT_ADD: WARNING: Manifest /var/syscmds/inputs/config-general/doit.txt has been processed already, bailing
# ---------- end sample log extract ----------

# Write a script which parses /var/log/messages and generates a CSV with two columns: minute, number_of_messages in sorted time order.

# ---------- begin sample output ----------
# minute, number_of_messages
# Jan 20 03:25,2
# Jan 20 03:26,2
# Jan 20 03:30,2
# Jan 20 05:03,1
# Jan 20 05:20,1
# Jan 20 05:22,6
# ---------- end sample output ------------ 

from collections import DefaultDict

def parse_log():
    min_to_msg_dict = DefaultDict(0)
    with open("/var/log/messages") as file:
        while x = file.readline() is not None:
            minute_with_secs = x.split("fakehost")[0]
            minute_split = minute.split(":")
            minute_split.delete(-1)
            minute = ':'.join(minute_split)
            min_to_msg_dict[minute] = min_to_msg_dict[minute] + 1
            
    
    print(min_to_msg_dict)
    
    
    
# Extract the program name from the field between the hostname and the log message and output those values in columns.
# ---------- begin sample output ----------
# minute,total_count,logrotate,run-parts,anacron,CROND,ntpd,rsyslogd,cs3,ACCT_ADD
# Jan 20 03:25,2,1,1,0,0,0,0,0,0
# Jan 20 03:26,2,0,0,2,0,0,0,0,0
# Jan 20 03:30,2,0,0,0,2,0,0,0,0
# Jan 20 05:03,1,0,0,0,0,1,0,0,0
# Jan 20 05:20,1,0,0,0,0,0,1,0,0
# Jan 20 05:22,6,0,0,0,0,0,0,5,1
# ---------- end sample output ------------
# Note: It is important that your program work with any arbitrary set of programs, not just the ones in the example output.

from collections import Set
    
def parse_log_with_program():
    
    min_to_msg_dict = {}
    with open("/var/log/messages") as file:
        while x = file.readline() is not None:
            hostname = x.split()[3]
            minute_with_secs = x.split(hostname)[0]
            minute_split = minute.split(":")
            minute_split.delete(-1)
            minute = ':'.join(minute_split)
            # min_to_msg_dict[minute] = min_to_msg_dict[minute] + 1
            
            program_name = x.split()[4].split('[')[0]
            
            if minute not in min_to_msg_Dict.keys:
                min_to_msg_dict[minute] = DefaultDict(DefaultDict(0))
            
            min_to_msg_dict[minute][program_name] = min_to_msg_dict[minute][program_name] + 1
                
            # min_to_msg_dict[prog_name] = min_to_msg_dict[prog_name] + 1
    allprogs = Set([x.keys() for x in min_to_msg_dict.values()])
    
    header = "minute,"
    header.append(",".join(allprogs))
    
    print(header)
    
    for i in min_to_msg_dict.keys():
        output = i + ":"
        for j in allprogs:
            output.append(min_to_msg_dict[i][j])
            output.append(",")
        print(output)
    
    

# Run this continuously on an ever-growing log file 



# Assume there is a REST API available at "http://www.linkedin.corp/api" for accessing employee information The employee information endpoint is "/employee/<id>" Each employee record you retrieve will be a JSON object with the following keys:
#   - 'name'  refers to a String that contains the employee's first and last name
#   - 'title' refers to a String that contains the employee's job title
#   - 'reports' refers to an Array of Strings containing the IDs of the employee's direct reports
# Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.
# For example, suppose that Flynn Mackie's employee id is 'A123456789' and his only direct reports are Wesley Thomas and Nina Chiswick. If you provide 'A123456789' as input to your function, you will see the sample output below.
 
# -----------Begin Sample Output--------------
# Flynn Mackie - Senior VP of Engineering
#   Wesley Thomas - VP of Design
#     Randall Cosmo - Director of Design
#       Brenda Plager - Senior Designer
#   Nina Chiswick - VP of Engineering
#     Tommy Quinn - Director of Engineering
#       Jake Farmer - Frontend Manager
#         Liam Freeman - Junior Software Engineer
#       Sheila Dunbar - Backend Manager
#         Peter Young - Senior Code Cowboy
# -----------End Sample Output--------------


# Sample JSON
# # GET /employee/A123456789
# {
#  "name": "Flynn Mackie",
#  "title": "Senior VP of Engineering",
#  "reports": ["A123456793", "A1234567898"]
# }

# http://docs.python-requests.org/en/latest/user/quickstart/#json-response-content

import requests

def get_reports(emp_id):
    r = requests.get("fakehost/" + start_employee_id).json()
    if "reports" not in r.keys():
        return None
    
    return r["reports"]

def get_details(emp_id):
    r = requests.get("fakehost/" + start_employee_id).json()
    
    return " - ".join([r["name"], r["title"]])

def print_list(input):
    if input is None or input.empty():
        return None
    return input.values()

def main(start_epmloyee_id):
    output = {}
    running_count = []
    emp_id = start_employee_id
    while x = get_reports(emp_id) is not None:
        output[emp_id] = x  # x = [123, 456]
        # running_count.push(x)  # runnig_count = [[123,456]] or [123,456]?
        for id in x:
            running_count.push(id)
        emp_id = running_count.pop()
    
    temp = output.keys()
    running_count = []
    while x = print_list(temp) is not None:
        print(x)
        print "\t"
        for id in x:
            running_count.push(id)
        x = running_count.pop()
        
    for x in output.keys():
        print "\t"
        print get_details(emp_id)