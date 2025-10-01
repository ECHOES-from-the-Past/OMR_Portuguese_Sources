# Author: Deanna Chun (github.com/DeannaLC)

# Converts an Aquitanian Neon MEI into PAM MEI(s) doing the following:
# - Given a text with n lines, creates n mei's (with up to 2 empty) where each mei contains syllables + zones from the line
# - Set @staffDef.lines = 1, remove @staffDef.clef.line and @staffDef.clef.shape
# - Remove colLayout
# - Convert @pname and @oct to @loc using the below chart
# - Remove custos
# - Set @syl wordpos based on syllables' positions in words

import xml.etree.ElementTree as ET
import sys

ET.register_namespace("", "http://www.music-encoding.org/ns/mei")
ns = "{http://www.music-encoding.org/ns/mei}"
xml_ns = "{http://www.w3.org/XML/1998/namespace}"

# Chart for converting pname and oct to loc:
#   B4 --------------------------------------   4
#   A4                                          3
#   G4 --------------------------------------   2
#   F4                                          1
#   E4 --------------------------------------   0
#   D4                                          -1
#   C4 --------------------------------------   -2
#   B3                                          -3
#   A3 --------------------------------------   -4

to_loc = {
    ("d", "5"): "6",
    ("c", "5"): "5",
    ("b", "4"): "4",
    ("a", "4"): "3",
    ("g", "4"): "2",
    ("f", "4"): "1",
    ("e", "4"): "0",
    ("d", "4"): "-1",
    ("c", "4"): "-2",
    ("b", "3"): "-3",
    ("a", "3"): "-4",
    ("g", "3"): "-5",
    ("f", "3"): "-6"
}

#Generate a dictionary where {zone id : zone}
def zone_map(mei):
    surface = mei.find(f"{ns}music/{ns}facsimile/{ns}surface")
    zones = surface.findall(f"{ns}zone")
    ret = {}
    for zone in zones:
        ret[zone.attrib[f"{xml_ns}id"]] = zone
    return ret

#Change staffDef lines to 1, remove clef
def edit_lines(mei):
    staffDef = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}scoreDef/{ns}staffGrp/{ns}staffDef")
    staffDef.set("lines", "1")
    del(staffDef.attrib['clef.line'])
    del(staffDef.attrib['clef.shape'])

#Remove colLayout
def delete_colLayout(mei):
    score = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score")
    colLayout = score.find(f"{ns}colLayout")
    score.remove(colLayout)

#Convert an nc's pname and oct to a loc (using dictionary above)
def pitch_to_loc(nc):
    oct = nc.attrib["oct"]
    pitch = nc.attrib["pname"]
    loc = to_loc[(pitch, oct)]
    nc.set("loc", loc)
    del(nc.attrib["oct"])
    del(nc.attrib["pname"])

#Convert all nc's pname an oct to a loc
def pitches_to_locs(mei):
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    for syllable in syllables:
        neumes = syllable.findall(f"{ns}neume")
        for neume in neumes:
            ncs = neume.findall(f"{ns}nc")
            for nc in ncs:
                pitch_to_loc(nc)

#Remove custos from the mei
def remove_custos(mei):
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    custos = layer.findall(f"{ns}custos")
    for custo in custos:
        layer.remove(custo)

#Set wordpos based on syllables' position in each word
def set_wordpos(mei, text):
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    split_text = text.split(" ")
    word = 0
    word_idx = 0
    for syllable in syllables:
        cur_word = split_text[word]
        syl = syllable.find(f"{ns}syl")
        syl_text = syl.text
        sect = cur_word[word_idx:word_idx+len(syl_text)]
        if syl_text == cur_word:
            syl.set("wordpos", "s")
            word += 1
        elif word_idx == 0:
            syl.set("wordpos", "i")
            word_idx += len(syl_text)
            syl.set("con", "d")
        elif word_idx + len(syl_text) == len(cur_word):
            syl.set("wordpos", "t")
            word_idx = 0
            word += 1
        else:
            syl.set("wordpos", "m")
            word_idx += len(syl_text)
            syl.set("con", "d")

#Set wordpos for the first line of text by removing words that aren't part of the chant
def set_first_wordpos(mei, text):
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    syl_idx = 0
    text_idx = 0
    to_remove = 1
    count = 1
    no_spaces = text.replace(" ", "")
    while text_idx < len(no_spaces) and syl_idx < len(syllables):
        cur_syl = syllables[syl_idx].find(f"{ns}syl").text
        cur_word = no_spaces[text_idx:text_idx+len(cur_syl)]
        if cur_syl == cur_word:
            syl_idx += 1
        else:
            to_remove = count
        text_idx += len(cur_syl)
        count += len(cur_syl)
    remove_words = no_spaces[:to_remove+1]
    text_idx = 0
    for word in text.split(" "):
        if text_idx + len(word) > len(remove_words):
            break
        if word == remove_words[text_idx:text_idx+len(word)]:
            text = text.replace(word, "", 1)
        text_idx += len(word)
    set_wordpos(mei, text.lstrip())

#Generate all text from an MEI
def all_text(mei):
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    ret = ""
    for syllable in syllables:
        syls = syllable.findall(f"{ns}syl")
        for syl in syls:
            ret += syl.text
    return ret

#Given the first line of text, separate the mei to contain only its syllables + zones
def separate_first(mei, text):
    keep_syllables = []
    block = text.replace(" ", "")
    block_idx = 0
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    syl_idx = 0
    while block_idx < len(block) and syl_idx < len(syllables):
        syllable = syllables[syl_idx]
        syl = syllable.find(f"{ns}syl")
        syl_word = syl.text
        if len(syl_word) + block_idx > len(block):
            break
        cur_text = block[block_idx:block_idx + len(syl_word)]
        if cur_text == syl_word:
            keep_syllables.append(syllable)
            block_idx += len(syl_word)
            syl_idx += 1
        else:
            keep_syllables = []
            block_idx += 1
    to_remove_syllables = []
    to_remove_ids = []
    for syllable in syllables:
        if syllable not in keep_syllables:
            to_remove_syllables.append(syllable)
            syl = syllable.find(f"{ns}syl")
            syl_facs = syl.attrib["facs"]
            to_remove_ids.append(syl_facs[1:])
            neumes = syllable.findall(f"{ns}neume")
            for neume in neumes:
                ncs = neume.findall(f"{ns}nc")
                for nc in ncs:
                    nc_facs = nc.attrib["facs"]
                    to_remove_ids.append(nc_facs[1:])
    for syllable in to_remove_syllables:
        layer.remove(syllable)
    zones = zone_map(mei)
    zone_ids = list(zones)
    surface = mei.find(f"{ns}music/{ns}facsimile/{ns}surface")
    for id in to_remove_ids:
        if id in zone_ids:
            remove = zones[id]
            surface.remove(remove)

#Given a section of text (middle or last lines), split the mei to contain only syllables and zones in that section
def separate(mei, text):
    keep_syllables = []
    block = text.replace(" ", "")
    block_idx = 0
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    for syllable in syllables:
        if block_idx >= len(block):
            break
        syl = syllable.find(f"{ns}syl")
        syl_word = syl.text
        if len(syl_word) + block_idx > len(block) + 1:
            break
        if block[block_idx:block_idx+len(syl_word)] == syl_word:
            keep_syllables.append(syllable)
            block_idx += len(syl_word)
        else:
            keep_syllables = []
            block_idx = 0
    to_remove_syllables = []
    to_remove_ids = []
    for syllable in syllables:
        if syllable not in keep_syllables:
            to_remove_syllables.append(syllable)
            syl = syllable.find(f"{ns}syl")
            syl_facs = syl.attrib["facs"]
            to_remove_ids.append(syl_facs[1:])
            neumes = syllable.findall(f"{ns}neume")
            for neume in neumes:
                ncs = neume.findall(f"{ns}nc")
                for nc in ncs:
                    nc_facs = nc.attrib["facs"]
                    to_remove_ids.append(nc_facs[1:])
    for syllable in to_remove_syllables:
        layer.remove(syllable)
    zones = zone_map(mei)
    zone_ids = list(zones)
    surface = mei.find(f"{ns}music/{ns}facsimile/{ns}surface")
    surface_zones = surface.findall(f"{ns}zone")
    for id in to_remove_ids:
        if id in zone_ids:
            remove = zones[id]
            surface.remove(remove)

def construct_text(mei):
    layer = mei.find(f"{ns}music/{ns}body/{ns}mdiv/{ns}score/{ns}section/{ns}staff/{ns}layer")
    syllables = layer.findall(f"{ns}syllable")
    ret = ""
    for syllable in syllables:
        syl = syllable.find(f"{ns}syl")
        ret += syl.text
        if syl.attrib["wordpos"] == "s" or syl.attrib["wordpos"] == "t":
            ret += " "
    return ret[:-1]

# Main script code
if len(sys.argv) < 3:
    print("Usage: python neon_to_mei.py <mei filepath> <txt filepath>")
    sys.exit(1)

mei_filepath = sys.argv[1]
txt_filepath = sys.argv[2]

with open (txt_filepath) as txt:
    first = True
    i = 1
    for line in txt:
        line = line.replace('\n', "")
        tree = ET.parse(mei_filepath)
        root = tree.getroot()
        edit_lines(root)
        delete_colLayout(root)
        remove_custos(root)
        if first:
            separate_first(root, line)
            set_first_wordpos(root, line)
            first = False
        else:
            separate(root, line)
            set_wordpos(root, line)
        tree.write(f"part{i}.mei")
        i += 1