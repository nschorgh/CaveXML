#! /usr/bin/env python3

print('This script issues warnings about CaveXML database entries.')
print()

import xml.etree.ElementTree

# Enter name of XML database here
#tree = xml.etree.ElementTree.parse('test.xml')
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()

count = 0

for item in root.findall('record'):
        
    count = count + 1  # count number of records
    
    # Find records that have neither a principal-cave-name nor any other-cave-name
    acavename = False
    pcn = item.findall('principal-cave-name')
    if len(pcn)>0: # tag present
        pcn = pcn[0].text
        if pcn is not None: # not empty
            str = pcn.strip() # strips leading and trailing whitespace
            if len(str)>0:
                acavename = True

    if acavename is False:
        print('WARNING: record without principal-cave-name')

    ocn = item.findall('other-cave-name')
    for i in range(0,len(ocn)):
        str = ocn[i].text
        if str is not None: # not empty
            str = str.strip()
            if len(str)>0:
                acavename = True
                
    if acavename is False:
        print('WARNING: Neither principal nor other cave name',count)


    # Find records without reference
    try:
        ref = item.find('reference').text
        if ref is None:
            print('WARNING: no reference for ',pcn)
    except:
        pass
        
                
print('')

print('Number of records:', count)
