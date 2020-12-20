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
    sys_link = cross_link_cavsys(i, conlist, pcnlist, syslist[i], list_of_lists, uidlist)
    if sys_link:
        print(pcnlist[i],'belongs to',syslist[i],'which points back to branch')
    
    # link branch-name entries
    bra_link = cross_link_branch(i, conlist, pcnlist, list_of_lists[i], uidlist)
    if len(bra_link)>0:
        for k in range(0,len(bra_link)):
            print(pcnlist[i],'has branch',list_of_lists[i][k],'which points back to cavesys')

    i = i + 1

