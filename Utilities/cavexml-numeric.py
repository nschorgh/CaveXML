#! /usr/bin/env python3

# This Python script converts near-numerical entries into fully numerical
# entries and outputs them in a file which can be used to support search
# functionality.

import xml.etree.ElementTree as ET
import csv
import re

tree = ET.parse('../allcaves-database.xml')
root = tree.getroot()



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
