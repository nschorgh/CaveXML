README
======

CaveXML is a data interchange format for the purpose of facilitating scientific research on caves. This repository provides: CaveXML element and data type definitions, an example database, and tools to work with CaveXML-formatted data.  


The most important files:  
   [`cavexml.md`](./cavexml.md)	  (explains the CaveXML standard)  
   `cavexml.xsd`		  (XML Schema Definition of CaveXML)  
   `allcaves-database.xml`  (Master version of the database in native format)  
   `Derivatives/allcaves-database.csv`  (csv version of the database generated from the XML version)  
   `Utilities/cavexml.py`	  (Python functions for CaveXML)  

Auxiliary files:  
   `cavexml-db-table.css`	  (minimalist Style Sheet so the XML database can be viewed in a webbrowser)  
   `Derivatives/allcaves-database.md` (Full records in Markdown format, generated from the XML version)  
   `Derivatives/allcaves-database.rdf` (XML/RDF version of database for KarstLink)  
   `Derivatives/list-of*.md`	  (various lists of selected entries from the database)
   `Derivatives/metadata.rdf`	  (a file used by the RDF ontology)  
   `Utilities/cavexml2csv.py`     (converts database to comma-separated-values using Python)  
   `Utilities/cavexml2html.py`    (outputs full records in HTML format)  
   `Utilities/cavexml2kml.py`	  (converts coordinates in CaveXML entries into KML format)  
   `Utilities/cavexml2md.py`      (creates filtered list of entries in Markdown format)  
   `Utilities/cavexml2md-full.py` (creates allcaves-database.md)  
   `Utilities/CaveXML2rdf.xquery` (converts database to RDF/XML using XQuery)
   `Utilities/CaveXML2rdf.py` 	  (converts database to RDF/XML using Python)  
   `Utilities/cavexml-auxiliary.py` (creates auxiliary information from database entries)  
   `Utilities/cavexml-warnings.py`   (issues informative warnings)   
   `Utilities/cavesystemfinder.py`   (connects cave branches with cave systems)  
   `Utilities/filter.xquery`      (creates simple filtered list of entries using XQuery)  
   `Utilities/reorder.xslt`    	  (sorts elements within each record)  

This is a pilot project to explore the capabilities of a CaveXML implementation end-to-end. The actual database is for demonstration, and mainly contains ice caves and lava tubes.


## Technical Notes

`cavexml.md` describes the meaning of the XML elements used to organize the data, and restrictions for the entries.

The master copy of the database is in XML format (`allcaves-database.xml`). With the help of `cavexml-db-table.css` the database content can be viewed in a web browser, but this provides a rather poor viewing experience.
Users can open `allcaves-database.csv` as a spreadsheet. `cavexml-numeric.py` generates an auxiliary file that contains, among other columns, minimum and maximum altitude, and it can be uploaded into the same spreadsheet to support numerical searches on quasi-numerical entries.  

The Python programs serve as examples for how a CaveXML database can be loaded and analyzed within Python. Parsing functions for quasi-numerical entries are found in `cavexml.py`, which also contains many other functions useful for working with CaveXML data.

The XML schema definition `cavexml.xsd` incorporates all CaveXML requirements. The following validates a database against the Schema:  

    xmllint --schema cavexml.xsd allcaves-database.xml -noout  

Alternatively, various online tools can be used to validate an XML database against an XSD document.  


## Acknowledgments

Thanks to Jean-Marc Vanel for help with XML and XQuery - March 2021


