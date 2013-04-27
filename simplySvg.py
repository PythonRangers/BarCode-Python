#===============================================================================
# This module is usefull to create simply a new .svg file
# 
# Created on: 24/apr/2013
# Last modified on: 27/apr/2013
# Author: pincopallino93
#===============================================================================
def createSvg(name, width, height):
    #@param: name; string; The name of the new file
    #@param: width; integer; The width of the new file
    #@param: height; integer; The height of the new file
    #@return: file.name; string; The path name of the new file
    file = open(name + '.svg', 'w')
    file.write('<?xml version="1.0" standalone="no"?>' + '\n' + '<svg width="'+ str(width) + '" height="'+ str(height) + '" version="1.1" xmlns="http://www.w3.org/2000/svg">' + '\n')
    file.close()
    return file.name
def addElem(svg,elem):
    #@param: svg; string; The path name of the file to which I want to add elements
    #@param: elem; string; Element to append
    file = open(svg, 'a+')
    lines = file.readlines()
    counter = False
    for line in lines:
        if line == "</svg>":
            counter = True        
    if counter == True:
        open(svg, 'w').writelines(lines[:-1])   
    file.write(elem)
    file.close
def saveSvg(svg):
    #@param: svg; string; The path name of the file I want to close
    file = open(svg, 'a+')
    for line in file:
        counter = True
        if line != "</svg>":
            counter = False
    if counter == False:
        file.write("</svg>")
    file.close
def createLine(x1, y1, x2, y2, color, stroke):
    #@param: x1; integer; The x-axis coordinate of the start of the line
    #@param: y1; integer; The y-axis coordinate of the start saof the line
    #@param: x2; integer; The x-axis coordinate of the end of the line
    #@param: y2; integer; The y-axis coordinate of the end of the line
    #@param: color; string; The color of new line (e.g. red)
    #@param: stroke; string; The stroke width of new line (e.g. 2)
    #@return: line; integer; Code of new line
    line = '<line x1="'+ str(x1) + '" y1="' + str(y1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '" stroke="' + color + '" stroke-width="' + str(stroke) + '" />' + '\n'
    return line