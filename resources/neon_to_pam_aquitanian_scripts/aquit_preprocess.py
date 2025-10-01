# Author: Deanna Chun (github.com/DeannaLC)

# Preprocess completed Aquitanian scripts from PAM for testing by doing the following:
# - Adds zones and facs for @nc and @syl elements
# - Removes @wordpos
# - Replace @loc with @pname + @oct
# - Add @colLayout with 2 cols
# - Set @staffDef.lines = 5, @staffDef.clef.line = 2, @staffDef.clef.shape = C

import xml.etree.ElementTree as ET
import sys

ns = "{http://www.music-encoding.org/ns/mei}"
xml_ns = "{http://www.w3.org/XML/1998/namespace}"

to_pname_oct = {
    "6": ("d", "5"),
    "5": ("c", "5"),
    "4": ("b", "4"),
    "3": ("a", "4"),
    "2": ("g", "4"),
    "1": ("f", "4"),
    "0": ("e", "4"),
    "-1": ("d", "4"),
    "-2": ("c", "4"),
    "-3": ("b", "3"),
    "-4": ("a", "3"),
    "-5": ("g", "3"),
    "-6": ("f", "3")
}

#Replace loc with pname and oct for testing
def remove_locs(mei):
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    for syllable in syllables:
        neumes = syllable.findall(f"{ns}neume")
        for neume in neumes:
            ncs = neume.findall(f"{ns}nc")
            for nc in ncs:
                loc = nc.attrib["loc"]
                pname, oct = to_pname_oct[loc]
                nc.set("pname", pname)
                nc.set("oct", oct)
                del(nc.attrib["loc"])

def modify_staffDef(mei):
    staffDef = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}scoreDef/{ns}staffGrp/{ns}staffDef")
    staffDef.set("lines", "5")
    staffDef.set("clef.line", "2")
    staffDef.set("clef.shape", "C")

def add_colLayout(mei):
    score = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score")
    colLayout = ET.Element(f"{ns}colLayout")
    colLayout.set("cols", "2")
    score.append(colLayout)
    
# Remove wordpos for testing
def remove_wordpos(mei):
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    for syllable in syllables:
        syl = syllable.find(f"{ns}syl")
        del(syl.attrib["wordpos"])
        if "con" in list(syl.attrib):
            del(syl.attrib["con"])

# Add facs to @nc and @syl, then create @zone where zone id = nc/syl fac
def add_zones(mei):
    facsimile = ET.Element(f"{ns}facsimile")
    surface = ET.Element(f"{ns}surface")
    music = mei.find(f"{ns}music")
    facsimile.append(surface)
    music.append(facsimile)
    layer = music.find(f"{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    id = 0
    for syllable in syllables:
        neumes = syllable.findall(f"{ns}neume")
        syl = syllable.find(f"{ns}syl")
        syl.set("facs", "#" + str(id))
        id += 1
        surface.append(ET.Element(f"{ns}zone", {f"{xml_ns}id":syl.attrib["facs"][1:]}))
        for neume in neumes:
            #surface.append(ET.Element(f"{ns}zone", {f"{xml_ns}id":neume.attrib[f"{xml_ns}id"]}))
            ncs = neume.findall(f"{ns}nc")
            for nc in ncs:
                nc.set("facs", "#" + str(id))
                surface.append(ET.Element(f"{ns}zone", {f"{xml_ns}id":nc.attrib["facs"][1:]}))
                id += 1

if len(sys.argv) < 2:
    print("Usage: python aquit_preprocess.py <mei filepath>")
    sys.exit(1)

ET.register_namespace("", "http://www.music-encoding.org/ns/mei")
filepath = sys.argv[1]
tree = ET.parse(filepath)
root = tree.getroot()
remove_locs(root)
remove_wordpos(root)
add_zones(root)
add_colLayout(root)
modify_staffDef(root)
tree.write("modified_aquit.mei", xml_declaration=True, encoding='utf-8')