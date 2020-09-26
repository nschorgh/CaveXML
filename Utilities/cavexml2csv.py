#! /usr/bin/env python3

# This Python script converts a CaveXML database into csv format. Repeat entries
# for the same element are merged so they fit into a single column. It also
# converts DOIs into hyperlinks.


import xml.etree.ElementTree as ET
import csv

tree = ET.parse('../allcaves-database.xml')
root = tree.getroot()



def merge_elements(stuff):
    if stuff is not None and len(stuff)>0:
        str = stuff[0].text
        for i in range(1,len(stuff)):  # merge multiple entries
            if stuff[i].text is not None:
                str = str + "; " + stuff[i].text
    else:
        str = ""
    return str



# open file for writing
thedata = open('tmp.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(thedata)

record_head = []
elementList = ['country-name','state-or-province','phys-area-name',
               'principal-cave-name','other-cave-name','latitude','longitude',
               'altitude','length','vertical-extent','number-of-entrances',
               'rock-type','cave-type','contents','ice-deposit-type','comments',
               'cave-system','branch-name','reference','cave-use']

for i in range(0,len(elementList)):
    record_head.append(elementList[i])

csvwriter.writerow(record_head)


count = 0
for item in root.findall('record'):
    record = []
    count = count + 1

    country = item.findall('country-name')
    str = merge_elements(country)
    record.append(str)
        
    sop = item.findall('state-or-province')
    str = merge_elements(sop)
    record.append(str)

    pan = item.findall('phys-area-name')
    str = merge_elements(pan)
    record.append(str)
    
    pcn = item.find('principal-cave-name') # maxOccurs=1
    if pcn is not None:
        record.append(pcn.text)
    else:
        record.append("")
    
    ocn = item.findall('other-cave-name')
    str = merge_elements(ocn)
    record.append(str)

    lat = item.find('latitude') # maxOccurs=1, decimal
    if lat is not None:
        record.append(lat.text)
    else:
        record.append("")
        
    lon = item.find('longitude') # maxOccurs=1, decimal
    if lon is not None:
        record.append(lon.text)
    else:
        record.append("")

    alt = item.findall('altitude') 
    str = merge_elements(alt)
    record.append(str)

    length = item.find('length') # maxOccurs=1, EUI
    if length is not None:
        record.append(length.text)
    else:
        record.append("")

    vex = item.find('vertical-extent') # maxOccurs=1, EUI
    if vex is not None:
        record.append(vex.text)
    else:
        record.append("")

    nre = item.find('number-of-entrances') # maxOccurs=1, EUI
    if nre is not None:
        record.append(nre.text)
    else:
        record.append("")

    rot = item.findall('rock-type')
    str = merge_elements(rot)
    record.append(str)
        
    cat = item.findall('cave-type')
    str = merge_elements(cat)
    record.append(str)

    cont = item.findall('contents')
    str = merge_elements(cont)
    record.append(str)
    
    idt = item.findall('ice-deposit-type')
    str = merge_elements(idt)
    record.append(str)
    
    comm = item.findall('comments')
    str = merge_elements(comm)
    record.append(str)

    sys = item.find('cave-system') # maxOccurs=1
    if sys is not None:
        record.append(sys.text)
    else:
        record.append("")
    
    branch = item.findall('branch-name')
    str = merge_elements(branch)
    record.append(str)

    ref = item.findall('reference')
    str = merge_elements(ref)
    str = str.replace("doi:", "https://doi.org:")
    record.append(str)
    
    caveuse = item.findall('cave-use')
    str = merge_elements(caveuse)
    record.append(str)
        
    csvwriter.writerow(record)

    
thedata.close()
print('Number of records:', count)
