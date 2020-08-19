from itertools import permutations
def No_Repeats(strr):
    if len(strr) == 1:
        return 1
    else:
            perm = permutations(strr)
            count = 0
            for i in list(perm):
                j = 0
                while j != len(i)-1:
                    if i[j] == i[j+1]:
                        break 
                    else:
                        if j == len(i)-2:
                            count +=1
                            break
                        j +=1 
                            
                
            return count



print(No_Repeats('abfdefa'))