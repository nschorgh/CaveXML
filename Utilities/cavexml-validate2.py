#! /usr/bin/env python3

print('This script validates aspects of the CaveXML standard that are ')
print('   not already validated by cavexml.xsd.')
print()

import xml.etree.ElementTree

# Enter name of XML database here
#tree = xml.etree.ElementTree.parse('test.xml')
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()

# These elements can occur at most once
maxOccurslist = ['principal-cave-name','latitude','longitude','length',
                 'vertical-extent','number-of-entrances','cave-system']



count = 0
valid = True

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

    ocn = item.findall('other-cave-name')
    for i in range(0,len(ocn)):
        str = ocn[i].text
        if str is not None: # not empty
            str = str.strip()
            if len(str)>0:
                acavename = True
                
    if acavename is False:
        print('ERROR: Neither principal nor other cave name',count)
        valid = False


    # Test maxOccurs=1
    for i in range(0,len(maxOccurslist)):
        h = item.findall(maxOccurslist[i])
        if h is not None:
            if len(h)>1:
                print('ERROR: More than one element for',
                      pcn,maxOccurslist[i],len(h))
                valid = False

        
                
print('')
if valid:
    print('Additional validations passed')
else:
    print('This database violates CaveXML standards')

print('Number of records:', count)
