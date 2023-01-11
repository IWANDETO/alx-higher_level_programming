#!/usr/bin/python3
def read_file(filename = ""):
	"""
		This function reads a text file and prints it out on the screen
	"""
	with open(filname, encoding = "utf-8") as f:
		print(f.read(), end = "")
