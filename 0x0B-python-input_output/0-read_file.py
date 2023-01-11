#!/usr/bin/python3
def read_file(filename = ""):
	"""
		This function reads a text file and prints it out on the screen
	"""
	with open(filname, mode = "r" encoding = "utf-8") as my_file:
		print(my_file.read(), end = "")
