def sum_digits(n):
    temp = n
    sum = 0

    while(temp > 0):
        rem = temp % 10
        sum = sum + rem
        temp = temp // 10
    return sum

n = int(input("Enter no: "))
print("Sum of its digits:", sum_digits(n))