
import collections

kmer = 4
in_genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
in_mistake = 1
out_result = []
mismatch_list = []

def hamming_distance(s1, s2):
    # Return the Hamming distance between equal-length sequences
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    else:
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

for i in xrange(len(in_genome)-kmer + 1):
    v = in_genome[i:i + kmer]
    out_result.append(v)

for t_kmer in set(out_result):
    for s_kmer in out_result:
        if hamming_distance(t_kmer, s_kmer) <= in_mistake:
            mismatch_list.append(t_kmer)

mismatch_count = collections.Counter(mismatch_list)
print [key for key,val in mismatch_count.iteritems() if val == max(mismatch_count.values())]
print mismatch_count.most_common()

