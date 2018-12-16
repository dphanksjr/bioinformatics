#finds where skew attains a minimum which gives an approximate location of ori (for E. coli)

input = 'GATACACTTCCCGAGTAGGTACTG'
n = 0
n_list = []
for i in input:
    if i == 'C':
        n = n-1
        n_list.append(n)
        print(n)
    elif i == 'G':
        n = n+1
        n_list.append(n)
        print(n)
    else:
        n_list.append(n)
        print(n)
n_list.insert(0,0)
print(n_list)

print(n_list.index(min(n_list)))
print(n_list.index(n_list))

#formatted_nlist = n_list[0:15]
formatted_nlist = [min(n_list)]

      
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

source = n_list
print(list_duplicates_of(source, min(n_list)))