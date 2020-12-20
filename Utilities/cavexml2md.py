#! /usr/bin/env python3

# This Python script outputs CaveXML database entries in Markdown format.
# It only outputs a subset of the elements, and creates one line per record.

import xml.etree.ElementTree as ET
from cavexml import *

tree = ET.parse('../allcaves-database.xml')
root = tree.getroot()

MDNL = '  \n'  # Markdown newline

# open file for writing
f = open("tmp.md","w")


def output_one_line_md(item):
    # output selected entries only, one line per record
    
    country = item.findall('country-name')
    outstr = merge_elements(country)
    if outstr:
        f.write(outstr)
        
    sop = item.findall('state-or-province')
    outstr = merge_elements(sop)
    if outstr:
        f.write(' - ' + outstr)

    pan = item.findall('phys-area-name')
    outstr = merge_elements(pan)
    if outstr:
        f.write(' - ' + outstr)

    uid = generate_unique_id(item)
    f.write(" [")                                  # open link
        
    pcn = item.find('principal-cave-name')
    if pcn is not None:
        if pcn.text is not None:
            f.write('**' + pcn.text + '** ')
    
    ocn = item.findall('other-cave-name')
    outstr = merge_elements(ocn)
    if outstr:
        f.write(' ' + outstr)

    cid = item.findall('cave-id')
    outstr = merge_elements(cid)
    if outstr is not None:
        f.write(' ' + outstr)

    f.write("](allcaves-database.md#" + uid + ")" ) # close link
        
    alt = item.findall('altitude')
    outstr = merge_elements(alt)
    if outstr:
        f.write(' ' + outstr + 'm')

    cavsys = item.find('cave-system') 
    if cavsys is not None:
        if cavsys.text:
            f.write(' *Part of* '+cavsys.text)

    length = item.find('length')
    number = 0
    if length is not None:
        number, approx, qual = parse_ExtendedUnsignedInteger(length.text)
    #if number is not None:
    #    f.write(' '+str(number)+'m')
        
    f.write(MDNL)


    
# main loop
count = 0
for item in root.findall('record'):

    ### downselect
    
    if is_this_an_ice_cave(item):
    #if is_this_an_ice_cave(item) and is_this_a_lava_tube(item):
        pass
    else:
        continue

    alt = item.findall('altitude') 
    minmax = parse_AltitudeEntry(alt)
    #if minmax[1]>=3000:
    #    pass
    #else:
    #    continue

    
    ###
        
    count += 1

    output_one_line_md(item)
    
        

    
print('Wrote file tmp.md')
print('Number of records:', count)

f.close()

# sort tmp.md > list-of-ice-caves.md
# pandoc list-of-ice-caves.md --from=gfm --pdf-engine=wkhtmltopdf --output tmp.pdf
