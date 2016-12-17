"""
Author: Lance Pereira
Date: 2016/12/16
Name: False Coins
"""

#print ("Atleast its running")

def evaluateCases(dataList):
	for values in dataList:
		(object1,object2,heavier) = values.split(" ")
		print(object1)
		print(object2)
		print(heavier)


def inputSorter():
	numberOfCases = input("How many trials: ")
	inputList = []
	for i in range(numberOfCases):
		inputList.append(raw_input())
	evaluateCases(inputList)
	#print (inputList)

inputSorter()
		