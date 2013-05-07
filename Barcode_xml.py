def Barcode(nome):
    from xml.dom.minidom import parse
    from simplySvg import createLine
    file = open(nome + '.svg', 'a+')
    file.write('<?xml version="1.0" standalone="no"?>' + '\n' + '<svg width="'+ str(574) + '" height="'+ str(100) + '" version="1.1" xmlns="http://www.w3.org/2000/svg">' + '\n')
    parser = parse("/home/andrea/Scrivania/PyRe/BarCode-Python/data/Code39.xml") 
    carattere = parser.getElementsByTagName('carattere')
    startX = 0
    for lettera in nome:
       print lettera
       for node in carattere:
           name = node.getAttribute('name')
           code = node.childNodes[0].nodeValue
           if lettera == name:
               for value in code:
                   if (value == "1"):
                       elem = createLine(startX, 0, startX, 100, "black", (574.0 / 216))
                   elif (value =="0"):
                       elem = createLine(startX, 0, startX, 100, "white", (574.0 / 216))
                   file.write(elem)
                   startX += (574.0 / 216)
                   print elem
               spazio = createLine(startX, 0, startX, 100, "white", (574.0 / 216))
               print spazio
               file.write(spazio)
    file.write('</svg>')
    file.close
