def anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
print(anagrams(str1, str2))