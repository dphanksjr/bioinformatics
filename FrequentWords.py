###The FrequentWords function finds the most frequent k-mers in a string.###

from collections import Counter

def FrequentWords(text, k):
    mostFrequent=[text[i:i+k] for i in range(0,len(text),k-m)]
    printmostFrequent=Counter(mostFrequent).most_common()
    print(printmostFrequent)

text = 'AAATTGACGCAT'
k = 3
m = k-1
FrequentWords(text, k)
    