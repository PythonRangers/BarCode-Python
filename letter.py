#===============================================================================
# This module contains the two functions: the first finds the equivalent code of 
# a letter in the .xml file and the latter returns the code in order to write a  
# .svg file following the standard Code 128
# 
# Created on: 27/apr/2013
# Last modified on: 27/apr/2013
# Author: pincopallino93
#===============================================================================
def makeLetter(letter):
#@param: letter; string; The letter 
    from xml.dom.minidom import parse
    dom = parse("Caratteri.xml")
    carattere = dom.getElementsByTagName('carattere')
    for node in carattere:
        name = node.getAttribute('name')
        code = node.childNodes[0].nodeValue
        if name == letter:
            return code
def svgLetter(code):    
    from simplySvg import createLine
    i = 0
    for value in code:
        if value == "1":
            line = createLine(i, 0, i, 200, "black", 1)
        elif value == "0":
            line = createLine(i, 0, i, 200, "white", 1)
        print line
        i = i + 1