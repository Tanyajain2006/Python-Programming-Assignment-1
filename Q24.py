def calculator(a, o, b):
    if(o == "+"):
        return a + b
    elif(o == "-"):
        return a - b
    elif(o == "*"):
        return a * b
    else:
        if(b != 0):
            return a / b
        else:
            return "Invalid Input"       

a = float(input("Enter no1: "))
o = input("Enter operator(+, -, *, /): ")
b = float(input("Enter no2: "))
print(calculator(a, o, b))