This folder contains scripts to convert Aquitanian MEIs from Neon into Aquitanian MEIs for PAM

There are 2 Python scripts:
1. aquit_preprocess.py - Since there aren't any complete MEIs from Neon, this is used to convert a PAM MEI into
the same format as one from Neon which can be used to test
**Usage: py aquit_preprocess <mei_filepath>**
2. neon_to_mei.py - Takes in a Neon MEI and txt file, converts it into mei(s) that can be used in PAM
**Usage: py neon_to_mei.py <mei_filepath> <txt_filepath>**

The following changes are made in this conversion:
1. Given a text with n lines, produces n mei's (up to 2 may be empty)
    - Each mei contains syllables and zones from its corresponding text line
2. Remove @clef.line and @clef.shape from @staffDef
3. Switch @lines in @staffDef to 1
4. Remove colLayout
5. Set @syl wordpos
6. Remove custos
7. Convert pname and oct to loc
