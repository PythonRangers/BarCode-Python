#===============================================================================
# This module contains the two functions: the first finds the equivalent code of 
# a letter in the .xml file and the latter returns the code in order to write a  
# .svg file following the standard Code 128
# 
# Created on: 27/apr/2013
# Last modified on: 28/apr/2013
# Author: pincopallino93
#===============================================================================
def Bar(nome, width, height):
    from csv import reader
    from simplySvg import createLine
    file = open(nome + '.svg', 'a+')
    file.write('<?xml version="1.0" standalone="no"?>' + '\n' + '<svg width="'+ str(width) + '" height="'+ str(height) + '" version="1.1" xmlns="http://www.w3.org/2000/svg">' + '\n')
    file.close
    code = reader(open("/home/andrea/Scrivania/PyRe/BarCode-Python/data/Code39.csv"))
    for lettera in nome:
        for row in code:
            if lettera == row[0]:
                for value in code:
                    if (value == "1"):
                        elem = createLine(startX, 0, startX, 200, "black", 1)
                    elif (value =="0"):
                        elem = createLine(startX, 0, startX, 200, "white", 1)
                    file.write(elem)
                    print elem
                file.close
                #@param: svg; string; The path name of the file I want to close
                file = open(nome + '.svg', 'a+')
                for line in file:
                    counter = True
                    if line != "</svg>":
                        counter = False
                    if counter == False:
                        file.write("</svg>")
    file.close
