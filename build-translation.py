#!/usr/bin/python

import csv
import pprint
import plistlib
import argparse
import shutil


parser = argparse.ArgumentParser(description='Build translated Alpha State Explorer template.')
parser.add_argument('srcTemplate')
parser.add_argument('translationCSV')
parser.add_argument('outputDir')

args = parser.parse_args()

src_template = args.srcTemplate
filename_csv = args.translationCSV
output_dir = args.outputDir

pp = pprint.PrettyPrinter(indent=4)


# a wrapper around csv.reader
# from http://docs.python.org/2/library/csv.html#csv-examples

def unicode_csv_reader(csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(csv_data,
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [cell.decode('utf-8') for cell in row]


class Translations:
	def __init__(self,input,languages,src_xml):
		self.input = input
		self.languages = languages;
		self.check_count = 0
		self.maps = {}
		self.alpha = None
		self.state = None
		for l in languages: 
			self.maps[l] = plistlib.readPlist(src_xml)
			#{"method-name":"Essence Kernel"}

	def add_alpha(self,row):
		print "\n--- Alpha: %s / %s ---" % (row[1],row[2])
		self.alpha = row[1].strip()
		name = row[1] + '-name'
		description = row[1] + '-description'
		i = 0
		for l in languages:
			self.maps[l][name] = row[1+i]
			i += 1
				
		row = self.input.next()
		i = 0
		for l in languages:
			self.maps[l][description] = row[1+i]
			i += 1
	
	def add_state(self,row):
		print "State: %s" % row[1]
		self.state = row[1].strip()
		name = "%s-%s-name" % (self.alpha, self.state)
		description = "%s-%s-description" % (self.alpha, self.state)
		self.check_count = 1
		
		i = 0
		for l in languages:
			self.maps[l][name] = row[1+i]
			i += 1
				
		row = self.input.next()
		i = 0
		for l in languages:
			self.maps[l][description] = row[1+i]
			i += 1		
	
	def add_check_item(self,row):
		#print "%d: %s" % (self.check_count, row[1])
		description = "%s-%s-check%d-description" % (self.alpha, self.state, self.check_count)

		i = 0
		for l in languages:
			if row[1+i]:
				self.maps[l][description] = row[1+i]
			i += 1

		self.check_count += 1

	
	def output(self,dir):
		for l in t.languages:
			if not l == 'en':
				plistlib.writePlist(self.maps[l], "%s/locale/%s.xml" % (dir,l) )



###############   main part   ##################


# XXX need to check the input values; specifically,
# check that the src_template dir exists, and has needed files
if src_template == output_dir:
	raise Exception('output directory is the same as src')

# XXX need to check if copied succesfully
shutil.copytree( src_template, output_dir );

# XXX posibly, need a command-line option as a switch for overwriting the output


t = None

with open(filename_csv, 'rb') as CSV:
	input = unicode_csv_reader( CSV )
	
	# row 1
	languages = input.next()
	lang_count = len(languages)
	languages = languages[1:lang_count]
	t = Translations(input, languages, "%s/locale/en.xml" % src_template )
	
	pp.pprint( languages )
	
	# row 2
	sources = input.next()
	# row 3
	input.next()
	
	# further rows
	for row in input:
		if row[0] == 'A':
			t.add_alpha( row )
		elif row[0] == 'S':
			t.add_state(row) 
		elif row[0] == '' and row[1] and row[1].count(' ') == 0:
			t.add_state(row)
		elif row[1]:
			t.add_check_item(row) 
		#if row[0] or row[1]:
		#	print ', '.join(row)


t.output(output_dir)

#pp.pprint( t.maps['ru'] )
