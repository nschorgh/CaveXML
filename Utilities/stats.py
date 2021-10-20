#! /usr/bin/env python3

# Statistical information about CaveXML database entries

import xml.etree.ElementTree
import urllib.request

# Enter name of XML database here
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')
root = tree.getroot()

# Get database directly from internet
#url = 'https://raw.githubusercontent.com/nschorgh/CaveXML/master/allcaves-database.xml'
#site = urllib.request.urlopen(url)
#data = site.read()
#root = xml.etree.ElementTree.fromstring(data)


def unique(list1):
 
   unique_list = []
   
   for x in list1:
      if x not in unique_list:
         unique_list.append(x)

   return unique_list



def makelist(element_name, longlist):
   cont = item.findall(element_name)
   if cont:
      for i in range(0,len(cont)):
         if cont[i].text:
            longlist.append(cont[i].text)



coulist = []
rotlist = []
cavlist = []
conlist = []
cuslist = []

count = 0

# loop through all records
for item in root.findall('record'):

   count += 1  # count number of records

   makelist('country-name', coulist)
   makelist('rock-type', rotlist)
   makelist('cave-type', cavlist)
   makelist('contents', conlist)
   makelist('cave-use', cuslist)
   

list_of_countries = unique(coulist)
list_of_rocktypes = unique(rotlist)
list_of_cavetypes = unique(cavlist)
list_of_contents = unique(conlist)
list_of_caveuses = unique(cuslist)


def output_stats(ulist, longlist):
   for j in range(0,len(ulist)):
      cc = sum(p == ulist[j] for p in longlist) 
      print(ulist[j], cc)
   print('')

print('country-name:'.upper())
output_stats(list_of_countries, coulist)
print('rock-type:'.upper())
output_stats(list_of_rocktypes, rotlist)
print('cave-type:'.upper())
output_stats(list_of_cavetypes, cavlist)
print('contents:'.upper())
output_stats(list_of_contents, conlist)
print('cave-use:'.upper())
output_stats(list_of_caveuses, cuslist)

print('Number of records searched:', count)

