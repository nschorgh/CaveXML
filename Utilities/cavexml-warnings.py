#! /usr/bin/env python3

print('This script issues warnings about CaveXML database entries.')
print()

import xml.etree.ElementTree
from cavexml import get_one_cave_name, parse_ExtendedUnsignedInteger

# Enter name of XML database here
#tree = xml.etree.ElementTree.parse('../../test.xml')
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()

# elements with maxOccurs>1
multipleelements = ['country-name','state-or-province','phys-area-name',
                    'other-cave-name','cave-id','altitude','map-link',
                    'rock-type','cave-type','contents','branch-name',
                    'reference','cave-use','curation']  

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

    leng = item.find('length')
    if leng is not None:
        lennumb, approx, qual = parse_ExtendedUnsignedInteger(leng.text)
    else:
        lennumber = None
        
    vex = item.find('vertical-extent') 
    if vex is not None:
        vexnumb, approx, qual = parse_ExtendedUnsignedInteger(vex.text)
    else:
        vexnumb = None
        
    if lennumb is not None and vexnumb is not None:
        if lennumb<vexnumb:
            print('WARNING: Length is smaller than vertical extent',leng.text,vex.text)

    for k in range(0,len(multipleelements)):
        tagname = multipleelements[k]
        rot = item.findall(tagname)
        for i in range(0,len(rot)):
            for j in range(0,i):
                if rot[i].text == rot[j].text:
                    print('WARNING: duplicate entry for',tagname,'in',acavename)
            empty = 0
            if rot[i].text is None:
                empty += 1
            if empty>0 and len(rot)>1: # empty tag in addition to another tag value
                print('WARNING: empty where empty need not be',acavename,tagname)

    ref = item.find('reference')
    try:
        ref = ref.text.strip()
        if ref is None:
            print('WARNING: no reference for',acavename)
    except:
        print('WARNING: no reference for',acavename)
        
    ref = item.findall('reference')
    for i in range(0,len(ref)):
        refstr = ref[i].text
        if refstr is None:
            continue
        if ('//doi:' in refstr) or ('doi.org:' in refstr): # should be doi: or https://doi.org/
            print('Malformatted doi', refstr)
        if 'doi' in refstr.lower():
            if 'DOI' not in refstr and 'doi' not in refstr:  # excludes combinations such as DOi, doI
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
