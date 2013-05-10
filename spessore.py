def Barcode(nome):
    from xml.dom.minidom import parse
    from simplySvg import createLine
    file = open(nome + '.svg', 'a+')
    file.write('<?xml version="1.0" standalone="no"?>' + '\n' + '<svg width="'+ str(215) + '" height="'+ str(50) + '" version="1.1" xmlns="http://www.w3.org/2000/svg">' + '\n')
    parser = parse("/home/andrea/Scrivania/PyRe/BarCode-Python/data/Code39.xml") 
    carattere = parser.getElementsByTagName('carattere')
    startX = 0
    stroke = 1
    for lettera in nome:
       for node in carattere:
           name = node.getAttribute('name')
           code = node.childNodes[0].nodeValue
           if lettera == name:
               for a in range(0, 11):
                   if code[a] == code[a+1]:
                       stroke += 1
                       print "Nella lettera " + lettera + ", " + code[a] + " = " + code[a+1] + " EVVAI"
                       print stroke
                   stroke = 1