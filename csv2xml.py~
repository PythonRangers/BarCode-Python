<<<<<<< HEAD
=======
#prova
>>>>>>> origin/master
import csv
csvFile = 'ITALIA1.csv'
xmlFile = 'ITALIA.xml'
csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<comuni>' + "\n")
tags = ["code", "prov", "name"]
province = ["AG","AL","AN","AO","AP","AQ","AR","AT","AV","BA","BG","BI","BL","BN","BO","BR","BS","BT","BZ","CA","CB","CE","CH","CI","CL","CN","CO","CR","CS","CT","CZ","EN","FC","FE","FG","FI","Fiume","FM","FR","GE","GO","GR","IM","IS","KR","LC","LE","LI","LO","LT","LU","MB","MC","ME","MI","MN","MO","MS","MT","MU","NA","NO","NU","OG","OR","OT","PA","PC","PD","PE","PG","PI","PL","PN","PO","PR","PT","PU","PV","PZ","RA","RC","RE","RG","RI","RM","RN","RO","SA","SI","SO","SP","SR","SS","SV","TA","TE","TN","TO","TP","TR","TS","TV","UD","VA","VB","VC","VE","VI","VR","VS","VT","VV","ZA"]
for pro in province:
    print(pro)
    xmlData.write('  <provincia code="' + pro + '">' + "\n")
    for row in csvData:
        if row[1] == pro:
            xmlData.write('    <comune ' + tags[2] + '="' + row[2] + '">' + row[0] +'</comune>' + "\n")     
    xmlData.write('  </provincia>' + "\n")
xmlData.write('</comuni>' + "\n")
xmlData.close()
