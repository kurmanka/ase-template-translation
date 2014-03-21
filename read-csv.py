#!/usr/bin/python

import pprint
import csv

filename = 'EssenceAlphaStateTranslation.csv'

languages = ();

def alpha(row):
	global translation
	print "\n--- Alpha: %s / %s ---" % (row[1],row[2])
	row = translation.next()
	no = 0
	for l in languages:
		no = no+1
		print '%s: %s' % (l, row[no])


def state(row):
	global translation
	print "State: %s" % row[1]
	

with open(filename, 'rb') as CSV:
	translation = csv.reader( CSV )
	
	# row 1
	languages = translation.next()
	lang_count = len(languages)
	languages = languages[1:lang_count]
	pp = pprint.PrettyPrinter(indent=4).pprint( languages )
	
	# row 2
	sources = translation.next() 
	# row 3
	translation.next()
	
	# further rows
	for row in translation:
		if row[0] == 'A':
			alpha( row )
		if row[0] == 'S':
			state(row) 
		if row[0] == '' and row[1] and row[1].count(' ') == 0:
			state(row)
		#if row[0] or row[1]:
		#	print ', '.join(row)
			

