#search for an amino acid sequence motif 

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import re

records = Seq("WALLLLFWLGWLGMLAGAVVIIVR", IUPAC.extended_protein)

#search = re.search("F.*?G", str(records))  #this is a lazy search.  works but is slower.
#should output FWLG
search = re.search("F[^G]*G", str(records))
print search.group()
###########################
import re
import cProfile

s = r'ACATCATCTATCTATACAATAAAAACTATCCCCTAACTACTACACTACTATCATCACATCATATCACTTTATATCCTAC'
for i in range(1,15):
    s = s + s

s = r'F' + s 
s = s + r'ATCTATCTATACAATAATCTATCTATACAATAATCTATCGATCTATCTATACAATAATCTATCTATACAATATCG' + s

cProfile.run('re.search(r"F[^G]+G",s)')