#===============================================================================
# This module is usefull to create an .xml file of characters from a .csv
# 
# Created on: 27/apr/2013
# Last modified on: 27/apr/2013
# Author: pincopallino93
#===============================================================================

#ATTENZIONE!!! Alcuni caratteri non sono letti in modo corretto da xml e quindi 
#vi sono errori ed il file non può essere parsato in seconda battuta. Bisogna trovare
#il modo di passarli, penso ad una codifica del tipo http://www.guru4.net/articoli/xml-escape/ 
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