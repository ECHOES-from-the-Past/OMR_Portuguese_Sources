This folder contains files for testing the Neon to Aquitanian script.

Sample_MEI.mei - An MEI from PAM analyzer which can be run through aquit_preprocess.py to create a simulation
of a Neon Aquitanian script
Usage: 
py aquit_preprocess.py path/Sample_MEI.mei

modified_aquit.mei - An MEI from running the script above

Sample_Text_1.txt - Text from the folio that has been split into 4 lines. Each line contains no overflow
from other pages (e.g., all text in the file is on the page). Generates 4 MEI files.
Usage:
py neon_to_mei.py path/modified_aquit.mei path/Sample_Text_1.txt

Sample_Text_2 - Text from the folio split into 4 lines. The first and last line contain extra text as
overflow from the previous and next pages. Generates 4 MEI files.
Usage:
py neon_to_mei.py path/modified_aquit.mei path/Sample_Text_2.txt

Sample_Text_3 - Text from the folio with 6 total lines. The first and last lines are not present on the page.
Geneates 6 MEI files, with the first and last being empty. 
Usage:
py neon_to_mei.py path/modified_aquit.mei path/Sample_Text_3.txt
