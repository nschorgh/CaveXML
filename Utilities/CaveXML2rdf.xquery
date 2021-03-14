(: Run with:
saxonb-xquery -q:CaveXML2rdf.xquery > res.rdf
Validate RDF/XML with:
$JENA/bin/riot --validate res.rdf
https://ontology.uis-speleo.org/howto/
:)
declare namespace karstlink = "https://ontology.uis-speleo.org/ontology/#" ;
declare namespace schema = "https://schema.org/" ;
declare namespace rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ;
declare namespace gn = "http://www.geonames.org/ontology#" ;
declare namespace w3geo = "http://www.w3.org/2003/01/geo/wgs84_pos#" ;
declare namespace dct = "http://purl.org/dc/terms/" ;
declare namespace rdfs=" http://www.w3.org/2000/01/rdf-schema#" ;
declare namespace cavexml="https://github.com/nschorgh/CaveXML/raw/master/cavexml.owl.ttl#" ;
declare namespace xsd="http://www.w3.org/2001/XMLSchema#" ;

declare function local:processRoot($doc as node()) as element()* {
    for $rec in $doc/CaveDataBase/record
      return local:processRecord($rec)
};

declare function local:processTag($tags as element()*, $inputElementName as xs:string ) as element()* {
  for $tag in $tags
    return
        if($tag / text() != "" ) then
          element { $inputElementName } { $tag / text() } 
        else ()
};

declare function local:processReferences($tags as element()*) as element()* {
  for $tag in $tags
    return local:processReference($tag)
};

declare function local:processReference($tag as element() ) as element()* {
  let $text := $tag / text()
  return
    if($text != "" ) then
      let $possibleURL := fn:replace($text, ".*(https?://.*)", "$1" )
      return
        if( fn:starts-with( $possibleURL, "http") ) then
          element dct:references {
            attribute rdf:resource { $possibleURL }
          }
        else element dct:references { $possibleURL }
    else ()
};

declare function local:processRecord($rec as element()) as element()* {
  let $cave-id := $rec/cave-id[1]
  return
  <karstlink:UndergroundCavity>
    {
        if($cave-id != "" ) then
            attribute rdf:ID { $cave-id }
        else ()
    }
    { local:processTag( $rec/country-name, "schema:addressCountry" ) }
    { local:processTag( $rec/state-or-province, "schema:addressLocality" ) }
    { local:processTag( $rec/phys-area-name, "schema:addressLocality" ) }
    { local:processTag( $rec/principal-cave-name, "rdfs:label" ) }
    { local:processTag( $rec/other-cave-name, "gn:alternateName" ) }
    { local:processTag( $rec/latitude, "w3geo:latitude" ) }
    { local:processTag( $rec/longitude, "w3geo:longitude" ) }
    { local:processTag( $rec/altitude, "w3geo:altitude" ) }
    { local:processTag( $rec/length, "karstlink:length" ) }
    { local:processTag( $rec/vertical-extent, "karstlink:verticalExtent" ) }
    { local:processTag( $rec/number-of-entrances, "cavexml:number-of-entrances" ) }
    { local:processTag( $rec/map-link, "schema:hasMap" ) }
    { local:processTag( $rec/rock-type, "cavexml:rock-type" ) }
    { local:processTag( $rec/cave-type, "cavexml:cave-type" ) }
    { local:processTag( $rec/contents, "cavexml:contents" ) }
    { local:processTag( $rec/comments, "rdfs:comment" ) }
    { local:processTag( $rec/cave-system, "schema:containedInPlace" ) }
    { local:processTag( $rec/branch-name, "karstlink:relatedToUndergroundCavity" ) }
    { local:processReferences( $rec/reference ) }
    { local:processTag( $rec/cave-use, "cavexml:cave-use" ) }
    { local:processTag( $rec/curation, "cavexml:curation" ) }
  </karstlink:UndergroundCavity>
};


let $sourceURL := "https://github.com/nschorgh/CaveXML/raw/master/allcaves-database.xml"
(: testing a local file:
let $doc := doc("allcaves-database-small.xml")
:)
let $doc := doc( $sourceURL )
let $baseURL := "https://github.com/nschorgh/CaveXML/raw/master/Derivatives/allcaves-database.rdf#"

return
<rdf:RDF
    xmlns:w3geo="http://www.w3.org/2003/01/geo/wgs84_pos#"
    xmlns:dbpedia="http://dbpedia.org/resource/"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:marcgt="http://id.loc.gov/vocabulary/marcgt/"
    xmlns:gn="http://www.geonames.org/ontology#"
    xmlns:dsw="http://purl.org/dsw/"
    xmlns:dct="http://purl.org/dc/terms/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:dwc="http://rs.tdwg.org/dwc/terms/"
    xmlns:cc="http://creativecommons.org/ns#"
    xmlns:dwciri="http://rs.tdwg.org/dwc/iri/"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#"
    xml:base="{$baseURL}"
>
  { local:processRoot($doc) }
</rdf:RDF>

