def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        print(a)
        temp = a + b
        a = b
        b = temp

n = int(input("Enter the number upto which fibonacci is calculated: "))
fibonacci(n)