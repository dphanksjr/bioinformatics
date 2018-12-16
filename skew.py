###This program gives all values of Skewi 
input = 'GAGCCACCGCGATA'
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

###optional
#formatted_nlist = n_list[0:15]
#print(formatted_nlist)