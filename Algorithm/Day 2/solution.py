def Inventory_Update(arr1,arr2):
    for i in arr2:
        for j in arr1:
            if i[1] == j[1]:
                j[0] = j[0]+i[0]
    check = []
    for i in arr1:
        check.append(i[1])
    for i in arr2:
        if i[1] not in check:
            arr1.append(i)
    return arr1




print(Inventory_Update([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))