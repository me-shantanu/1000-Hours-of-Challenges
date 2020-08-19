from itertools import combinations
def return_index(*args):
    res = 0
    for arg in args[0:-1]:
        res = res + args[-1].index(arg)
    return res 

def Pairwise(arr,keyword):
    count = 0
    comb = combinations(arr,2)
    for i in list(comb):
        if sum(i) == keyword:
            count += return_index(i[0],i[1],arr)
    return count

print(Pairwise([7, 9, 11, 13, 15], 20))