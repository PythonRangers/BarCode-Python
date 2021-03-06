#===============================================================================
# This module is usefull to create an .xml file of characters from a .csv
# 
# Created on: 27/apr/2013
# Last modified on: 30/apr/2013
# Author: pincopallino93
#===============================================================================
from csv import reader
csvFile = '/data/Caratteri.csv'
openCsv = open(csvFile)
xmlFile = '/data/Caratteri.xml'
csvData = reader(openCsv)
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<caratteri>' + "\n")
for row in csvData:
    xmlData.write('    <carattere name="&#' + row[0] + ';">' + row[2] + '</carattere>' + "\n")     
xmlData.write('</caratteri>' + "\n")
xmlData.close()