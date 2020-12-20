#! /usr/bin/env python3

# This Python script converts the near-numerical entries of a CaveXML database
# into fully numerical entries and outputs them in a file which can be used to
# support search functionality.

import xml.etree.ElementTree as ET
import csv
import re
from cavexml import parse_ExtendedUnsignedInteger, parse_AltitudeEntry
import unicodedata

tree = ET.parse('../allcaves-database.xml')
root = tree.getroot()



# open files for writing
thenumbers = open('tmp-numeric.csv', 'w')

# create the csv writer object
csvwriter_nr = csv.writer(thenumbers)


record_head = []
record_head.append('normalized-cave-name')
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
    try:
        #record_nr.append(pcn.text)
        nfkd_form = unicodedata.normalize('NFKD', pcn.text)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        back_to_native = str(only_ascii,'utf-8')
        record_nr.append(back_to_native)
    except:
        record_nr.append("")
    
    alt = item.findall('altitude') 
    minmax = parse_AltitudeEntry(alt)
    if abs(minmax[0]) != 99999:
        record_nr.append(minmax[0])
        record_nr.append(minmax[1])
    else:
        record_nr.append("")
        record_nr.append("")
        
    length = item.find('length') # maxOccurs=1, EUI
    if length is not None:
        number, approx, qual = parse_ExtendedUnsignedInteger(length.text)
        record_nr.append(number)
    else:
        record_nr.append("")

    vex = item.find('vertical-extent') # maxOccurs=1, EUI
    if vex is not None:
        number, approx, qual = parse_ExtendedUnsignedInteger(vex.text)
        record_nr.append(number)
    else:
        record_nr.append("")

    nre = item.find('number-of-entrances') # maxOccurs=1, EUI
    if nre is not None:
        number, approx, qual = parse_ExtendedUnsignedInteger(nre.text)
        record_nr.append(number)
    else:
        record_nr.append("")


    csvwriter_nr.writerow(record_nr)
        


thenumbers.close()
print('Wrote file tmp-numeric.csv')
print('Number of records:', count)
