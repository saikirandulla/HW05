#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys
from sys import exit

# Body


def infinite_stairway_room(name):
	count = 0
	print "You walk through the door to see a dimly lit hallway,", name+"."
	print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light,', name+'.'
	print "There is also a window from which you can jump out the building, but you may die of injuries,", name+'.'
	print "Do you choose to take stairs or jump,",name+"?"
	next = raw_input("> ")
    
    # infinite stairs option
	if next == "take stairs":
		print 'You took the stairs,',name
		if (count > 0):
			print "but you're not happy about it"
		infinite_stairway_room(count + 1)
    # option 2
	if next == "jump":
		print ' You risked your life and jumped through the window into a gold room,', name+"!"
		gold_room(name)


def gold_room(name):
	print "This room is full of gold.  How much do you take,", name,"?"

	next = raw_input("> ")
	try:
		how_much = int(next)
	except:
		dead("Man, learn to type a number.", name)

	if how_much < 50:
		print "Nice,", name, "is not greedy,", name," wins!"
		exit(0)
	else:	
		dead("You greedy bastard!",name)


def bear_room(name):
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take" or next == "honey":
			dead("The bear looks at you then slaps your face off.", name)
		elif next == "taunt" and not bear_moved:
			print "The bear has moved from the door. You can go through it now,",name + "."
			bear_moved = True
		elif next == "taunt" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open" or next == "door" and bear_moved:
			infinite_stairway_room(name)
		else:
			print "I got no idea what that means."


def cthulhu_room(name):
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		main()
	elif "head" in next:
		dead("Well that was tasty!",name)
	else:
		cthulhu_room()

def dead(why,name):
	print name+",",why,"Good job!"
	exit(0)

def back_room(name):
	print "You are in the room filled with programmers who haven't showered since it last rained in California,", name
	print "You state your name but nobody listens -- probably because your name doesn't sound like a python keyword,", name
	print "You soon start programming python and never leave,",name
	exit(0)
	
##############################################################################
def main():
	# START the TextAdventure game
	name = sys.argv[1]
	print name + " is in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")

	if next == "left":
		bear_room(name)
	elif next == "right":
		cthulhu_room(name)
	elif next == "back":
		back_room(name)
	else:
		dead("You stumble around the room until you starve, ", name)

if __name__ == '__main__':
    main()
