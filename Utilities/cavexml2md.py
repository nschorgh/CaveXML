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


count = 0
for item in root.findall('record'):

    if is_this_an_ice_cave(item):
        pass
    else:
        continue 
    
    count = count + 1

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

    pcn = item.find('principal-cave-name')
    if pcn is not None:
        if pcn.text is not None:
            f.write(' **' + pcn.text + '** ')
    
    ocn = item.findall('other-cave-name')
    outstr = merge_elements(ocn)
    if outstr:
        f.write(' ' + outstr)

    cid = item.findall('cave-id')
    outstr = merge_elements(cid)
    if outstr:
        f.write(' ' + outstr)

    cavsys = item.find('cave-system') 
    if cavsys is not None:
        if cavsys.text:
            f.write(' *Part of* '+cavsys.text)
    
    #branch = item.findall('branch-name')
    #outstr = merge_elements(branch)
    #f.write(outstr)

        
    f.write(MDNL)

    

print('Number of records:', count)

f.close()

# sort tmp.md > list-of-ice-caves.md
# pandoc list-of-ice-caves.md --from=gfm --pdf-engine=wkhtmltopdf --output tmp.pdf
