#!/usr/bin/python2.7
import sys
import time
from preprocess import preprocess

dataset = []
freqs = {}
stops = set()

def FindStops():
	try: # load stop words
		f = open('stops.txt')
		print 'Loading Stop Words...'
		for w in f:
			stops.add(w[:-1])
		f.close()	
	except IOError:	# first run: find stop words
		print 'Finding Stop Words...'
		for sample in dataset:
			words = sample[0] + sample[1]
			for w in words: 
				if freqs.has_key(w): freqs[w]+=1
				else: freqs[w] = 1
		f = open('stops.txt','w')
		for k in freqs:
			if freqs[k] >= 10000: 
				stops.add(k)
				f.write(k+'\n')
		f.close()	
		

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
			if w not in stops: # only check for overlap if not a stop word
				if w in q2_set: overlap+=1
			else: total -= 1 # if stop word, decrement it from total words
		for w in q2:
			if w not in stops:
				if w in q1_set: overlap+=1
			else: total -= 1	
		if total > 0:
			if overlap/total >= thr: dup = 1
			else: dup = 0

			if dup == sample[2]: acc+=1
		else: # if all words are stop words, overlapping score is zero 
			if sample[2] == 0: acc+=1
				
	print "Threshold: %f, Accuracy: %f" %(thr, acc/len(dataset))


print 'Preprocessing Data...'
dataset = preprocess(sys.argv[1])

FindStops()

print 'Computing Accuracy...'
ComputeAccuracy(float(sys.argv[2]))