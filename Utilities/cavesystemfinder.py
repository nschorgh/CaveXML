#! /usr/bin/env python3

# finds and cross-links cave systems and branch names

import xml.etree.ElementTree
from cavexml import *

# Enter name of XML database here
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()
        
pcnlist, conlist, uidlist, syslist, list_of_lists = cross_load_data(root)

# main loop, go through all records
#for i in range(0,len(pcnlist)):
i=0  # number of records
cc_distinct=0 # number of distinct caves (don't count branches linked to cave system)
cc_cavsys=0 # number of records with non-empty cave-system entry
cc_cavsys_linked=0 # number of records with non-empty cave-system entry and successfully linked
cc_branch=0 # number of records with non-emtpy branch entries
cc_branches=0
cc_branches_linked=0

for item in root.findall('record'):
    
    # link cave-system entry
    cavsys = syslist[i]
    if len(cavsys)>0:
        cc_cavsys += 1
        idxs = find_all_indices(cavsys, pcnlist)
        if len(idxs)>0:
            print('s Found',len(idxs),'potential name match(es) for system',cavsys)
        else:
            print('s No potential name match found for system',cavsys)
    sys_link = cross_link_cavsys(i, conlist, pcnlist, syslist[i], list_of_lists, uidlist)
    if sys_link:
        print('S',pcnlist[i],'belongs to',syslist[i],'which points back to branch')
        cc_cavsys_linked +=1

    # link branch-name entries
    bralist = list_of_lists[i]
    if len(bralist)>0:
        cc_branch += 1
    for k in range(0,len(bralist)):
        cc_branches += 1
        idxs = find_all_indices(bralist[k], pcnlist)
        if len(idxs)>0:
            print('b Found',len(idxs),'potential name match(es) for branch',bralist[k])
        else:
            print('b No potential name match found for branch',bralist[k])
    bra_link = cross_link_branch(i, conlist, pcnlist, list_of_lists[i], uidlist)
    if len(bra_link)>0:
        for k in range(0,len(bra_link)):
            if bra_link[k] is not None:  # pcn is not absent
                print('B',pcnlist[i],'has branch',list_of_lists[i][k],'which points back to cavesys')
                cc_distinct -=1
                cc_branches_linked +=1

    i += 1
    cc_distinct += 1


print()
print('Number of records:',i)
print('Number of records that are part of cave system:',cc_cavsys)
print('Number of branches linked to a cave system:',cc_cavsys_linked)
print('Number of records that list branches:',cc_branch)
print('Number of branches listed:',cc_branches)
print('Number of branches linked to a cave system:',cc_branches_linked)
print('Number of distinct caves:',cc_distinct)

# This needs some more work

