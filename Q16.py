def frequency(str):
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for key, value in count.items():
        print(f"{key} occurs {value}")

str = input("Enter string: ")
frequency(str)