'''
Given STDIN arguments as $filepath and $count, print top 10 frequent words in the file. 
File content is a group of paragraphs, and word separators include spaces, dots, commas, semicolons, exclamations etc.

Example:
python fileparser.py "info.txt" "10"
$filepath = /log/filename.txt
$count = 10

Output:
price	9867
master	8766
logs	8400
burst	5632
alps	2121
nature	2009
dots	1437
pluck	1000
circle	451
book	105 
'''

import sys
from collections import Counter

def file_parser(filename:str, count:int):
	wordsfreq = {}
	with open(filename, 'r') as file:
		for line in file:
			line = line.rstrip()
			# assume space separator as space, to begin with
			words = line.split()
			wordsfreq = Counter(words)

	# print top freq numbers
	for word, freq in sorted(wordsfreq.items(), key=lambda x:x[1], reverse= True):
		if count > 0:
			outputline = word + '\t'+ str(freq)
			print(outputline)
			count -= 1
		else:
			break

def main():
	# read inputs from command line
	inputs = list(sys.argv)
	filename = inputs[1]
	count = int(inputs[2])
	file_parser(filename,count)
	
if __name__ == "__main__":
	main()

###########################################	
# TEST
# filename = 'countwords_info.txt'
# count = 15
# OUTPUT
'''
>python countwords.py countwords_info.txt 15
and     7
of      2
in      2
like    2
The     1
true    1
power   1
Po      1
see     1
comes   1
from    1
de      1
strong  1
relat   1
with    1
'''
