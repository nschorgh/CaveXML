#! /usr/bin/env python3

print('This script issues warnings about CaveXML database entries.')
print()

import xml.etree.ElementTree
from cavexml import get_one_cave_name

# Enter name of XML database here
#tree = xml.etree.ElementTree.parse('test.xml')
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()



count = 0

for item in root.findall('record'):
        
    count = count + 1  # count number of records

    acavename = False
    pcn = item.find('principal-cave-name')
    if pcn is not None: # tag present
        if pcn.text is not None: # not empty
            if len(pcn.text.strip())>0:
                acavename = True
    if acavename is False:
        print('WARNING: record without principal-cave-name', count)

        
    acavename = get_one_cave_name(item)
    if len(acavename)==0:
        print('WARNING: Neither principal nor other cave name nor cave id',count)


    # Find records without reference
    try:
        ref = item.find('reference').text
        if ref is None:
            print('WARNING: no reference for ',acavename)
    except:
        pass
        
                
print('')
print('Number of records:', count)
