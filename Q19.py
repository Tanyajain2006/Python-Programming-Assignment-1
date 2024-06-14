def remove_punctuation(str):
    import string
    s = "" # creates an empty string
    for i in str:
        if(i not in string.punctuation):
            s = s + i
    return s

str = input("Enter string: ")
print(f"String after removing punctuation: {remove_punctuation(str)}")