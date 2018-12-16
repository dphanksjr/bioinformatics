###This function finds the reverse complement of a string###
 
from string import maketrans
intab = 'ATCG'
outtab = "TAGC"

def ReverseComplement(input):
    trantab = maketrans(intab, outtab)
    complement = input.translate(trantab)
    reverseComplement = complement[::-1]
    print(reverseComplement)

input = 'CCAGATC'

ReverseComplement(input)