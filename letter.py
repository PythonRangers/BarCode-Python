#===============================================================================
# This module contains three functions: the first finds the equivalent code of 
# a letter in the .xml file, the second returns the code in order to write a  
# .svg file following the standard Code 128 and the third, the main, creates the 
# bar code through a word
# 
# Created on: 27/apr/2013
# Last modified on: 28/apr/2013
# Author: pincopallino93
#===============================================================================
def makeLetter(letter):
#@param: letter; string; The letter 
    from xml.dom.minidom import parse
    dom = parse("/home/pcx/Documenti/workspace/csv2xml/Caratteri.xml")
    carattere = dom.getElementsByTagName('carattere')
    for node in carattere:
        name = node.getAttribute('name')
        code = node.childNodes[0].nodeValue
        if name == letter:
            return code
def svgLetter(code,j):
#@param: code; string; The letter code returned from makeLetter    
    from simplySvg import createLine
    i = 0
    codeSvg = []
    for value in code:
        if value == "1":
            line = createLine(i + j, 0, i + j, 50, "black", 1)
            codeSvg.append(line)
        elif value == "0":
            line = createLine(i + j, 0, i + j, 50, "white", 1)
            codeSvg.append(line)
        i = i + 1
    return codeSvg
def main(word):
#@param: word; string; The world to convert in Code 128
    from simplySvg import createSvg, addElem, saveSvg
    svg = createSvg(word, 200, 200)
    j = 0
    codeWord = []
    for elem in word:
        numeri= makeLetter(elem)
        print numeri
        code = svgLetter(numeri, j) 
        j = j + 11
        for riga in code:
            addElem(svg, riga)
    saveSvg(svg)