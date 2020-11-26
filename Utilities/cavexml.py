#! /usr/bin/env python3

# Module for CaveXML
# defines several helpful functions

import re  # Regular Expressions


def merge_elements(stuff):
    # merges repeat XML elements, useful for flattenig database
    if stuff is not None and len(stuff)>0:
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
                
    if lownumber>highnumber:  # fits initialization
        lownumber = ""; highnumber = ""
        
    return lownumber, highnumber



def is_coord_approximate(latlon):
    # Latitude or longitude are approximate if they both have no more than one digit
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
