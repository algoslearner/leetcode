'''
Count number of emails in a large file:
'''

import re 

n_email_addresses = 0 
with open("/Downloads/email.txt",'r') as f 
  for line in f: 
    emails_found = re.findall(r'[\w\.-]+@[\w\.-]+', line) 
    n_email_addresses += len(emails_found) 
print(n_email_addresses)
