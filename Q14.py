def multiple_lines():
    list = []
    while(True):
        line = input("Enter input: ")
        if(not line):
            break
        list.append(line)

    for i in list:
        print(i)

multiple_lines()