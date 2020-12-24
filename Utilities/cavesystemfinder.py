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
i=0
for item in root.findall('record'):
    
    # link cave-system entry
    cavsys = syslist[i]
    if len(cavsys)>0:
        idxs = find_all_indices(cavsys, pcnlist)
        if len(idxs)>0:
            print('s Found',len(idxs),'potential name match(es) for system',cavsys)
        else:
            print('s No potential name match found for system',cavsys)
    sys_link = cross_link_cavsys(i, conlist, pcnlist, syslist[i], list_of_lists, uidlist)
    if sys_link:
        print('S',pcnlist[i],'belongs to',syslist[i],'which points back to branch')

    # link branch-name entries
    bralist = list_of_lists[i]
    for k in range(0,len(bralist)):
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

    i = i + 1

