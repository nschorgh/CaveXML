#! /usr/bin/env python3

print('This script issues warnings about CaveXML database entries.')
print()

import xml.etree.ElementTree
import numpy
from cavexml import get_one_cave_name

# Enter name of XML database here
#tree = xml.etree.ElementTree.parse('../../test.xml')
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()



count = 0

for item in root.findall('record'):
        
    count += 1  # count number of records

    try:
        ref = item.find('country-name').text.strip()
        if ref is None:
            print('WARNING: country-name missing', count)
    except:
        pass

    a = item.findall('country-name')
    if len(a)>1:
        print('More than one country name', count)

    
    tag = False
    pcn = item.find('principal-cave-name')
    if pcn is not None: # tag present
        if pcn.text: # not empty
            if len(pcn.text.strip())>0:  # not blank
                tag = True
    if tag is False:
        print('WARNING: record without principal-cave-name', count)
        try:
            if len(item.find('cave-system').text.strip())>0:
                print('WARNING: no principal-cave-name but part of cave system')
        except:
            pass
        try:
            if len(item.find('branch-name').text.strip())>0:
                print('WARNING: no principal-cave-name but branches', count)
        except:
            pass
    
    acavename = get_one_cave_name(item)
    if len(acavename)==0:
        print('WARNING: neither principal nor other cave name nor cave id',count)


    ref = item.find('reference')
    if ref is None:
        print('WARNING: no reference for',acavename)
    else:
        ref = ref.text.strip()
        if ref is None:
            print('WARNING: no reference for',acavename)

            
    ref = item.findall('reference')
    for i in range(0,len(ref)):
        refstr = ref[i].text
        if '//doi:' in refstr or 'doi.org:' in refstr: # should be doi: or https://doi.org/
            print('Malformatted doi', refstr)
        if 'doi' in refstr.lower():
            if 'DOI' not in refstr and 'doi' not in refstr:  # excludes comabinations such as DOi, doI
                print('Use doi or DOI', refstr)
        if 'www' in refstr:
            if "https://www" not in refstr and "http://www." not in refstr:
                print('WARNING: www could be http://www or https://www ', refstr) 

# move on to cross comparisons
print('... cross comparisons ...')

lcou = []
lcav = []
lcid = []

for item in root.findall('record'):

    con = item.findall('country-name')
    try:
        lcou.append(con[0].text)
    except:
        lcou.append(" ")
        
    aname = get_one_cave_name(item)
    lcav.append(aname)

    cid = item.findall('cave-id')
    try:
        lcid.append(cid[0].text)
    except:
        lcid.append(" ")


# find records with the same Cave-Id
for i in range(0,len(lcav)):
    idxs = [n for n,x in enumerate(lcid) if x==lcid[i] ]
    for k in range(0,len(idxs)):
        ii = idxs[k]
        if i<ii and lcou[i]==lcou[ii]:
            if lcid[i]==lcid[ii] and lcid[i]!=' ' and lcid[i] is not None: 
                print('SAME ID:',lcou[i],lcav[i],lcav[ii],lcid[i])



print('')
print('Number of records:', count)
