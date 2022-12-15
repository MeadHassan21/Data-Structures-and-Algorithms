def bubbleSort(list_m):
    indexing_lenght = len(list_m) - 1
    sorted = False 
    
    while not sorted:
        sorted = True
        for i in range(0,indexing_lenght):
            if list_m[i] > list_m[i+1]:
                sorted = False
                list_m[i], list_m[i+1] = list_m[i+1], list_m[i]
    return list_m
    


