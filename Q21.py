def q21(target):
    list = [1,2,1,2,3,1,1,3,3,3,3,5]
    count = 0
    for i in list:
        if(i == target):
            count = count + 1
    return count

target = int(input("Enter number that you want to find in list: "))
print(q21(target))
    