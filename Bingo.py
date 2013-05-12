def Barcode(nome):
    from xml.dom.minidom import parse
    from simplySvg import createLine
    scelta = int(input("Scegli il tipo di codifica: "))
    spessore = 4
    grandezza = spessore*12*18 + spessore*17
    file = open(nome + "_" + str(scelta) + '.svg', 'a+')
    file.write('<?xml version="1.0" standalone="no"?>' + '\n' + '<svg width="'+ str(grandezza + 10) + '" height="'+ str(74) + '" version="1.1" xmlns="http://www.w3.org/2000/svg">' + '\n')
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
                print "INIZIO CODICE A BARRE RELATIVO ALLA LETTERA " + lettera + " -- " + code
                inizio = createLine(startX, 0, startX, 74,"black", spessore)
                #print startX, 1, "black"
                file.write(inizio)
                print inizio
                startX = startX + spessore
                for a in range(1, len(code)-1):
                    elem = ""
                    if code[a] == "1":
                        colore = "black"
                    elif code[a] == "0":
                        colore = "white" 
                    #if (code[a] != code[a-1] and code[a] == code[a+1]):
                     #   startX -= 1
                    #elif (code[a] == code[a-1] and code[a] != code[a+1]):
                    #    spessore = 2
                    #elif (code[a] != code[a-1] and code[a] != code[a+1]):
                    #    spessore = 1
                    elem = createLine(startX, 0, startX, 74, colore, spessore)
                    print elem
                    file.write(elem)
                    startX += spessore
                    #print elem
                ultimo = createLine(startX, 0, startX, 74, "black", spessore)
                file.write(ultimo)
                print ultimo
                startX += spessore
                if startX < grandezza:
                    spazio = createLine(startX, 0, startX, 74, "white", spessore)
                    print spazio
                #print "SPAZIO"
                #print startX, spessore, colore
                #print "FINE DEL CODICE A BARRE RELATIVO ALLA LETTERA " + lettera
                    file.write(spazio)
                    startX += spessore
    file.write('</svg>')
    file.close
