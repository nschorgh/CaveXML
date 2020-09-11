#! /usr/bin/env python3

# Determines properties of CaveXML database entries 
print('This script validates aspects of the CaveXML standard that are ')
print('   not already validated by cavexml.xsd.')
print()

import xml.etree.ElementTree

# Enter name of XML database here
#tree = xml.etree.ElementTree.parse('../icecave-database.xml')
#tree = xml.etree.ElementTree.parse('../lavatube-database.xml')
#tree = xml.etree.ElementTree.parse('../planetary-caves.xml')
tree = xml.etree.ElementTree.parse('allcaves-database.xml')

root = tree.getroot()

# These elements can occur at most once
maxOccurslist = ['principal-cave-name','latitude','longitude','length',
                 'vertical-extent','number-of-entrances','cave-system']



count = 0
valid = True

for item in root.findall('record'):
        
    count = count + 1  # count number of records

    
    # Find records that have neither a principal-cave-name nor any other-cave-name
    pcn = item.findall('principal-cave-name')
    if len(pcn)>0:
        pcn = item.find('principal-cave-name').text
    ocn = item.findall('other-cave-name')
    if len(ocn)>0:
        str = ocn[0].text
        if (str is None) and (pcn is None):  # Both tags present but empty
            print('ERROR: Neither principal nor other cave name',count)
            valid = False
    if (pcn is None) and len(ocn)==0:
        print('ERROR: Neither principal nor other cave name',count)
        valid = False


    # Test maxOccurs=1
    for i in range(0,len(maxOccurslist)):
        h = item.findall(maxOccurslist[i])
        if h is not None:
            if len(h)>1:
                print('ERROR: More than one element for',
                      maxOccurslist[i],len(h))
                valid = False

        
    # Test whether lat/lon appear in pairs
    latitude = item.findall('latitude')
    longitude = item.findall('longitude')
    if len(latitude) is not len(longitude):
        print('ERROR: unpaired latitude or longitude', count, pcn)
        valid = False

        
                
print('')
if valid:
    print('Additional validations passed')
else:
    print('This database violates CaveXML standards')

print('Number of records:', count)
