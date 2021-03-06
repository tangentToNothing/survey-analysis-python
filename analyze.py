#!usr/bin/python
import os
import sys,getopt
import csv

def main():
	inputfile = ''

	for i in range(0, len(sys.argv)):
		arg = sys.argv[i]
		if(arg == '-i'):
			inputfile = sys.argv[i+1]
		elif(arg == "-h"):
			print("analyze11.py -i <inputtext>")

	projector_items = ['projection','projector','projector,','projection']
	whiteboard_blackboard_items = ['board','whiteboard','blackboard','blackboard,','whiteboard,','chalkboard']
	marker_chalk_items = ['marker','markers','chalk','eraser','erasers']
	HVAC_items = ['heating','heater','temperature', 'temperature control', 'thermostat','HVAC','hvac','Temperature']
	furniture_items = ['desk','desks','lectern','lecterns','table','tables','blinds','podium','podiums']
	display_items = ['display', 'screen', 'TV', 'tv']
	scheduling_items = ['seats','seating','capacity','cap','schedule','scheduling']
	design_items = ['cover','covering', 'blocking','blocks','obstruct','block']
	doccam_items = ['Document','camera','document']
	computer_items = ['computer', 'computers','laptop','laptops','PC','pc','PCs','Laptop','Computer']

	projector_count = 0
	whiteboard_blackboard_count = 0
	marker_chalk_count = 0
	HVAC_count = 0
	furniture_count = 0
	display_count = 0
	scheduling_count = 0
	design_count = 0
	doccam_count = 0
	computer_count = 0

	text = []
	input1 = open(inputfile)
	text = input1.read()

	array_text = text.split()
	for word in array_text:
		if word in projector_items:
			projector_count+=1
		if word in whiteboard_blackboard_items:
			whiteboard_blackboard_count+=1
		if word in marker_chalk_items:
			marker_chalk_count+=1
		if word in HVAC_items:
			HVAC_count +=1
		if word in furniture_items:
			furniture_count+=1
		if word in display_items:
			display_count +=1
		if word in scheduling_items:
			scheduling_count+=1
		if word in design_items:
			design_count+=1	
		if word in doccam_items:
			doccam_count+=1
		if word in computer_items:
			computer_count+=1


	print("There were:\n")
	print(str(projector_count) + " projection items")
	print(str(whiteboard_blackboard_count) + " whiteboard/blackboard items")
	print(str(marker_chalk_count) + " marker/chalk items")
	print(str(HVAC_count) + " HVAC items")
	print(str(furniture_count) + " furniture items")
	print(str(display_count) + " display items")
	print(str(scheduling_count) + " scheduling items")
	print(str(design_count) + " design items")
	print(str(doccam_count) + " document camera items")
	print(str(computer_count) + " computer items")
	print("\nThere were " + str(projector_count + whiteboard_blackboard_count + marker_chalk_count + HVAC_count + furniture_count + display_count + scheduling_count + design_count + doccam_count + computer_count) + " items")
	print("\nThere were " + str(len(array_text)) + " words")

main()

