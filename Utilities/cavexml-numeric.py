#! /usr/bin/env python3

# This Python script converts the near-numerical entries of a CaveXML database
# into fully numerical entries and outputs them in a file which can be used to
# support search functionality.

import xml.etree.ElementTree as ET
import csv
import re
from cavexml import parse_ExtendedUnsignedInteger, parse_AltitudeEntry

tree = ET.parse('../allcaves-database.xml')
root = tree.getroot()



# open files for writing
thenumbers = open('tmp-numeric.csv', 'w')

# create the csv writer object
csvwriter_nr = csv.writer(thenumbers)


record_head = []
record_head.append('principal-cave-name')
record_head.append('min_altitude')
record_head.append('max_altitude')
record_head.append('length')
record_head.append('vertical-extent')
record_head.append('number-of-entrances')
csvwriter_nr.writerow(record_head)


count = 0
for item in root.findall('record'):
    record = []
    record_nr = []
    count = count + 1

    pcn = item.find('principal-cave-name') # maxOccurs=1
    if pcn is not None:
        record_nr.append(pcn.text)        
    else:
        record_nr.append("")
    
    alt = item.findall('altitude') 
    minmax = parse_AltitudeEntry(alt)
    record_nr.append(minmax[0])
    record_nr.append(minmax[1])

    length = item.find('length') # maxOccurs=1, EUI
    if length is not None:
        number = parse_ExtendedUnsignedInteger(length.text)
        record_nr.append(number)
    else:
        record_nr.append("")

    vex = item.find('vertical-extent') # maxOccurs=1, EUI
    if vex is not None:
        number = parse_ExtendedUnsignedInteger(vex.text)
        record_nr.append(number)
    else:
        record_nr.append("")

    nre = item.find('number-of-entrances') # maxOccurs=1, EUI
    if nre is not None:
        number = parse_ExtendedUnsignedInteger(nre.text)
        record_nr.append(number)
    else:
        record_nr.append("")


    csvwriter_nr.writerow(record_nr)
        


thenumbers.close()
print('Number of records:', count)
