'''
Question 1:
You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivore

$ cat dataset2.csv 
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptorr,2.62,bipedal
'''

import math
import re

dino = {}
biped = {}
g = 9.8

with open('dataset1.csv','r') as dataset1:
	for line in dataset1:
		cols = line.split(',')
		name = cols[0]
		dino[name] = cols[1]

with open('dataset2.csv','r') as dataset2:
	for line in dataset2:
		col = line.split(',')
		if col[2].rstrip() == "bipedal":
			name = col[0]
			if name in dino:
				# calculate speed
				stride_len = float(col[1])
				leg_len = float(dino[name])
				speed = ((stride_len / leg_len) - 1) * math.sqrt(leg_len * g)
				biped[name] = speed
				
			else:
				print("new bipedal dino : " + name)
				
				
# sort from fasted to slowest
#for n in sorted(biped, key =biped.get, reverse=True):
	#print(n)

for name, speed in sorted(biped.items(), key =lambda x:x[1], reverse=True):
	print(name)

	
######################################################################################
# output
'''
new bipedal dino : Deinonychus
new bipedal dino : Velociraptorr
Struthiomimus
Hadrosaurus
Tyrannosaurus Rex
'''

