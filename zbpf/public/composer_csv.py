#coding:utf-8
import csv

def getCsv(value1,value2,file_name):
	rows=[]
	with open(file_name,'r') as f:
		readers=csv.reader(f,delimiter=',',quotechar='|')
		next(readers,None)
		for row in readers:
			rows.append(row)
		return rows[value1][value2]

def getDdtCsv(file_name):
	rows=[]
	with open(file_name,'r') as f:
		readers=csv.reader(f,delimiter=',',quotechar='|')
		next(readers,None)
		for row in readers:
			rows.append(row)
		return rows

