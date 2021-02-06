<?xml version="1.0" encoding="utf-8"?>
<!-- This xslt script arranges the elements within each record in the order 
     required by the CaveXML standard.

     Usage:
            xsltproc reorder.xslt allcaves-database.xml 
-->
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
  
    <xsl:output method="xml" encoding="UTF-8" indent="yes"/>

    <xsl:template match="CaveDataBase">
        <xsl:copy>
            <!-- copy any children -->
            <xsl:apply-templates select="*"/>
        </xsl:copy>
    </xsl:template>

    
    <xsl:template match="record">
        <xsl:copy>
            <!-- <xsl:apply-templates select="@*" /> -->
            <xsl:apply-templates select="country-name" />
            <xsl:apply-templates select="state-or-province" />
	    <xsl:apply-templates select="phys-area-name" />
            <xsl:apply-templates select="principal-cave-name" />
            <xsl:apply-templates select="other-cave-name" />
	    <xsl:apply-templates select="cave-id" />
	    <xsl:apply-templates select="latitude" />
	    <xsl:apply-templates select="longitude" />
	    <xsl:apply-templates select="altitude" />
	    <xsl:apply-templates select="length" />
	    <xsl:apply-templates select="vertical-extent" />
	    <xsl:apply-templates select="number-of-entrances" />
	    <xsl:apply-templates select="map-link" />
	    <xsl:apply-templates select="rock-type" />
	    <xsl:apply-templates select="cave-type" />
	    <xsl:apply-templates select="contents" />
	    <xsl:apply-templates select="comments" />
	    <xsl:apply-templates select="cave-system" />
	    <xsl:apply-templates select="branch-name" />
	    <xsl:apply-templates select="reference" />
	    <xsl:apply-templates select="cave-use" />
	    <xsl:apply-templates select="curation" />
            <xsl:apply-templates select="*[not(self::country-name or 
					 self::state-or-province or 
					 self::phys-area-name or
					 self::principal-cave-name or 
					 self::other-cave-name or self::cave-id or
					 self::latitude or self::longitude or 
					 self::altitude or
					 self::length or self::vertical-extent or
					 self::number-of-entrances or
					 self::map-link or
					 self::rock-type or self::cave-type or
					 self::contents or self::comments or
					 self::cave-system or self::branch-name or
					 self::reference or
					 self::cave-use or self::curation 
					 )]"/>
        </xsl:copy>
    </xsl:template>

    <!-- this is the identity transform: 
	 it copies everything that isn't matched by a more specific template -->
    <xsl:template match="@*|node()"> 
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/> 
        </xsl:copy>
    </xsl:template>

</xsl:stylesheet>


<!-- Indentation can be changed with
     xmlstarlet fo -s 3 allcaves-database.xml
-->
