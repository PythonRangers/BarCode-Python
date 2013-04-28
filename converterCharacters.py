#===============================================================================
# This module is usefull to create an .xml file of characters from a .csv
# 
# Created on: 27/apr/2013
# Last modified on: 28/apr/2013
# Author: pincopallino93
#===============================================================================
# WARNING!!! Some characters are not read correctly by .xml and for this there is 
# an error in the parsing. It is necessary to correct them manually (because of 
# programmer's laziness :D):
# " = &#34; 
# & = &#38;
# < = &#60; 
from csv import reader
csvFile = 'Caratteri.csv'
openCsv = open(csvFile)
xmlFile = 'Caratteri.xml'
csvData = reader(openCsv)
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<caratteri>' + "\n")
for row in csvData:
    xmlData.write('    <carattere name="' + row[0] + '">' + row[1] + '</carattere>' + "\n")     
xmlData.write('</caratteri>' + "\n")
xmlData.close()