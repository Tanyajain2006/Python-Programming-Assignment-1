def write():
    text_file = open("C:/Users/Admin/OneDrive/OfficeMobile/Python Programming Assignment 1/Text File.txt", 'w')
    print(str, file = text_file)

str = input("Enter a greeting message: ")
write()