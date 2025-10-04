CaveXML 0.2 Draft
==============

Proposed revised CaveXML standard, called 0.2, whereas the original version will be referred to as version 0.1.  

<p>

| CaveXML 0.1           | CaveXML 0.2   |  Notes |  
|:----------------------|:-------------|:------------|
|<record\>   | <cave\> |  renamed | 
|<country-name\> | <country-name\> | |
|<state-or-province\> | <state-or-province\> | | 
|<phys-area-name\> |  <phys-area-name\> |  | 
|<principal-cave-name\>| <principal-cave-name\> | |  
|<other-cave-name\> | <other-cave-name\> |  | 
|<cave-id\>  | <cave-id\> |  | 
|	     | <entrance\> | new | 
|	     | &nbsp;&nbsp;&nbsp;&nbsp;<entrance-id\> | new | 
|<latitude\> | &nbsp;&nbsp;&nbsp;&nbsp;<latitude\> | | 
|<longitude\> | &nbsp;&nbsp;&nbsp;&nbsp;<longitude\> |  | 
|<altitude\> | &nbsp;&nbsp;&nbsp;&nbsp;<altitude\> | no more ranges | 
|	     | &nbsp;&nbsp;&nbsp;&nbsp;<entrance-type\>  | new |
|<length\>   | <length\> |  | 
|<vertical-extent\> | <vertical-extent\> |  | 
|<number-of-entrances\>| <number-of-entrances\> |  | 
|<map-link\> | <map-link\> |  |
|<rock-type\> | <rock-type\> |  | 
|<cave-type\> | <cave-type\> |  | 
|<contents\> | <contents\> |  | 
|<comments\> | <comments\> |  |
|<cave-system\> |    | deleted |
|<branch-name\> | <cave\>  | restructured | 
|<reference\> | <reference\> |  | 
|<cave-use\> | <cave-use\> |  | 
|<curation\> | <curation\> |  |

&nbsp;

New in version 0.2:
---

The `<entrance>` element is introduced, where entrance-specific information goes, such as longitude, latitude, and altitude. That allows simplification of the altitude element, which is now specific to each entrance rather than applied to the whole cave. New elements `<entrance-id>` and `<entrance-type>` are also introduced. The downside is that every single-entrance cave, which is most caves, requires the extra `<entrance>` opening and closing tags.

Instead of `<branch-name>` whole `<cave>` records can be entered and that recursively. In other words, a cave system is now a cave record with additional cave records within it. That does away with the problem of finding information about branches elsewhere in the database. If two caves share an entrance, they must have matching `<entrance-id>` entries. The element `<cave-system>` is now redundant; the name of the cave system is the `<principal-cave-name>` one level above.

`<record>` has changed to `<cave>`.

Finally, elements can now be placed in any order.

CaveXML 0.2 is not backwards compatible with 0.1. For example, there can be no longitude or latitude entries outside of the `<entrance>` element.   


CaveXML 0.2 Definitions
---


A CaveXML database has the following structure:

        <CaveDataBase> 
          <cave>
            ...
          </cave>
          <cave>
            ...
          </cave>
            .
            .
            .
        </CaveDataBase>

Elements within a cave record are defined as follows:  
<span style="color: red"> (Red indicates changes to the previous CaveXML version) </span>  

**<country-name\>**  *controlled vocabulary*  
Country name where the cave entrance is located. This should be the name of the country spelled according to the GeoNames ontology, which for most instances is identical to the country name according to the ISO 3166 standard. (The precise list is found in the CaveXML Schema Definition `cavexml.xsd`). Similar to UISIC field [SY285](http://www.uisic.uis-speleo.org/exchange/atendefn.html#285)  
For extraterrestrial caves, this element specifies the planetary body where the cave is located. Allowed terms are "Moon", which refers to Earth's moon, "Mars", and a few more. An empty or missing entry implies the cave is located on planet Earth.  

**<state-or-province\>**  *string*  
State or province where the cave entrance is located. This can also be a county or district. [state-or-province] is intended for politically or organizationally defined areas below country level. For geologically or physically defined units, use [phys-area-name] instead.  
Generalization of UISIC field [SY287](http://www.uisic.uis-speleo.org/exchange/atendefn.html#287)

**<phys-area-name\>**  *string*  
Name of mountain, volcano, mountain range, island, massif, geologic unit, or another physically-defined unit. Example: Pyrenees. For politically-defined regions use [state-or-province] instead. Parks also belong in the field [phys-area-name].

**<principal-cave-name\>**  *string, maxOccurs=1*    
The current formal agreed name for a cave or karst feature, expressed in the local language. The character set is UTF-8, so characters from many languages can be used.    
UISIC field [CA70](http://www.uisic.uis-speleo.org/exchange/atendefn.html#70).
Similar to KarstLink property 'label'.

**<other-cave-name\>**  *string*  
Further names which a cave or karst feature has or has had beyond its current name as given in [principal-cave-name].    
Similar to UISIC field [CA69](http://www.uisic.uis-speleo.org/exchange/atendefn.html#69) and KarstLink property 'alternate name'.

**<cave-id\>**  *ASCII string*  
National cave identification number: Unique cave identifier, such as an optional 3-letter organization code + cave registry number, e.g. HSS-234/7, where HSS stands for Hawaii Speleological Survey. For small countries, this might just be the national cave identification number or cadastral number, e.g. 1234/5. The [cave-id] is restricted to a subset ASCII characters that includes numbers, capital letters, and the symbols ()*+,-./:;<=>?@. It does not include small letters or any other symbols.  
Similar to UISIC field [CA227](http://www.uisic.uis-speleo.org/exchange/atendefn.html#227) and to the "international cave number". A record is allowed to have more than one [cave-id]. No two caves within the same country should have the same [cave-id], but this is not required by the CaveXML standard.  

<span style="color: red"> **<entrance\>** *complexType*  </span>

&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">**<entrance-id\>**  *ASCII string*   
&nbsp;&nbsp;&nbsp;&nbsp; Entrance identification number, if available. This could be a cadastral number, e.g. 1234/5. The [entrance-id] has the same format requirements as the [cave-id]. It is restricted to a subset of ASCII characters that includes numbers, capital letters, and the symbols ()*+,-./:;<=>?@. It does not include small letters or any other symbols.  </span>

&nbsp;&nbsp;&nbsp;&nbsp; **<latitude\>**  *-90 ≤ decimal ≤ +90, maxOccurs=1*  
&nbsp;&nbsp;&nbsp;&nbsp; The N-S latitude of the cave entrance or karst feature, expressed as +/- degrees and decimal degrees. Positive if north of the equator, negative if south of the equator. Expressed as a decimal number, rather than as degrees, minutes, and seconds. If [latitude] is given, [longitude] must also be provided. Trailing zeros are significant and imply a coordinate is exact rather than rounded.   
&nbsp;&nbsp;&nbsp;&nbsp; UISIC fields [CA245](http://www.uisic.uis-speleo.org/exchange/atendefn.html#245) (exact) or [CA21](http://www.uisic.uis-speleo.org/exchange/atendefn.html#21) (coarse).
KarstLink property 'latitude'.

&nbsp;&nbsp;&nbsp;&nbsp; **<longitude\>**  *-180 ≤ decimal ≤ +180, maxOccurs=1*  
The E-W longitude of the cave entrance or karst feature, expressed as +/- degrees and decimal degrees. Positive if east of Greenwich, or negative if west of Greenwich. Expressed as a decimal number, rather than as degrees, minutes, and seconds. If [longitude] is given, [latitude] must also be provided. Trailing zeros are significant and imply a coordinate is exact rather than rounded. For extraterrestrial caves, the longitude must also be within -180&deg; and +180&deg;, even if it is conventional to use the range 0&deg; to 360&deg; instead.    
UISIC fields [CA246](http://www.uisic.uis-speleo.org/exchange/atendefn.html#246) (exact) or [CA22](http://www.uisic.uis-speleo.org/exchange/atendefn.html#22) (coarse).
KarstLink property 'longitude'.

&nbsp;&nbsp;&nbsp;&nbsp; **<altitude\>**  *(special string)*  <span style="color: red">*maxOccurs=1*</span>  
&nbsp;&nbsp;&nbsp;&nbsp; Altitude of cave entrance in meters above sea level (or above zero datum), followed by an optional comment. The altitude must be rounded to the nearest integer. Examples: \~2500 main entrance or 2227 lower entrance. And altitude can be preceded by > or ~. The number can also be followed by a "+" symbol to indicate "or higher". Negative altitudes can also be entered and are appropriate for underwater and extraterrestrial caves. They can optionally be preceded with '\~'.  
Similar to UISIC fields [CA442](http://www.uisic.uis-speleo.org/exchange/atendefn.html#442) (altitude) and [CA670](http://www.uisic.uis-speleo.org/exchange/atendefn.html#670) (altitude-comment) combined. Similar to KarstLink property 'altitude'.  
<span style="color: red">Note: altitude ranges are no longer allowed</span>

&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red"> **<entrance-type\>**  </span> *controlled vocabulary*  
&nbsp;&nbsp;&nbsp;&nbsp; TBD  

**<length\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The aggregate length of the cave passages in meters, usually obtained by summing the lengths of all surveyed distances. Length differs from horizontal extent. The length must be rounded to the nearest integer. The unit must be meters, not kilometers or feet. Symbols ~ and > are allowed in front of the number. Symbol + is allowed after the number.   
UISIC field [CA56](http://www.uisic.uis-speleo.org/exchange/atendefn.html#56).
Similar to KarstLink property 'length'.

**<vertical-extent\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The overall vertical distance in meters between the highest and lowest known point of the cave or karst feature, expressed as an unsigned value. (Sometimes vertical extent is defined as the vertical distance between the highest and lowest survey station.) The vertical extent must be rounded to the nearest whole meter. Symbols ~ and > are allowed in front of the number. Symbol + is allowed after the number.   
UISIC field [CA511](http://www.uisic.uis-speleo.org/exchange/atendefn.html#511)
Similar to KarstLink property 'vertical extent'.

**<number-of-entrances\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The total number of entrances to the cave, whether they are numbered or not. This is usually a positive integer, but expressions such as \>5, 10+, and ~100 are allowed, where "10+" means "ten or more", whereas ">5" means "more than five".    
UISIC field [CA9](http://www.uisic.uis-speleo.org/exchange/atendefn.html#9)

**<map-link\>**  *anyURI*  
A Uniform Resource Identifier (URI) that points to a map of the cave, in form of an image or in form of geospatial data. A common type of entry for [map-link] is a Uniform Resource Locator (URL) that points to a cave map on the internet, e.g., http://www.mexicancaves.org/maps/1944.pdf. The only syntactic restriction is the exclusion of certain special characters that are not allowed in URIs. Items that belong in this field are single-page maps and digital (geospatial) survey data. Items that do *not* belong in this field are URIs to multi-page documents, articles that contain maps (these belong to [reference]), and maps of cave entrance locations.

**<rock-type\>**  *controlled vocabulary*  
Type(s) of rock in which the cave or karst feature is formed from, selected from a pre-defined list of options.
Similar to UISIC field [CA7](http://www.uisic.uis-speleo.org/exchange/atendefn.html#7), which has [similar options](http://www.uisic.uis-speleo.org/exchange/atencode.html#7).   
List of options: *limestone, dune limestone, dolomite, marble, basalt, dolerite, granite, gypsum, ice, lava, magnesite, mudstone, quartzite, sandstone, soil, tuff*. More than one [rock-type] can be entered, e.g., for a cave in ice with a basalt floor.

**<cave-type\>**  *controlled vocabulary*  
The cave type(s) based on the formation process and selected from a pre-defined list of terms.  
List of options: *solution cave, artificial cave, boulder cave, glacier cave, lava tunnel, lava vent, tectonic cave, eolian cave, piping cave, sea cave, weathering cave, misc. type*.  "Boulder caves" are also known as "talus caves" or "rockslide caves". The term "lava tunnel" is equivalent to "lava tube", and "lava tube" and "lava vent" are subcategories of volcanic caves. Eolian (wind), piping (suffosion), sea (littoral), and frost weathering (frost wedging) caves are types of erosional caves. Cave formation processes that belong to "misc. type" include deposition caves and biology-made caves. UISIC field [CA8](http://www.uisic.uis-speleo.org/exchange/atendefn.html#8) lists [similar options](http://www.uisic.uis-speleo.org/exchange/atencode.html#8).

**<contents\>**  *controlled vocabulary*  
What the cave contains. Similar to UISIC field [CA72](http://www.uisic.uis-speleo.org/exchange/atendefn.html#72).  
List of options: *permanent ice, periodic ice, extensive guano, many bats, occasional bats, birds, fish, snakes, trogloxenes, accidental trogloxenes, troglophiles, troglobites, charcoal, paintings, minerals, lake(s), waterfall(s), tree roots, perennially submerged, intermittently submerged, perennially part-submerged, intermittently part-submerged*. CA72 has [36 allowed options](http://www.uisic.uis-speleo.org/exchange/atencode.html#72), which have been shortened to 18, and the four terms about submersion are borrowed from [CA2](http://www.uisic.uis-speleo.org/exchange/atendefn.html#2). If the desired entry is not available among the list of terms, enter it in [comments] instead.

**<comments\>**  *string*  
Comments about a cave or karst feature. This field should be used only when a suitable more specific field is not available. Use semicolons (;) between separate comments, or place them in separate [comments] entries.  
UISIC field [CA53](http://www.uisic.uis-speleo.org/exchange/atendefn.html#53) and KarstLink property 'comment'.

<span style="color: red"> **<cave\>**  *complexType, recursive*   
On occasion, it is discovered that two named caves are connected with one another, and hence form a single cave.
For such a system of caves, the cave record can contain another cave record within it.
This element is defined recursively, so all elements can be reused and multiple levels are allowed. A cave system can contain another cave system, each made up of several caves.
Another type of cave system is a lava tube with collapsed portions that divide the conduit into segments. When two cave branches share the same entrance, their [entrance-id] must match. If no official entrance ids are available, dummy entries must be created to declare this topology. Any entrance element without an entrance id is automatically assumed to be physically different from any entrance listed in a parallel [cave] record belonging to the same cave system.
</span>  
<span style="color: red">Note: The elements [cave-system] and [cave-branch] are no longer allowed. They have been replaced with [cave].</span>  

**<reference\>**  *string*  
Bibliographical reference, often abbreviated as "Author et al. (year) doi", e.g., "Waters et al. (1990) https://doi.org/10.3133/b1673". Multiple references must be placed in separate [reference] entries. All references that served as source of the data in the record ought to be included here. Any URL can accompany a reference, but permlinks, such as those starting with https://doi.org/ or https://hdl.handle.net/ are preferable. This field can also contain references to data, e.g., https://www.mindat.org/loc-195731.html.

**<cave-use\>**  *controlled vocabulary*  
The present use (if any) being made of the cave. Similar to UISIC field [CA41](http://www.uisic.uis-speleo.org/exchange/atendefn.html#41).  
CA41 allows [32 predefined terms](http://www.uisic.uis-speleo.org/exchange/atencode.html#41). This list has been shortened to nine terms: *guided tourist cave, self-guided tourist cave, waste disposal, habitation, livestock shelter, water source, mine, shrine, temple*.

**<curation\>**  *string*  
Comments about the curation of database entries. This is a free-form entry, but data curators can choose to use their own standardized terminology or codes.   

<p>

Table 1: Data types for each CaveXML element. Default attributes are *minOccurs=0* and *maxOccurs=unbounded*. The third column shows restrictions on the element or on its value. The last column contains examples of valid entries.  

| Element               | XML data type | Restrictions | Example |  
|:----------------------|:-------------:|:------------:|:--------|  
|\<country-name\> | token with restriction | pre-defined list of strings | Austria |  
|\<state-or-province\> | string | - | California |  
|\<phys-area-name\> | string | - | Pyrenees |
|\<principal-cave-name\>| string | maxOccurs=1 | Kolowrathöhle |  
|\<other-cave-name\> | string | - | M-340 |
|\<cave-id\> | token with restriction | RegEx pattern, ASCII | HSS-1547/9 |
|\<entrance\> | complexType | - | -  |
|\<entrance-id\> | token with restriction | RegEx pattern, ASCII | 1511/24 |
|\<latitude\> | decimal with restriction | range -90...+90, maxOccurs=1 | 47.72792 |
|\<longitude\> | decimal with restriction | range -180...+180, maxOccurs=1 | 13.00858 |
|\<altitude\> | token with restriction | RegEx pattern, maxOccurs=1 | \~1500 main entrance |
|\<entrance-type\> | token with restriction | pre-defined list of strings |   |
|\<length\> | ExtendedUnsignedInteger | maxOccurs=1 | \>5000 |
|\<vertical-extent\> | ExtendedUnsignedInteger | maxOccurs=1 | 240 |
|\<number-of-entrances\>| ExtendedUnsignedInteger | maxOccurs=1 | 7+ |
|\<map-link\> | anyURI | - | http://www.mexicancaves.org/maps/1944.pdf |
|\<rock-type\> | token with restriction | pre-defined list of strings | limestone |
|\<cave-type\> | token with restriction | pre-defined list of strings | glacier cave |
|\<contents\> | token with restriction | pre-defined list of strings | waterfall(s) |
|\<comments\> | string | - | Mauna Loa flow of 1855 |
|\<cave\> | complexType  | - | - | 
|\<reference\> | string | - | Yonge et al. (2018) doi:10.1016/B978-0-12-811739-2.00015-2 |
|\<cave-use\> | token with restriction | pre-defined list of strings | guided tourist cave |
|\<curation\> | string | - | updated length based on Smith et al. (2020) |





