#!/usr/bin/env python
import sys
import os

RED = '\x1b[91m'
RED1 = '\033[31m'
BLUE = '\033[94m'
GREEN = '\033[32m'
BOLD = '\033[1m'
NORMAL = '\033[0m'
TRANSPARENT = '\033[0m'

def clear():
	return os.system('cls' if os.name == 'nt' else 'clear')

def logo():
	clear()
	print (BLUE + "	 ___  _____   _____ _ __  " + TRANSPARENT)
	print (BLUE + "	/ __|/ _ \ \ / / _ \ |_ \ " + TRANSPARENT)
	print (BLUE + "	\__ \  __/\ V /  __/ | | |" + TRANSPARENT)
	print (BLUE + "	|___/\___| \_/ \___|_| |_|" + TRANSPARENT)
	print (BLUE + "							  " + TRANSPARENT)

logo()

if (sys.version_info[0] < 3):
	print (RED+"Python Version 3 Needed!"+TRANSPARENT)
	print (RED1+"python sqrt.py <nr>"+TRANSPARENT)
	sys.exit(0)

class sqrt:

	def __init__(self, n):
		self.n = n
		self.result = []

	def createLeftNumber(self, left, clct):
		lst = []
		lst.append(left)
		lst.append(clct)
		tmp = ''.join(repr(int(n)) for n in lst)
		return int(tmp)

	def createRightNumber(self, right, pair):
		lst = []
		lst.append(right)
		lst.append(pair[0])
		lst.append(pair[1])
		tmp = ''.join(repr(int(n)) for n in lst)
		return int(tmp)

	def createDescendNumber(self, l, c):
		return self.createLeftNumber(l, c) * c

	def addTwoZero(self, nr):
		lst = []
		lst.append(nr)
		lst.append(0)
		lst.append(0)
		tmp = ''.join(repr(int(n)) for n in lst)
		return int(tmp)

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
	print (RED1+"python sqrt.py <nr>"+TRANSPARENT)
else:
	sqrtObj = sqrt(int(sys.argv[1]))
	print (sqrtObj.sqrtdump())