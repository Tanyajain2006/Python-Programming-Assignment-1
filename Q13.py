def age(birth_year, current_year):
    return current_year - birth_year

birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))
print(age(birth_year, current_year))