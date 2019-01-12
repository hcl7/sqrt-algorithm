#!/usr/bin/env python
import sys
import os

Black = '\x1b[30m'
Red = '\x1b[31m'
Green = '\x1b[32m'
Yellow = '\x1b[33m'
Blue = '\x1b[34m'
Magenta = '\x1b[35m'
Cyan = '\x1b[36m'
White = '\x1b[37m'
Default = '\x1b[39m'
LightGray = '\x1b[90m'
LightRed = '\x1b[91m'
LightGreen = '\x1b[92m'
LightYellow = '\x1b[93m'
LightBlue = '\x1b[94m'
LightMagenta = '\x1b[95m'
LightCyan = '\x1b[96m'
LightWhite = '\x1b[97m'

def clear():
	return os.system('cls' if os.name == 'nt' else 'clear')

def logo():
	clear()
	print (Blue + "	 ___  _____   _____ _ __  " + Default)
	print (Blue + "	/ __|/ _ \ \ / / _ \ |_ \ " + Default)
	print (Blue + "	\__ \  __/\ V /  __/ | | |" + Default)
	print (Blue + "	|___/\___| \_/ \___|_| |_|" + Default)
	print (Blue + "							  " + Default)

logo()

if (sys.version_info[0] < 3):
	print (Red+"Python Version 3 Needed!"+Default)
	print (Red+"python sqrt.py <nr>"+Default)
	sys.exit(0)

class sqrt:

	def __init__(self, n):
		self.n = n
		self.result = []

	def createLeftNumber(self, left, clct):
		left *= 10
		left += clct
		return left

	def createRightNumber(self, right, pair):
		tmp = right * 10
		tmp += pair[0]
		tmp *= 10
		tmp += pair[1]
		#tmp = ''.join(repr(int(n)) for n in lst)
		return tmp

	def createDescendNumber(self, l, c):
		return self.createLeftNumber(l, c) * c

	def addTwoZero(self, nr):
		tmp = nr * 100
		return tmp

	def closest(self, l, b):
		n = 9
		ncounter = n
		closestNumber = self.createDescendNumber(l, n)
		tmp = self.createDescendNumber(l, n)
		while (closestNumber>b):
			tmp = self.createDescendNumber(l, n)
			closestNumber = tmp
			ncounter = n
			n-=1
		return ncounter, closestNumber

	def closestPerfectRootNumber(self, n):
		tmp = 0
		index = 0
		i = 1
		while (tmp <= n):
			tmp = i * i
			index = i
			i += 1
		index -= 1
		return index, index * index

	def numberToList(self, n):
		return [int(d) for d in str(n)]

	def singleOdd(self, n):
		rightn = n
		collecter, descender = self.closestPerfectRootNumber(n)
		leftn = collecter
		self.result.append(collecter)
		leftn += collecter
		rightn -= descender
		return leftn, rightn, collecter, descender

	def multiplePair(self, l):
		tmpnr = self.createLeftNumber(l[0], l[1])
		leftn, rightn, collecter, descender = self.singleOdd(tmpnr)
		#print (leftn, rightn, collecter, descender)
		l.pop(0)
		l.pop(0)
		for i, j in zip(l[::2], l[1::2]):
			rightn = self.createRightNumber(rightn, [i,j])
			collecter, descender = self.closest(leftn, rightn)
			leftn = self.createLeftNumber(leftn, collecter)
			self.result.append(collecter)
			leftn += collecter
			rightn -= descender
			#print (leftn, rightn, collecter, descender)
		return leftn, rightn, collecter, descender

	def multipleOdd(self, l):
		tmpnr = l[0]
		leftn, rightn, collecter, descender = self.singleOdd(tmpnr)
		#print (leftn, rightn, collecter, descender)
		l.pop(0)
		for i, j in zip(l[::2], l[1::2]):
			rightn = self.createRightNumber(rightn, [i,j])
			collecter, descender = self.closest(leftn, rightn)
			self.result.append(collecter)
			leftn = self.createLeftNumber(leftn, collecter)
			leftn += collecter
			rightn -= descender
		return leftn, rightn, collecter, descender

	def sqrtdump(self):
		result = []
		leftn = 0
		descender = 0
		collecter = 0
		nrl = self.numberToList(self.n)
		if (len(nrl)%2==1 and len(nrl)<2):
			leftn, rightn, collecter, descender = self.singleOdd(self.n)
			while (rightn != 0):
				if (len(self.numberToList(rightn)) <= 12):
					rightn = self.addTwoZero(rightn)
					collecter, descender = self.closest(leftn, rightn)
					leftn = self.createLeftNumber(leftn, collecter)
					self.result.append(collecter)
					leftn += collecter
					rightn -= descender
				else:
					self.showNumber(self.n, self.result)
					sys.exit(0)
		elif (len(nrl)%2==1 and len(nrl)>=3):
			tmpcollecter, tmpdescender = self.closestPerfectRootNumber(nrl[0])
			leftn, rightn, collecter, descender = self.multipleOdd(nrl)
			while (rightn != 0):
				if (len(self.numberToList(rightn)) <= 12):
					rightn = self.addTwoZero(rightn)
					collecter, descender = self.closest(leftn, rightn)
					leftn = self.createLeftNumber(leftn, collecter)
					self.result.append(collecter)
					leftn += collecter
					rightn -= descender
				else:
					self.showNumber(self.n, self.result)
					sys.exit(0)
		else:
			collecter, descender = self.closestPerfectRootNumber(self.createLeftNumber(nrl[0], nrl[1]))
			result.append(collecter)
			leftn, rightn, collecter, descender = self.multiplePair(nrl)
			while (rightn != 0):
				if (len(self.numberToList(rightn)) <= 12):
					rightn = self.addTwoZero(rightn)
					collecter, descender = self.closest(leftn, rightn)
					leftn = self.createLeftNumber(leftn, collecter)
					self.result.append(collecter)
					leftn += collecter
					rightn -= descender
				else:
					self.showNumber(self.n, self.result)
					sys.exit(0)
					#print (''.join(repr(int(n)) for n in self.result))

	def showNumber(self, n, l):
		length = len(self.numberToList(n))
		if length % 2 == 1:
			length+=1
		l.insert(length//2, '.')
		print (''.join(map(str, l)))

if len(sys.argv)  < 2:
	print (Red+"python sqrt.py <nr>"+Default)
else:
	sqrtObj = sqrt(int(sys.argv[1]))
	print (sqrtObj.sqrtdump())
