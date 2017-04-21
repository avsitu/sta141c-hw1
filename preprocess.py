#!/usr/bin/python2.7
import csv 

def preprocess(fn):
	dataset = [] # stores data from file
	replaced = ['?',',','!','.','(',')','\'','\"',':']
	f_in = csv.reader(open(fn))
	for row in f_in:
		q1 = row[3].lower().replace('-','')
		q2 = row[4].lower().replace('-','')

		for r in replaced: # replaces all symbols with spaces
			q1 = q1.replace(r, ' ')
			q2 = q2.replace(r, ' ')
		# strips trailing space from q1 and q2 and splits by space 	
		# appends [q1, q2, target variable] to dataset	
		dataset.append([q1.strip(' ').split(' '),q2.strip(' ').split(' '),int(row[5])])
	return dataset
