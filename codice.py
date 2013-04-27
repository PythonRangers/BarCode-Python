vocali = "AEIOU"
consonanti = "BCDFGHLMNPQRSTVZ"
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
corr = ["a", "b", "c", "d", "e", "h", "l", "m", "p", "r", "s", "t"]
mesi = [ "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12" ]
contr =["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",",w","x","y","z"]
num_corrisp_p = [1,0,5,7,9,13,15,17,19,21,1,0,5,7,9,13,15,17,19,21,2,4,18,20,11,3,6,8,12,14,16,10,22,25,24,23]
num_corrisp_d = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def codiceCatast(PROV,COMU):
#@param PROV: string; Sigla provincia (es. RM)
#@param COMU: string; Nome comune (es. ZAGAROLO)
#@return: codeCom: string; Codice del comune (es. M141)
    from xml.dom.minidom import parse
    dom = parse("/home/pcx/Documenti/workspace/csv2xml/Comuni.xml")
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

def main():
  x = raw_input("Nome: ") #richiede un tipo di dato "stringa" per il nome
  x = x.upper()
  y = raw_input("Cognome: ") #richiede un tipo di dato "stringa" per il cognome
  y = y.upper()
  data = str(raw_input("Data di nascita: (formato 'ggmmaaaa'): ")) #trasforma l'input numerico della data di nascita in una stringa
  sesso = raw_input("Sesso (m/f): ")
  comune = (raw_input("Comune di nascita: ")).upper()
  provincia = (raw_input("Provincia di nascita (**): ")).upper()
  me = data[2:4]
  indice = mesi.index(me) #trova a quale indice corrisponde quel numero 
  mese = corr[indice]
  n = 0 #inizializzazione variabile per scorrere nella stringa del nome
  c = 0 #inizializzazione variabile per scorrere nella stringa del cognome
  nome = "" #creazione di una stringa vuota per il nome
  cognome = "" #creazione di una stringa vuota per il cognome
  nome_voc = [] #array vuoto per le consonanti nel nome
  nome_cons = [] #array vuoto per le vocali nel nome
  cognome_voc = [] #array vuoto per le vocali nel cognome
  cognome_cons = [] #array vuoto per le consonanti nel cognome
  for n in range(0, len(x)):
    if x[n] in consonanti:
      nome_cons.append(x[n]) #aggiunge all'array che si occupa delle consonanti del nome, le consonanti del nome
    elif x[n] in vocali:
      nome_voc.append(x[n]) #aggiunge all'array che si occupa delle vocali del nome, le vocali del nome
  for c in range(0, len(y)):
    if y[c] in consonanti:
      cognome_cons.append(y[c]) #aggiunge all'array che si occupa delle consonanti del cognome, le consonanti del cognome
    elif y[c] in vocali:
      cognome_voc.append(y[c]) #aggiunge all'array che si occupa delle vocali del cognome, le vocali del cognome
  while len(nome) < 3:
    if len(nome_cons) == 1:
      nome = str(nome_cons[0] + nome_voc[0] + nome_voc[1])
    if len(nome_cons) == 2:
      nome = str(nome_cons[0] + nome_cons[1] + nome_voc[0])
    if len(nome_cons) == 3:
      nome = str(nome_cons[0] + nome_cons[1] + nome_cons[2])
    if len(nome_cons) > 3:
      nome = str(nome_cons[0] + nome_cons[2] + nome_cons[3]) 
  while len(cognome) < 3:
    if len(cognome_cons) == 1:    
      cognome = str(cognome_cons[0] + cognome_voc[0] + cognome_voc[1])
    if len(cognome_cons) == 2:    
      cognome = str(cognome_cons[0] + cognome_cons[1] + cognome_voc[0])
    if len(cognome_cons) == 3:    
      cognome = str(cognome_cons[0] + cognome_cons[1] + cognome_cons[2])
    if len(cognome_cons) > 3:
      cognome = str(cognome_cons[0] + cognome_cons[1] + cognome_cons[2])
  if sesso == "f":
    d = int(data[0:2])
    codice = cognome + nome + data[6:8] + mese + str(d + 40)
  else:
    codice = cognome + nome + data[6:8] + mese + data[0:2]
#Algoritmo per codice catastale
  CATASTO = codiceCatast(provincia,comune)
  codice = codice + CATASTO
#Algoritmo per il carattere finale di controllo  
  pari = 0
  dispari = 0
  code = codice.lower()
  for n in range(0,len(code),2):
   for x in range(0,len(contr)):
      if code[n] == contr[x]:
        pari = pari + int(num_corrisp_p[x])
  for h in range(1,len(code),2):
    for y in range(0,len(contr)):
      if code[h] == contr[y]:
        dispari = dispari + int(num_corrisp_d[y])
  cont = pari + dispari
  lett = cont % 26
  new_code = code + alfabeto[lett]

  
  print new_code.upper()
  
