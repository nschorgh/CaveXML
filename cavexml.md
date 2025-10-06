CaveXML Definitions
===================

> "The systematic documentation, mapping and publication of data about caves (excepting entrance locations) is a responsibility of all users of the cave environment, and should be encouraged by management authorities."  
> *Guidelines for Cave and Karst Protection*, Working Group on Cave and Karst Protection (1997)

CaveXML facilitates exchange of data about caves through the definition and implementation of a data interchange format. The CaveXML standard defines a set of XML elements and their meaning, as described below. Its syntax is implemented in an XML Schema Definition (`cavexml.xsd`). As a pilot project, basic data for a few thousand caves has been organized in CaveXML format.  

The Informatics Commission of the International Union of Speleology (UISIC) has drafted guidelines for a data exchange standard with over 700 fields. CaveXML builds on these recommendations for the much smaller number of elements it uses.  

A CaveXML database has the following structure, where each record corresponds to a cave or cave system:

        <CaveDataBase> 
          <record>
            ...
          </record>
          <record>
            ...
          </record>
            .
            .
            .
        </CaveDataBase>

Elements within a record are defined as follows:

**\<country-name\>**  *controlled vocabulary*  
Country name where the cave entrance is located. This should be the name of the country spelled according to the GeoNames ontology, which for most instances is identical to the country name according to the ISO 3166 standard. (The precise list is found in the CaveXML Schema Definition `cavexml.xsd`). Similar to UISIC field [SY285](http://www.uisic.uis-speleo.org/exchange/atendefn.html#285)  
For extraterrestrial caves, this element specifies the planetary body where the cave is located. Allowed terms are "Moon", which refers to Earth's moon, "Mars", and a few more. An empty or missing entry implies the cave is located on planet Earth.  

**\<state-or-province\>**  *string*  
State or province where the cave entrance is located. This can also be a county or district. [state-or-province] is intended for politically or organizationally defined areas below country level. For geologically or physically defined units, use [phys-area-name] instead.  
Generalization of UISIC field [SY287](http://www.uisic.uis-speleo.org/exchange/atendefn.html#287)

**\<phys-area-name\>**  *string*  
Name of mountain, volcano, mountain range, island, massif, geologic unit, or another physically-defined unit. Example: Pyrenees. For politically-defined regions use [state-or-province] instead. Parks also belong in the field [phys-area-name].

**\<principal-cave-name\>**  *string, maxOccurs=1*    
The current formal agreed name for a cave or karst feature, expressed in the local language. The character set is UTF-8, so characters from many languages can be used.    
UISIC field [CA70](http://www.uisic.uis-speleo.org/exchange/atendefn.html#70).
Similar to KarstLink property 'label'.

**\<other-cave-name\>**  *string*  
Further names which a cave or karst feature has or has had beyond its current name as given in [principal-cave-name].    
Similar to UISIC field [CA69](http://www.uisic.uis-speleo.org/exchange/atendefn.html#69) and KarstLink property 'alternate name'.

**\<cave-id\>**  *ASCII string*  
National cave identification number: Unique cave identifier, such as an optional 3-letter organization code + cave registry number, e.g. HSS-234/7, where HSS stands for Hawaii Speleological Survey. For small countries, this might just be the national cave identification number or cadastral number, e.g. 1234/5. The [cave-id] is restricted to a subset ASCII characters that includes numbers, capital letters, and the symbols +,-. and /. It does not include small letters or any other symbols.  
Similar to UISIC field [CA227](http://www.uisic.uis-speleo.org/exchange/atendefn.html#227) and to the "international cave number". A record is allowed to have more than one [cave-id]. No two caves within the same country should have the same [cave-id], but this is not required by the CaveXML standard.  

**\<latitude\>**  *-90 ≤ decimal ≤ +90, maxOccurs=1*  
The N-S latitude of the cave entrance or karst feature, expressed as +/- degrees and decimal degrees. Positive if north of the equator, negative if south of the equator. Expressed as a decimal number, rather than as degrees, minutes, and seconds. If [latitude] is given, [longitude] must also be provided. Trailing zeros are significant and imply a coordinate is exact rather than rounded.   
UISIC fields [CA245](http://www.uisic.uis-speleo.org/exchange/atendefn.html#245) (exact) or [CA21](http://www.uisic.uis-speleo.org/exchange/atendefn.html#21) (coarse).
KarstLink property 'latitude'.

**\<longitude\>**  *-180 ≤ decimal ≤ +180, maxOccurs=1*  
The E-W longitude of the cave entrance or karst feature, expressed as +/- degrees and decimal degrees. Positive if east of Greenwich, or negative if west of Greenwich. Expressed as a decimal number, rather than as degrees, minutes, and seconds. If [longitude] is given, [latitude] must also be provided. Trailing zeros are significant and imply a coordinate is exact rather than rounded. For extraterrestrial caves, the longitude must also be within -180&deg; and +180&deg;, even if it is conventional to use the range 0&deg; to 360&deg; instead.    
UISIC fields [CA246](http://www.uisic.uis-speleo.org/exchange/atendefn.html#246) (exact) or [CA22](http://www.uisic.uis-speleo.org/exchange/atendefn.html#22) (coarse).
KarstLink property 'longitude'.

**\<altitude\>**  *(special string)*  
Altitude or range of altitudes of cave entrance(s) in meters above sea level (or above zero datum), followed by an optional comment that can be used to clarify the nature of the entry. The altitude must be rounded to the nearest integer. Multiple [altitude] entries can be entered. Examples: \~2500 main entrance, 2227 lower entrance, 2227-2500. And altitude can be preceded by > or ~. The number can also be followed by a "+" symbol to indicate "or higher". If a range of altitudes is provided, it represents the altitudes of the lowest and highest known entrances of a cave, and not an uncertainty in altitude. The latter should be indicated with a "\~" sign in front of the number. Negative altitudes can also be entered and are appropriate for underwater and extraterrestrial caves. They can optionally be preceded with '\~'. Ranges of negative altitudes have to be represented by two individual altitude entries.    
Similar to UISIC fields [CA442](http://www.uisic.uis-speleo.org/exchange/atendefn.html#442) (altitude) and [CA670](http://www.uisic.uis-speleo.org/exchange/atendefn.html#670) (altitude-comment) combined. Similar to KarstLink property 'altitude'.

**\<length\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The aggregate length of the cave passages in meters, usually obtained by summing the lengths of all surveyed distances. Length differs from horizontal extent. The length must be rounded to the nearest integer. The unit must be meters, not kilometers or feet. Symbols ~ and > are allowed in front of the number. Symbol + is allowed after the number.   
UISIC field [CA56](http://www.uisic.uis-speleo.org/exchange/atendefn.html#56).
Similar to KarstLink property 'length'.

**\<vertical-extent\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The overall vertical distance in meters between the highest and lowest known point of the cave or karst feature, expressed as an unsigned value. (Sometimes vertical extent is defined as the vertical distance between the highest and lowest survey station.) The vertical extent must be rounded to the nearest whole meter. Symbols ~ and > are allowed in front of the number. Symbol + is allowed after the number.   
UISIC field [CA511](http://www.uisic.uis-speleo.org/exchange/atendefn.html#511)
Similar to KarstLink property 'vertical extent'.

**\<number-of-entrances\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The total number of entrances to the cave, whether they are numbered or not. This is usually a positive integer, but expressions such as \>5, 10+, and ~100 are allowed, where "10+" means "ten or more", whereas ">5" means "more than five".    
UISIC field [CA9](http://www.uisic.uis-speleo.org/exchange/atendefn.html#9)

**\<map-link\>**  *anyURI*  
A Uniform Resource Identifier (URI) that points to a map of the cave, in form of an image or in form of geospatial data. A common type of entry for [map-link] is a Uniform Resource Locator (URL) that points to a cave map on the internet, e.g., http://www.mexicancaves.org/maps/1944.pdf. The only syntactic restriction is the exclusion of certain special characters that are not allowed in URIs. Items that belong in this field are single-page maps and digital (geospatial) survey data. Items that do *not* belong in this field are URIs to multi-page documents, articles that contain maps (these belong to [reference]), and maps of cave entrance locations.

**\<rock-type\>**  *controlled vocabulary*  
Type(s) of rock in which the cave or karst feature is formed from, selected from a pre-defined list of options.
Similar to UISIC field [CA7](http://www.uisic.uis-speleo.org/exchange/atendefn.html#7), which has [similar options](http://www.uisic.uis-speleo.org/exchange/atencode.html#7).   
List of options: *limestone, dune limestone, dolomite, marble, basalt, dolerite, granite, gypsum, ice, lava, magnesite, mudstone, quartzite, sandstone, soil, tuff*. More than one [rock-type] can be entered, e.g., for a cave in ice with a basalt floor.

**\<cave-type\>**  *controlled vocabulary*  
The cave type(s) based on the formation process and selected from a pre-defined list of terms.  
List of options: *solution cave, artificial cave, boulder cave, glacier cave, lava tunnel, lava vent, tectonic cave, eolian cave, piping cave, sea cave, weathering cave, misc. type*.  "Boulder caves" are also known as "talus caves" or "rockslide caves". The term "lava tunnel" is equivalent to "lava tube", and "lava tube" and "lava vent" are subcategories of volcanic caves. Eolian (wind), piping (suffosion), sea (littoral), and frost weathering (frost wedging) caves are types of erosional caves. Cave formation processes that belong to "misc. type" include deposition caves and biology-made caves. UISIC field [CA8](http://www.uisic.uis-speleo.org/exchange/atendefn.html#8) lists [similar options](http://www.uisic.uis-speleo.org/exchange/atencode.html#8).

**\<contents\>**  *controlled vocabulary*  
What the cave contains. Similar to UISIC field [CA72](http://www.uisic.uis-speleo.org/exchange/atendefn.html#72).  
List of options: *permanent ice, periodic ice, extensive guano, many bats, occasional bats, birds, fish, snakes, trogloxenes, accidental trogloxenes, troglophiles, troglobites, charcoal, paintings, minerals, lake(s), waterfall(s), tree roots, perennially submerged, intermittently submerged, perennially part-submerged, intermittently part-submerged*. CA72 has [36 allowed options](http://www.uisic.uis-speleo.org/exchange/atencode.html#72), which have been shortened to 18, and the four terms about submersion are borrowed from [CA2](http://www.uisic.uis-speleo.org/exchange/atendefn.html#2). If the desired entry is not available among the list of terms, enter it in [comments] instead.

**\<comments\>**  *string*  
Comments about a cave or karst feature. This field should be used only when a suitable more specific field is not available. Use semicolons (;) between separate comments, or place them in separate [comments] entries.  
UISIC field [CA53](http://www.uisic.uis-speleo.org/exchange/atendefn.html#53) and KarstLink property 'comment'.

**\<cave-system\>**  *string, maxOccurs=1*  
On occasion, it is discovered that two named caves are connected with one another, and hence form a single cave. The caves keep their individual names and the whole is referred to as a cave system. Another type of cave system is a lava tube with collapsed portions that divide the conduit into segments. A record in the database can be a cave (with one or more branches or segments) or a cave system (of two or more named caves). Entries can link to the system they are part of using the field [cave-system], which should match the [primary-cave-name] of the cave system. Caves can have a [cave-system] element even if a dedicated record for the cave system does not exist in the database. Vice versa, the entry [branch-name] links the cave system to branches or segments that have their own record (and their own entrances). (A group of caves that are not connected and never were connected do not form a cave system and must be represented by individual entries. If they are in close vicinity of one another, it can be indicated in the [phys-area-name] or [comments] fields.)

**\<branch-name\>**  *string*    
A [branch-name] is the [principal-cave-name] of named cave branches or cave segments with their own entrances. This field allows a record to be a cave system consisting of named caves that already have their own record in the database. Multiple [branch-name]s should be listed, even if the target records do not exist in the database. The presence of one or more [branch-name] entries identifies a record as a cave system.

**\<reference\>**  *string*  
Bibliographical reference, often abbreviated as "Author et al. (year) doi", e.g., "Waters et al. (1990) https://doi.org/10.3133/b1673". Multiple references must be placed in separate [reference] entries. All references that served as source of the data in the record ought to be included here. Any URL can accompany a reference, but permlinks, such as those starting with https://doi.org/ or https://hdl.handle.net/ are preferable. This field can also contain references to data, e.g., https://www.mindat.org/loc-195731.html.

**\<cave-use\>**  *controlled vocabulary*  
The present use (if any) being made of the cave. Similar to UISIC field [CA41](http://www.uisic.uis-speleo.org/exchange/atendefn.html#41).  
CA41 allows [32 predefined terms](http://www.uisic.uis-speleo.org/exchange/atencode.html#41). This list has been shortened to nine terms: *guided tourist cave, self-guided tourist cave, waste disposal, habitation, livestock shelter, water source, mine, shrine, temple*.

**\<curation\>**  *string*  
Comments about the curation of database entries. This is a free-form entry, but data curators can choose to use their own standardized terminology or codes.  


Syntax rules (in support of parsing and querying)
-------------------------------------------------

-   All fields are optional *(minOccurs=0)*.

-   Elements with *maxOccurs=1* can appear at most once within a record, whereas the default is *maxOccurs=unbounded*. (The UISIC refers to this as multi-valued, as opposed to single-valued.)

-   CaveXML defines only these 22 elements, although additional elements may be added in future. No other elements are allowed, but there may be ways of adding another namespace.

-   The elements must appear in the order listed above.

-   Text uses the UTF-8 character set (Unicode), so characters from many languages can be used.

-   XML has five **special characters**: ampersand &, single quote ', double quote ", smaller than \<, and larger than \>. That doesn't mean these characters cannot be used; it depends on how they are used. For example, \> can be used in front of a number without problem. In URLs '&' must be replaced with `%26`.

-   **Almost-numerical entries:** Length entries are usually numbers, but they can also be of the form "\>42000", "\~100", or "2000+". A data type "ExtendedUnsignedInteger" has been created in CaveXML for this purpose. ExtendedUnsignedIntegers are positive integers that can contain a few additional symbols. The symbols "\>" and "\~" are allowed in front of the number. The number should contain no comma or decimal point, and digits after the decimal point are prohibited to avoid ambiguity. The elements [length], [vertical-extent], and [number-of-entrances] are ExtendedUnsignedIntegers and therefore obey the same syntax rules. Length and vertical extent must be rounded to the nearest whole meter. After the number, a "+" symbol is allowed, which has the meaning "or more". Mathematically it corresponds to \> for integers (such as the number of cave entrances) and ≥ for decimal numbers (such as length, altitude, and vertical extent). Only one symbol is allowed in front of the number, but note that "\>\~100" is equivalent to "\~100+". However, "10+" for the number of cave entrances is equivalent to "\>9". The element [altitude] also accepts ExtendedUnsignedIntegers, along with additional types of entries.



CaveXML data types
------------------

The use of well-defined data types facilitates storage and querying of the data. Among the built-in XML data types, CaveXML uses or builds on the following four: String, token, decimal, and anyURI. The default character set for a string is UTF-8, which encodes over one hundred thousand characters, so a string can include characters from many languages. A "token" in XML is a string with insignificant whitespaces ignored. Specifically, a token ignores leading and trailing spaces, internal sequences of consecutive spaces, carriage return, line feed, and tab characters. For example, the token representation of the string " \~20" is "\~20". The data type "token" is helpful when comparing with pre-defined strings or when applying RegEx patterns. The XML data type "decimal" is a floating-point number without exponent notation, and is ideal for representing latitude and longitude. The XML data type "anyURI" is intended for Uniform Resource Identifiers (URIs) and merely disallows certain special characters in a string.  

XML allows the writers of Schema to add restrictions to a built-in data type. One type of restriction for a string or token is a pre-defined list of strings, for example the list of all countries in the world. The use of pre-defined terms (a controlled vocabulary) is obviously helpful for queries. Entries that are not on the list of pre-defined strings are not valid within CaveXML (i.e., an error will occur when the XML database is validated against the XML Schema) and will therefore already be identified during the data compilation stage.

The [cave-id] field can consistent of a subset of ASCII characters. Technically this is implemented as a RegEx pattern that allows ASCII codes 43-57 (a few symbols and the ten digits) and 65-90 (the capital letters, A-Z). The RegEx expression is `[+-9A-Z]*`. This includes five symbols, the numbers, and capital letters. It does not include small letters or whitespaces. (Nevertheless, whitespaces are allowed at the beginning and the end, because [cave-id] is a token rather than a string.) POSIX defines ASCII characters that are especially portable. The POSIX subset of the ASCII characters are the ten digits, the letters (small and capital), and three symbols: hyphen (ASCII code 45), period (46), and underscore (95). However, a frequently used symbol in cave-ids is the forward slash (ASCII code 47). Whereas 38 of the 41 allowed characters for [cave-id] are POSIX portable, three extra are included: plus (43), comma (44), and the forward slash (47).   

For quantities such as length or vertical extent, it is desirable to allow entries such as >5000, ~100, and 7+. The cave is at least 5000 meters long; it is approximately 100 meter deep, and has 7 or more entrances. A purely numerical data type would be too restrictive. For this purpose, CaveXML defines the user-derived data type ExtendedUnsignedInteger, which can represent such patterns. An ExtendedUnsignedInteger allows one of two symbols in front of the number: \~ (approximate) or \> (larger than). The number is an integer of any length, without commas or periods. This choice was made because commas and periods can lead to ambiguities. For example, "2,007" could be interpreted as approximately 2&nbsp;km or approximately 2&nbsp;m. In some countries the decimal point is a period, in others it is a comma. Lengths and depths can rarely be defined more accurately than one meter anyway. Hence, integers suffice to represent length, vertical extent, and certainly the number of cave entrances. In accordance with the UISIC recommendation, CaveXML defines the vertical extent as positive, irrespective of whether a cave leads upslope or downslope from the entrance, so an unsigned representation is perfect. Technically, an ExtendedUnsignedInteger is defined within the CaveXML Schema as token restricted by a set of RegEx patterns. This pattern is consistent with expressions such as \>5000, \~100, 7+, and with all integers. Examples of non-matching patterns are: 123.4, \>\~2000, 100-200, and anything that contains a letter. Note that for a floating-point number \>\~2000 is practically equivalent to \~2000+, and the latter is a valid ExtendedUnsignedInteger.

Entries for altitude (elevation) can be even more varied, e.g., "1220-1570" to indicate the range of altitudes from the lowest to the highest entrance. The UISIC recommends an element [altitude-comment] so the meaning of the numerical value for the altitude could be clarified, e.g. "1220 lower entrance", or "2500 coarse" to indicate the altitude is approximate. For caves with more than one entrance, multiple altitude entries might be needed. The altitude must be queryable numerically, e.g., the user would search for caves with altitudes above 4000 m a.s.l. It can be decided later whether \~4000 and \>3000 should be compatible with this condition or not, i.e., whether the user wishes to find caves that are definitely above this altitude or merely might be above this altitude. After considering various options, the implementation chosen for CaveXML was to have a single [altitude] element which can hold specific patterns of numbers and strings. Three types of entries are allowed:
i) An unsigned integer or an ExtendedUnsignedInteger optionally followed by a comment. The comments are restricted to a subset of ASCII characters.
ii) A negative integer optionally preceded by ~, and optionally followed by a comment, where comments are again restricted to a subset of ASCII characters.
iii) A range of integers, such as 100-200, and not followed by a comment. A query function can interpret "100-200" as two altitude entries: "100" for the lowermost entrance and "200" for the uppermost entrance. Allowing ranges to be entered is convenient for the person who compiles the data. Three dash-like symbols are allowed as range delimiter: hyphen-minus (the only dash-like symbol in the ASCII character set), en-dash, and em-dash. There may be a few additional dash-like symbols in Unicode, which are not accepted.   

Technically, the data type for the altitude element is implemented as a token restricted by one of three RegEx patterns. Altitude values (in meters) are restricted to at most five digits, as no mountain in the solar system is taller than that. The comments allowed as part of an altitude entry are those consistent with the RegEx pattern `[ ,()\w]\*`, that is, they can contain spaces, commas, parentheses, and alphanumerical characters. Other characters, such as dashes and semicolons, are not allowed in a comment following an altitude value. Dashes serve as range delimiter and can be relied upon by a parsing function to distinguish between a range and an entry with a single number, whereas "-" as the very first symbol indicates a negative altitude.  

This concludes the description of all the data types that have been defined in the CaveXML Schema. Table 1 shows the data types associated with each CaveXML element. None of the elements is required to appear in a record, and some elements can occur no more than once.

| Element               | XML data type | Restrictions | Example |  
|:----------------------|:-------------:|:------------:|:--------|  
|\<country-name\> | token with restriction | pre-defined list of strings | Austria |  
|\<state-or-province\> | string | - | California |  
|\<phys-area-name\> | string | - | Pyrenees |
|\<principal-cave-name\>| string | maxOccurs=1 | Kolowrathöhle |  
|\<other-cave-name\> | string | - | M-340 |
|\<cave-id\> | token with restriction | RegEx pattern, ASCII | HSS-1547/9 |
|\<latitude\> | decimal with restriction | range -90...+90, maxOccurs=1 | 47.72792 |
|\<longitude\> | decimal with restriction | range -180...+180, maxOccurs=1 | 13.00858 |
|\<altitude\> | token with restriction | RegEx pattern | \~1500 main entrance |
|\<length\> | ExtendedUnsignedInteger | maxOccurs=1 | \>5000 |
|\<vertical-extent\> | ExtendedUnsignedInteger | maxOccurs=1 | 240 |
|\<number-of-entrances\>| ExtendedUnsignedInteger | maxOccurs=1 | 7+ |
|\<map-link\> | anyURI | - | http://www.mexicancaves.org/maps/1944.pdf |
|\<rock-type\> | token with restriction | pre-defined list of strings | limestone |
|\<cave-type\> | token with restriction | pre-defined list of strings | glacier cave |
|\<contents\> | token with restriction | pre-defined list of strings | waterfall(s) |
|\<comments\> | string | - | Mauna Loa flow of 1855 |
|\<cave-system\> | string | maxOccurs=1 | Labyrinth Cave System | 
|\<branch-name\> | string | -| Blue Grotto |
|\<reference\> | string | - | Yonge et al. (2018) doi:10.1016/B978-0-12-811739-2.00015-2 |
|\<cave-use\> | token with restriction | pre-defined list of strings | guided tourist cave |
|\<curation\> | string | - | updated length based on Smith et al. (2020) |


Table 1: Data types for each CaveXML element. Default attributes are *minOccurs=0* and *maxOccurs=unbounded*. The third column shows restrictions on the element or on its value. The last column contains examples of valid entries.  


Further Discussion
------------------

**Design Principles**  

CaveXML is designed to provide convenience for data entry, while also being strict and logical enough to allow for a great deal of automated data processing. Here are a few examples:  
- A number can be entered as "~500" to mean "approximately 500" or "10+" to mean "10 or more", but only a few specific symbols are allowed in front and after the number to ensure every entry can be successfully parsed and understood.  
- Records for caves that are connected with one another can be linked automatically.  
- For references to the published literature, a doi (digital object identifier) suffices to automatically generate a hyperlink. Even the bibliographic information can be automatically sourced based purely on the doi.  
- CaveXML records do not have a catalog number. Unique record identifiers can be generated automatically, when needed.  

There is a profound and mutual relation between the data exchange standard and its implementation: *All of the requirements of the CaveXML data exchange standard can be implemented with an XML schema definition.* More specifically, the requirements can be verified within version 1.0 of XML schema definitions, and do not require the extended capabilities of version 1.1.
For example, if the [cave-id] were required to be unique among records, this could not be verified with an XML schema, because it would require cross-comparisons between records.
This design choice, that the CaveXML data exchange standard can be fully verified with an XML schema definition, has two practical consequences.
First, verifying that a database is consistent with the CaveXML exchange standard requires nothing beyond an XML validation. No additional software or validation step are necessary.
Second, *all* of the specifications can be verified during the XML validation. Hence, any software used to process CaveXML data can rely on the specifications being followed completely.
This design choice leads to simplicity and rigor. It also protects the interchange standard from making demands that might be difficult to verify. For this reason 'XML' is included in the name of the standard.  


**Unique record identifier**

CaveXML entries do not include a catalog number that would uniquely identify a record. This is intentional. Catalog numbers are not a physical property of the cave and there is no fundamental reason to use them.  

A unique record identifier can be generated in form of a hash code based on the totality of entries in the record. The hash function is a deterministic procedure that turns an input of arbitrary length into an output of fixed length. For example, the MD5 hash generates a 32-character hexadecimal code, and the probability that the same MD5 hash is produced from different inputs is essentially zero. The same record always results in the same hash. When the record is edited, the hash code changes.
Practically, the hash code could be generated based on a limited number of entries, such as [state-or-province], [phys-area-name], and cave names (principal and other). The strings are merged into a single long string that serves as input for a hash code generator. Two caves in close vicinity of each other should not have the same name, so they ought to differ in one of those fields. And if location information is omitted from the record and the cave name is not unique, the ambiguity is fundamental.
Hence, unique record identifiers can be generated automatically from CaveXML data records. They are not permanent, because they change with even minor edits.   

Another approach to generating unique record identifiers would have been to use the country name (or its ISO letter abbreviation) plus the national cave id, if available. Cave ids, such as cave numbers or cadastral numbers, are usually unique for each cave. A record may have more than one cave-id and, in principle, could even have more than one [country-name], but as long as a national cave id is available and unique to the cave, it could be used as unique record identifier. There is one infrequent situation that introduces a serious flaw to this approach, namely that sometimes a cave system inherits its id number from one of its branches, namely when the system of assigning identification numbers is based on entrances. For example, Eisrohrhöhle and the Eisrohrhöhle-Bammelschacht-System both have the cadastral number 1337/118. This introduces fundamental ambiguities, which should be resolved at a level beyond the CaveXML interchange format definitions.  


**Automated cross-linking between cave systems and their branches**

When a cave system consists of several branches that have their own record in the database, they can be cross-linked. The elements [cave-system] and [branch-name] point to a [principal-cave-name], but cave names might not be unique, even within the same country, so a more sophisticated approach is needed to unambiguously cross-link a cave system with its branches.  When [cave-system] points to a [principal-cave-name], that record should include a [branch-name] that points back to the [principal-cave-name] of the referring record. This two-way reference guarantees that correct cross links have been established.  

CaveXML allows [cave-system] and [branch-name] to both be present simultaneously in the same record, and hence a hierarchy of levels is possible. However, since at most one [cave-system] entry is allowed in a record, it can only refer to the next-highest level in the hierarchy. Multiple [branch-name] entries are allowed, so a reference could be made to a branch that is more than one hierarchical level below, but that entry cannot be back-linked, so listing second-order branches in a single record would be of limited usefulness. In the terminology of data structures, cave systems are organized as trees, not as graphs. Organizing cave branches as trees rather than as undirected graphs is a natural choice, because the XML data model itself corresponds to hierarchical trees.   


**Character string normalization in support of search queries (approximate matching)**

Cave names may be written with the characters of the local language, and use of the UTF-8 character set (Unicode) makes this possible. For searches, however, one may prefer to use a more restricted character set, perhaps only the 26 letters of the English alphabet that are contained in the ASCII character set. For example, Scărişoara Cave in Romania should be found in the database by just typing Scarisoara. In Hawaii there is a cave named Kaʻūpūlehu, which one would want to find by just typing Kaupulehu. For this purpose, a function is needed that reduces words written with Unicode characters to an ASCII character set. (Variations in spelling can be entered in the field [other-cave-name], but entering all conceivable variants would be onerous and unnecessary.)  

The ideal transcription of symbols into ASCII characters depends on the language. For example, the German Umlaut 'ü' is properly transcribed as 'ue', but the same character is also used in Azerbaijani, Basque, and Hungarian, where it is better transcribed simply as 'u'. So far, CaveXML provides no mechanism for specifying the language a cave name is written in; a language attribute for cave names would be a welcome upgrade.  

Within the scope of language-independent character-by-character transcriptions, the Python function 'unidecode' provides lossy ASCII transliterations of Unicode text, and it can serve as a case study for the reduction of cave names into the ASCII character set. Two such Python modules are available: text-unidecode and unidecode. The unidecode function converts 'Scărişoara' into 'Scarisoara'. It also works with non-Latin alphabets. The Korean cave name '쌍용굴' is translated by unidecode to 'sangyonggul', which is indeed a name that is also used for this cave, although it is more often written with a second 'S' in front as 'Ssangyonggul'.
Unidecode does not remove spaces, dashes, or apostrophes. Certainly, one would want to find Aladdin's Cave with or without typing the apostrophe. Hence additional simplifications should be made after applying the unidecode function, including setting all letters to lower case. One possibility is to omit all characters that are not alphanumerical Latin characters, but obviously only after and not before the unidecode function is applied.  

The same transliteration function can also be applied to the search term. The database entry "Kaʻūpūlehu" will turn into "kaupulehu", and when the user types "Ka'upulehu", it will also be converted into kaupulehu and match the database entry.
Of course this is not perfect. 'Hoehle' will not match 'Höhle'. However, the case study demonstrates that names can be normalized reasonably well automatically, without placing any constraints on the characters allowed in the cave name field.  


**Scalability**

The worldwide database of the Grottocenter currently contains 60,182 caves. Hence, a worldwide database of natural caves significant enough to be worth cataloging might contain on the order of 100,000 records, and national databases will be much smaller.
This means that a CaveXML database fits easily in memory, whether it be desktop computer, laptop, or cell phone. CaveXML records consist only of text, not photos, maps, or videos, which can only be linked to.  

From a computational point of view, going through a list of this length is lightning fast, so it can be done on-the-fly and basic linear-time search methods suffice. To link records of cave branches that belong to the same cave, cross-comparisons have to be made. Only a fraction of records potentially have interconnections (i.e., either [cave-system] or [branch-name] is present and not empty), so even these cross-comparisons can be performed quickly. CaveXML data can be pre-processed to generate auxiliary entries. This may be convenient, but from a computational point of view, it should be unnecessary.
In conclusion, simple methods of storing and searching data are expected to scale up to the expected size of a global CaveXML database.  
