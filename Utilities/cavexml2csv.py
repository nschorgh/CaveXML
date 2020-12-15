#! /usr/bin/env python3

# This Python script converts a CaveXML database into csv format. Repeat entries
# for the same element are merged so they fit into a single column. It also
# converts DOIs into hyperlinks.


import xml.etree.ElementTree as ET
import csv
from cavexml import *

tree = ET.parse('../allcaves-database.xml')
root = tree.getroot()



# open file for writing
thedata = open('tmp.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(thedata)

record_head = []
elementList = ['country-name','state-or-province','phys-area-name',
               'principal-cave-name','other-cave-name','cave-id','latitude','longitude',
               'altitude','length','vertical-extent','number-of-entrances',
               'rock-type','cave-type','contents','comments',
               'cave-system','branch-name','reference','cave-use','curation']

for i in range(0,len(elementList)):
    record_head.append(elementList[i])

csvwriter.writerow(record_head)


count = 0
for item in root.findall('record'):

    # optional filter criteria
    #if not is_this_an_ice_cave(item):
    #    continue
    
    record = []
    count += 1

    country = item.findall('country-name')
    outstr = merge_elements(country)
    record.append(outstr)
        
    sop = item.findall('state-or-province')
    outstr = merge_elements(sop)
    record.append(outstr)

    pan = item.findall('phys-area-name')
    outstr = merge_elements(pan)
    record.append(outstr)
    
    pcn = item.find('principal-cave-name') # maxOccurs=1
    if pcn is not None:
        record.append(pcn.text)
    else:
        record.append("")
    
    ocn = item.findall('other-cave-name')
    outstr = merge_elements(ocn)
    record.append(outstr)

    cid = item.findall('cave-id')
    outstr = merge_elements(cid)
    record.append(outstr)

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
    outstr = merge_elements(alt)
    record.append(outstr)

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
    outstr = merge_elements(rot)
    record.append(outstr)
        
    cat = item.findall('cave-type')
    outstr = merge_elements(cat)
    record.append(outstr)

    cont = item.findall('contents')
    outstr = merge_elements(cont)
    record.append(outstr)

    comm = item.findall('comments')
    outstr = merge_elements(comm)
    record.append(outstr)

    sys = item.find('cave-system') # maxOccurs=1
    if sys is not None:
        record.append(sys.text)
    else:
        record.append("")
    
    branch = item.findall('branch-name')
    outstr = merge_elements(branch)
    record.append(outstr)

    ref = item.findall('reference')
    outstr = merge_elements(ref)
    if outstr:
        outstr = outstr.replace("doi:", "https://doi.org/")
        outstr = outstr.replace("DOI:", "https://doi.org/")
    record.append(outstr)
    
    caveuse = item.findall('cave-use')
    outstr = merge_elements(caveuse)
    record.append(outstr)

    cur = item.findall('curation')
    outstr = merge_elements(cur)
    record.append(outstr)

        
    csvwriter.writerow(record)

    
thedata.close()
print('Wrote file tmp.csv')
print('Number of records:', count)
