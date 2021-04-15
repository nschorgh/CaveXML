#! /usr/bin/env python3

# This Python script converts a CaveXML database into csv format. Repeat entries
# for the same element are merged so they fit into a single column. The script 
# also converts DOIs into hyperlinks.


import xml.etree.ElementTree as ET
import csv
from cavexml import *

tree = ET.parse('../allcaves-database.xml')
root = tree.getroot()


# open file for writing
thedata = open('tmp.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(thedata)

# list of all CaveXML elements
elementList = ['country-name','state-or-province','phys-area-name',
               'principal-cave-name','other-cave-name','cave-id','latitude','longitude',
               'altitude','length','vertical-extent','number-of-entrances','map-link',
               'rock-type','cave-type','contents','comments',
               'cave-system','branch-name','reference','cave-use','curation']

record_head = []
for i in range(0,len(elementList)):
    record_head.append(elementList[i])

csvwriter.writerow(record_head)


def element2cell(tagname):
    # element -> tabel cell entry
    # maxOccurs = 1
    buf = item.find(tagname) 
    if buf is not None:
        record.append(buf.text)
    else:
        record.append("")
        
        
def elements2cell(tagname):
    # flatten elements
    # maxOccurs = unbounded
    stuff = item.findall(tagname)
    outstr = merge_elements(stuff)
    record.append(outstr)
    
        
count = 0
for item in root.findall('record'):

    # optional filter criteria
    #if not is_this_an_ice_cave(item):
    #    continue
    
    record = []
    count += 1

    elements2cell('country-name')
    elements2cell('state-or-province')
    elements2cell('phys-area-name')
    element2cell('principal-cave-name') # maxOccurs=1
    elements2cell('other-cave-name')
    elements2cell('cave-id')
    element2cell('latitude') # maxOccurs=1
    element2cell('longitude') # maxOccurs=1
    elements2cell('altitude')
    element2cell('length') # maxOccurs=1 
    element2cell('vertical-extent') # maxOccurs=1
    element2cell('number-of-entrances') # maxOccurs=1
    elements2cell('map-link')
    elements2cell('rock-type')
    elements2cell('cave-type')
    elements2cell('contents')
    elements2cell('comments')
    element2cell('cave-system') # maxOccurs=1
    elements2cell('branch-name')    

    ref = item.findall('reference')
    refstr = merge_elements(ref)
    if refstr:
        refstr = refstr.replace("doi:", "https://doi.org/")
        refstr = refstr.replace("DOI:", "https://doi.org/")
    record.append(refstr)

    elements2cell('cave-use')
    elements2cell('curation')
        
    csvwriter.writerow(record)

    
thedata.close()
print('Wrote file tmp.csv')
print('Number of records:', count)
