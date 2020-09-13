#! /usr/bin/env python3

# This Python script converts a CaveXML database into csv format. Repeat entries
# for the same element are merged so they fit into a single column. The script
# also outputs a second file that converts near-numerical entries into fully
# numerical entries, which can be used to support search functionality.

import xml.etree.ElementTree as ET
import csv
import re

#tree = ET.parse('../icecave-database.xml')
#tree = ET.parse('../lavatube-database.xml')
tree = ET.parse('allcaves-database.xml')
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


def parse_ExtendedUnsignedInteger(eui):
    if eui is None:
        return

    # test whether input is ExtendedUnsignedInteger
    matched = re.fullmatch("[~>]?[0-9]+[+]?", eui.strip())
    if matched is None:
        print('Error:',eui,'is not an ExtendedUnsignedInteger')
        return

    # extract number
    number = [int(s) for s in re.findall(r'\b\d+\b',eui)]
    number = number[0]

    # set defaults
    qualifier = ''
    approx = False

    # determine meaning of characters, if present
    if len(eui)>0:
        first_char = eui[0]
        if first_char=="~":
            approx = True
        if first_char==">":
            qualifier = '>'

        last_char = eui[len(eui)-1]
        if last_char == '+':
            qualifier = '+'
            
    #print(eui,qualifier,number,approx)
    return number



def parse_AltitudeEntry(alt):

    lownumber = +99999; highnumber = -99999

    for i in range(0,len(alt)):
        str = alt[i].text
        if str is not None:
            if "-" in str or "–" in str: # altitude range
                if "-" in str:
                    hyphen = '-'
                if "–" in str:
                    hyphen = '–'
                minalt = int(str.split(hyphen)[0])
                maxalt = int(str.split(hyphen)[1])
                if minalt<lownumber:
                    lownumber = minalt
                if maxalt>highnumber:
                    highnumber = maxalt
            else:  # ExtendedUnsignedInteger optionally followed by comment
                str = str.strip()
                if len(str.split(' '))>1:  
                    str = str.split(' ')[0]  # strip comment to make it an EUI
                number = parse_ExtendedUnsignedInteger(str)
                if number<lownumber:
                    lownumber = number
                if number>highnumber:
                    highnumber = number
                
    if lownumber>highnumber:  # fits initialization
        lownumber = ""; highnumber = ""
        
    return lownumber, highnumber



# open files for writing
thedata = open('tmp.csv', 'w')
thenumbers = open('tmp-numeric.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(thedata)
csvwriter_nr = csv.writer(thenumbers)

record_head = []
elementList = ['country-name','state-or-province','phys-area-name',
               'principal-cave-name','other-cave-name','latitude','longitude',
               'altitude','length','vertical-extent','number-of-entrances',
               'rock-type','cave-type','contents','ice-deposit-type','comments',
               'cave-system','branch-name','reference','cave-use']

for i in range(0,len(elementList)):
    record_head.append(elementList[i])

csvwriter.writerow(record_head)

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

    country = item.find('country-name') 
    if country is not None:
        record.append(country.text)
    else:
        record.append("")
    
    sop = item.findall('state-or-province')
    str = merge_elements(sop)
    record.append(str)

    pan = item.findall('phys-area-name')
    str = merge_elements(pan)
    record.append(str)
    
    pcn = item.find('principal-cave-name') # maxOccurs=1
    if pcn is not None:
        record.append(pcn.text)
        record_nr.append(pcn.text)        
    else:
        record.append("")
        record_nr.append("")
    
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
    minmax = parse_AltitudeEntry(alt)
    record_nr.append(minmax[0])
    record_nr.append(minmax[1])

    length = item.find('length') # maxOccurs=1, EUI
    if length is not None:
        record.append(length.text)
        number = parse_ExtendedUnsignedInteger(length.text)
        record_nr.append(number)
    else:
        record.append("")
        record_nr.append("")

    vex = item.find('vertical-extent') # maxOccurs=1, EUI
    if vex is not None:
        record.append(vex.text)
        number = parse_ExtendedUnsignedInteger(vex.text)
        record_nr.append(number)
    else:
        record.append("")
        record_nr.append("")

    nre = item.find('number-of-entrances') # maxOccurs=1, EUI
    if nre is not None:
        record.append(nre.text)
        number = parse_ExtendedUnsignedInteger(nre.text)
        record_nr.append(number)
    else:
        record.append("")
        record_nr.append("")

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
    csvwriter_nr.writerow(record_nr)
        
thedata.close()
print('Number of records:', count)
