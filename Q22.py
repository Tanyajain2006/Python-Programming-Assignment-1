def max_min():
    list = [2, 3, 5, 1, 4]
    max = list[0]
    min = list[0]
    for i in list:
        if(i > max):
            max = i
        if(i < min):
            min = i
            
    print("Maximum element:", max)
    print("Minimum element:", min)

max_min()