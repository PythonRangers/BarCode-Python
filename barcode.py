#===============================================================================
# This module contains three functions: the first finds the equivalent code of 
# a letter in the .xml file, the second returns the code in order to write a  
# .svg file following the standard Code 128 and the third, the main, creates the 
# bar code through a word
# 
# Created on: 27/apr/2013
# Last modified on: 02/may/2013
# Author: pincopallino93
#===============================================================================
def makeLetter(letter, code):
#@param: letter; string; The letter 
    from xml.dom.minidom import parse
  #  if code == 39:
   #     parser = parse("/data/Caratteri_39.xml")
 #   elif code == 128:
    parser = parse("/data/Caratteri.xml") 
    carattere = parser.getElementsByTagName('carattere')
    for node in carattere:
        name = node.getAttribute('name')
        code = node.childNodes[0].nodeValue
        if name == letter:
            return code
def svgLetter(code,j):
#@param: code; string; The letter code returned from makeLetter    
    from utility.simplySvg import createLine
    i = 0
    codeSvg = []
    for value in code:
        if value == "1":
            line = createLine(25 + i + j, 25, 25 + i + j, 75, "black", 1)
            codeSvg.append(line)
        elif value == "0":
            line = createLine(25 + i + j, 25, 25 + i + j, 75, "white", 1)
            codeSvg.append(line)
        i = i + 1
    return codeSvg
def codeControl(code):
    #asdfasdf
    return codeControl #array, iniziale e finale
def main(word, code):
#@param: word; string; The world to convert in Code 128
    from utility.simplySvg import createSvg, addElem, saveSvg
    lunghezza = len(word) * 11 + 50
    svg = createSvg(word + '_' + str(code), lunghezza, 100)
    #addElem(svg, codeControlInitial)
    j = 0
    codeWord = []
    for elem in word:
        caratteri = makeLetter(elem, code)
        code = svgLetter(caratteri, j) 
        j = j + 11
        for riga in code:
            addElem(svg, riga)
    #addElem(svg, codeControlFinal)
    saveSvg(svg)