#!/usr/bin/env python3
#__auth__ nhienit

import string
import getopt 
import sys

MIN = 0
MAX = 25

def rotate(char, start, end, shift):
	asc = ord(char) + shift
	if asc > end:
		return chr(start + (asc - end -1))
	else:
		return chr(asc)

def convert(str, shift):
	output = ''

	if shift > MAX:
		shift -= 26 * round(shift/26)
	elif shift < MIN:
		while(shift < MIN):
			shift += 26

	for char in str:
		if char in string.ascii_lowercase:
			output += rotate(char, ord(string.ascii_lowercase[0]), ord(string.ascii_lowercase[-1]), shift)
		elif char in string.ascii_uppercase:
			output += rotate(char, ord(string.ascii_uppercase[0]), ord(string.ascii_uppercase[-1]), shift)
		else:
			output += char
	return output

def help():
	print("Usage:")
	print("For encode: python3 main.py [-e | --encode] [-c | --cipher=] [-s | --shift]")
	print("For decode: python3 main.py [-d | --decode] [-c | --cipher=] ")
	return

if __name__ == "__main__":
	argv = sys.argv[1:]
	options, remainder = getopt.getopt(argv, 'edhc:s:', ['encode', 'decode', 'cipher=', 'shift=', '--help'])

	for opt, arg in options:
		if opt in ('-h', '--help'):
			exit(help())
		if opt in ('-e', '--encode'):
			mode = 'encode'
		elif opt in ('-d', '--decode'):
			mode = 'decode'
		elif opt in ('-c', '--cipher'):
			cipher = arg
		elif opt in ('-s', '--shift'):
			shift = int(arg)

	try:
		if mode == "encode":
			print(convert(cipher, shift))
		elif mode == "decode":
			for i in range(-25, 26):
				print("Shift=%d: %s"%(i, convert(cipher, i)))
	except:
		exit(help())