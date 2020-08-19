def symmetric_difference(*args):
    arr_2D = []
    for arg in args:
        arr_2D.append(arg)

    if len(arr_2D) == 1:
        return arr_2D[0]
    elif len(arr_2D) == 0:
        print("please enter some argumnets for calculating symmetric difference")
    elif len(arr_2D) > 1:
        i = 2
        res = symmetric(arr_2D[0],arr_2D[1])
        if len(arr_2D) > 2:
            while i != len(arr_2D):
                res = symmetric(res,arr_2D[i])
                i +=1
            res.sort()
            x = list(set(res))
            return x
        else:
            res.sort()
            x = list(set(res))
            return res
    
def symmetric(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            result.append(arr1[i])

    for i in range(len(arr2)):
        if arr2[i] not in arr1:
            result.append(arr2[i])
    return result

finial = (symmetric_difference([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))
print(finial)
