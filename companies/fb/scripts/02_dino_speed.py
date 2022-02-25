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

leg_length = {}
stride_length = {}
pedal = {}
speed = {}

# read the input file - 1
with open(dataset1.csv,"r") as dataset1:
	for line in dataset1:
		line_list = line.split(",")
		if line_list[0] != "NAME":
			dinoName = line_list[0]
			leg_length[dinoName] = line_list[1]

# read the input file - 2
with open(dataset2.csv,"r") as dataset2:
	for line2 in dataset2:
		line2_list = line2.split(",")
		if line2_list[0] != "NAME":
			dinoName = line2_list[0]
			leg_length[dinoName] = line2_list[1]
			pedal[dinoName] = line2_list[1]

# speed calculation
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
g = 9.8
for name in pedal:
	if pedal[name] = "bipedal":
		stride_len = stride_length[name]
		leg_len = leg_length[name]
		speed = ((float(stride_len) / float(leg_len)) - 1) * (math.sqrt(float(leg_len) * g))
		speed[speed] = name
		

# print the names of only the bipedal dinosaurs from fastest to slowest		
names = reversed(sorted(speed.keys()))
for i in names:
	print(speed[i])
