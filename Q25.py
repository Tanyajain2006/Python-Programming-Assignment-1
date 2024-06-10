def q25():
    text_file1 = open("C:/Users/Admin/OneDrive/OfficeMobile/Python Programming Assignment 1/TextFile1.txt", 'w')
    print(list1, file = text_file1)

    list2 = list1.copy()
    text_file2 = open("C:/Users/Admin/OneDrive/OfficeMobile/Python Programming Assignment 1/TextFile2.txt", 'w')
    print(list2, file = text_file2)

list1 = [1, 2, 3, "Hello", True, 20.02, 20+2j]
q25()