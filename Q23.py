# converting celsius to fahrenheit
def fahrenheit(c):
    f = ((9 * c) / 5) + 32
    return f

c = float(input("Enter temperature in celsius: "))
print("Temperature in fahrenheit:", fahrenheit(c))

# converting fahrenheit to celsius
def celsius(f):
    c = ((f - 32) * 5) / 9
    return c


f = float(input("Enter temperature in fahrenheit: "))
print("Temperature in celsius:", celsius(f))