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
bipedals = {}
g = 9.8

# read the input file - 1
with open("dataset1.csv","r") as dataset1:
	for line in dataset1:
		details = line.split(",")
		if details[0] != "NAME":
			name = details[0]
			dino[name] = details[1]

# read the input file - 2
with open("dataset2.csv","r") as dataset2:
	for line2 in dataset2:
		details2 = line2.split(",")
		if details2[0] != "NAME" and details2[2].rstrip() == "bipedal":
			name = details2[0]
			if name in dino:
				leg_len = float(dino[name])
				stride_len = float(details2[1])
				# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
				s = ((stride_len / leg_len) - 1) * (math.sqrt(leg_len * g))
				s = round(s,4)
				bipedals[name] = s
			else:
				# print("New bipedal dinosaur: "+name)
				continue
	

# print the names of only the bipedal dinosaurs from fastest to slowest	
print(bipedals)	
sorted_keys = reversed(sorted(bipedals, key=bipedals.get))
for name in sorted_keys:
	print(name)

