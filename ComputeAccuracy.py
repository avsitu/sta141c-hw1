#!/usr/bin/python2.7

# usage: python2 ComputeScore.py [filename] [threshold]
import sys
import time
from preprocess import preprocess

dataset = [] # stores data from file

def ComputeAccuracy(thr):
	acc = 0.0
	for sample in dataset:
		q1 = sample[0]
		q2 = sample[1]
		q1_set = set(q1)
		q2_set = set(q2)
		overlap = 0.0
		total = len(q1) + len(q2)
		for w in q1:
			if w in q2_set: overlap+=1
		for w in q2:
			if w in q1_set: overlap+=1

		# set predicted value dup	
		if overlap/total >= thr: dup = 1
		else: dup = 0
		# check if prediction matches target
		if dup == sample[2]: acc+=1 
	acc = acc/len(dataset)
	print "Threshold: %f, Accuracy: %f" %(thr,acc)


print 'Preprocessing Data...'
dataset = preprocess(sys.argv[1])

print 'Computing Accuracy...'
ComputeAccuracy(float(sys.argv[2]))	
