def Barcode(nome):
    from xml.dom.minidom import parse
    from simplySvg import createLine
    scelta = int(input("Scegli il tipo di codifica: "))
    file = open(nome + "_" + str(scelta) + '.svg', 'a+')
    file.write('<?xml version="1.0" standalone="no"?>' + '\n' + '<svg width="'+ str(600) + '" height="'+ str(76) + '" version="1.1" xmlns="http://www.w3.org/2000/svg">' + '\n')
    parser = parse("/home/andrea/Scrivania/PyRe/BarCode-Python/data/Code" + str(scelta) + ".xml") 
    carattere = parser.getElementsByTagName('carattere')
    startX = 10
    for lettera in nome:
        print lettera
        for node in carattere:
            name = node.getAttribute('name')
            binario = node.childNodes[0].nodeValue
            code = str(binario)
            if lettera == name:
                print "INIZIO CODICE A BARRE RELATIVO ALLA LETTERA " + lettera + "  -- " + code
                inizio = elem = createLine(startX, 0, startX, 100,"black", (574.0 / 216))
                file.write(inizio)
                print startX, str(574.0 / 216), "black"
                startX = startX + (574.0 / 216)
                for a in range(1, len(code)-1):
                    elem = ""
                    if code[a] == "1":
                        colore = "black"
                    elif code[a] == "0":
                        colore = "white" 
                    if (code[a] != code[a-1] and code[a] == code[a+1]):
                        spessore = (2*574.0 / 216)
                        elem = createLine(startX, 0, startX, 100, colore, spessore)
                    elif (code[a] == code[a-1] and code[a] != code[a+1]):
                        spessore = 0
                        elem = createLine(startX, 0, startX, 100, colore, spessore) 
                    elif (code[a] != code[a-1] and code[a] != code[a+1]):
                        spessore = 574.0 / 216
                        elem = createLine(startX, 0, startX, 100, colore, spessore)
                    print startX,spessore, colore
                    file.write(elem)
                    startX += spessore
                    #print elem
                spessore = 574.0 / 216
                spazio = createLine(startX, 0, startX, 100, "white", spessore)
                print "SPAZIO"
                #print spazio
                print "FINE DEL CODICE A BARRE RELATIVO ALLA LETTERA " + lettera
                startX = startX + spessore
                file.write(spazio)
    file.write('</svg>')
    file.close