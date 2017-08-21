import os
import re
from datetime import datetime

filename = raw_input("Enter filename : ")
print filename
#filename = 'test.csv'

def csv_parser(filename):
	"""functions to read csv file and return a object list of dictionaries """
	file_open = open(filename,'r')
	file_read = file_open.read()
	file_lines = file_read.split("\r",1)
	objects = []
	objects_dict ={}
	header = []
	line_value = []

	header_line = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)",file_lines[0])
	for ele in header_line:
		#print ele.strip('\'\"')
		header.append(ele.strip('\'\" '))


	for obj in file_lines[1].split("\"\r\n"):
		line = obj.replace("\",","$@$").replace(",\"","$@$").replace("\"","").split("$@$")
		objects.append(dict(zip(header,line)))

	objects.pop(-1)

	if any('year' in d for d in objects) and any('make' in d for d in objects) and any('model' in d for d in objects):
		objects = sorted(objects, key=lambda k: (k['year'], k['make'], k['model']))
	elif any('year' in d for d in objects) and any('make' in d for d in objects):
		objects = sorted(objects, key=lambda k: (k['year'], k['make']))
	elif any('year' in d for d in objects):
		objects = sorted(objects, key=lambda k: (k['year']))

	for i in objects:
		if 'entrydate' in i.keys():
			datestr = i['entrydate']
			i['entrydate'] = datetime.strptime(datestr, '%b %d %Y %I:%M:%S:%f%p')

	"""for i in objects:
		print i['year'] + " " + i["make"] + " " + i["model"]"""
	return objects


if __name__ == '__main__':
	csv_parser(filename)
		
