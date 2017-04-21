#!/usr/bin/python2.7
import sys
import time
from preprocess import preprocess

dataset = [] # stores data from file

def ComputeScore():
	global dataset
	scores = []
	acc = 0.0
	for sample in dataset:
		q1 = sample[0]
		q2 = sample[1]
		q1_set = set(q1)
		q2_set = set(q2)
		overlap = 0.0
		total = len(q1) + len(q2)
		for w in q1: # count overlaps of q1 words in q2
			if w in q2_set: overlap+=1
		for w in q2: # count overlaps of q2 words in q1
			if w in q1_set: overlap+=1

		scores.append(overlap/total)
	for i,s in enumerate(scores[:10]): 
		print '%.3f,' %s,
	print '\n'	
	t = (min(scores),max(scores),sum(scores)/len(scores))
	print 'Min Score: %f, Max Score: %f, Mean Score: %f' %t		

dataset = preprocess(sys.argv[1])
ComputeScore()
