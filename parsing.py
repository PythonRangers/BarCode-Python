def codiceCatasto(PROV,COMU):
#@param PROV: string; Sigla provincia (es. RM)
#@param COMU: string; Nome comune (es. ZAGAROLO)
#@return: codeCom: string; Codice del comune (es. M141)
    from xml.dom.minidom import parse, parseString
    dom = parse("Comuni.xml")
    provincia = dom.getElementsByTagName('provincia')
    for node in provincia:
        codeProv = node.getAttribute('code')
        if codeProv == PROV:   
            comuniList = node.getElementsByTagName('comune')
            for comune in comuniList:
                codeCom = comune.childNodes[0].nodeValue
                nameCom = comune.getAttribute('name')
                if nameCom == COMU:
                    return codeCom