#===============================================================================
# This module contains the two functions: the first finds the equivalent code of 
# a letter in the .xml file and the latter returns the code in order to write a  
# .svg file following the standard Code 128
# 
# Created on: 27/apr/2013
# Last modified on: 28/apr/2013
# Author: pincopallino93
#===============================================================================
def createSvg(nome, width, height):
    #@param: name; string; The name of the new file
    #@param: width; integer; The width of the new file
    #@param: height; integer; The height of the new file
    #@return: file.name; string; The path name of the new file
    from xml.dom.minidom import parse
    from simplySvg import createLine
    file = open(nome + '.svg', 'a+')
    file.write('<?xml version="1.0" standalone="no"?>' + '\n' + '<svg width="'+ str(width) + '" height="'+ str(height) + '" version="1.1" xmlns="http://www.w3.org/2000/svg">' + '\n')
    file.close
#@param: letter; string; The letter 
    dom = parse("/home/andrea/Scrivania/csv2xml/Caratteri.xml")
    carattere = dom.getElementsByTagName('carattere')
    for node in carattere:
        name = node.getAttribute('name')
        code = node.childNodes[0].nodeValue
    #@param: svg; string; The path name of the file to which I want to add elements
    #@param: elem; string; Element to append
    file = open(nome + '.svg', 'a+')
    lines = file.readlines()
    i = 0
    counter = False
    for line in lines:
        if line == "</svg>":
            counter = True        
    if counter == True:
        open(nome, 'a+').writelines(lines[:-1])
    for value in code:
        if value == "1":
            elem = createLine(i, 0, i, 200, "red", 1)
        elif value == "0":
            elem = createLine(i, 0, i, 200, "white", 1)
        i = i + 1   
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
