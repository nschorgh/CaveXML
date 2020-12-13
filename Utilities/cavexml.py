#! /usr/bin/env python3

# Module for CaveXML
# defines several helpful functions

import re  # Regular Expressions


def merge_elements(stuff):
    # merges repeat XML elements, useful for flattenig database
    #if stuff is not None and len(stuff)>0:
    if stuff:
        str = stuff[0].text
        for i in range(1,len(stuff)):  # merge multiple entries
            if stuff[i].text is not None:
                str = str + "; " + stuff[i].text
    else:
        str = ""
    return str



def parse_ExtendedUnsignedInteger(eui):
    if eui is None:
        return

    # test whether input is ExtendedUnsignedInteger
    matched = re.fullmatch("[~>]?[0-9]+[+]?", eui.strip())
    if matched is None:
        print('Error:',eui,'is not an ExtendedUnsignedInteger')
        return

    # extract number
    number = [int(s) for s in re.findall(r'\b\d+\b',eui)]
    number = number[0]

    # set defaults
    qualifier = ''
    approx = False

    # determine meaning of characters, if present
    if len(eui)>0:
        first_char = eui[0]
        if first_char=="~":
            approx = True
        if first_char==">":
            qualifier = '>'

        last_char = eui[len(eui)-1]
        if last_char == '+':
            qualifier = '+'
            
    #print(eui,qualifier,number,approx)
    return number



def parse_AltitudeEntry(alt):

    lownumber = +99999; highnumber = -99999

    for i in range(0,len(alt)):
        str = alt[i].text
        if str is not None:
            if "-" in str or "–" in str: # altitude range
                if "-" in str:
                    hyphen = '-'
                if "–" in str:
                    hyphen = '–'
                minalt = int(str.split(hyphen)[0])
                maxalt = int(str.split(hyphen)[1])
                if minalt<lownumber:
                    lownumber = minalt
                if maxalt>highnumber:
                    highnumber = maxalt
            else:  # ExtendedUnsignedInteger optionally followed by comment
                str = str.strip()
                if len(str.split(' '))>1:  
                    str = str.split(' ')[0]  # strip comment to make it an EUI
                number = parse_ExtendedUnsignedInteger(str)
                if number<lownumber:
                    lownumber = number
                if number>highnumber:
                    highnumber = number
                
    if lownumber>highnumber and lownumber!=+99999:
        swap = highnumber
        highnumber = lownumber
        lownumber = swap
        
    return lownumber, highnumber



def parse_cave_id(caveid):

    org = ''
    id = ''
    
    if caveid is None:
        return
    
    str = caveid.text
    if str is not None:
        try:
            org = str.split('-')[0]  # 3-letter organization code
            re.compile("[A-Z]{3}", org)  # fails if it doesn't match
            id  = str.split('-')[1]
        except:  # no organization given
            org = ''
            id  = str.split('-')[0]

    return org, id



def is_this_an_ice_cave(record):
    # returns True if contents field includes 'permanent ice'
    cont = record.findall('contents')
    if cont:
        for i in range(0,len(cont)):
            if cont[i].text:
                if 'permanent ice' in cont[i].text:
                    return True

    return False



def is_this_a_lava_tube(record):
    # returns True if cave-type field includes 'lava tunnel'
    cavetype = record.findall('cave-type')
    if cavetype:
        for i in range(0,len(cavetype)):
            if cavetype[i].text:
                if 'lava tunnel' in cavetype[i].text:
                    return True

    return False



def is_coord_approximate(latlon):
    # Latitude or longitude are approximate if they have no more than one digit
    # after the decimal point. Returns Boolean.
    approx = False
    if latlon is not None: # Tag present (but could be empty)
        if latlon.text is not None:
            try:
                latlon_float = float(latlon.text)
                if int(10*latlon_float)==10*latlon_float:
                    approx = True
            except:
                pass

    return approx



def get_one_cave_name(item):
    # Get a cave name for a record by searching, in the following order
    # 1. principal-cave-name
    # 2. cave-id(s)
    # 3. other-cave-name(s)

    pcn = item.findall('principal-cave-name')
    if len(pcn)>0: # tag present
        pcn = pcn[0].text
        if pcn is not None: # not empty
            str = pcn.strip() # strips leading and trailing whitespace
            if len(str)>0:
                return str

    cid = item.findall('cave-id')
    for i in range(0,len(cid)):
        str = cid[i].text
        if str is not None: 
            str = str.strip()
            if len(str)>0:
                return str
                
    ocn = item.findall('other-cave-name')
    for i in range(0,len(ocn)):
        str = ocn[i].text
        if str is not None:
            str = str.strip()
            if len(str)>0:
                return str

    return ''  # if no name found, return empty string



def extract_hyperlink_from_string(refstr):
    k = refstr.find("https://")
    if k<0:
        k = refstr.find("http://")
    if k>=0: 
        t = refstr[k:] 
        kend = t.find(" ") 
        if kend>0:
            t = t[:kend]
            t = '"' + t + '"'

    if k>=0:
        return t
    else:
        return ''
