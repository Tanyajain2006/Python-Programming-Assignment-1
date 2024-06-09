n = int(input("Enter no: "))

temp = n
sum = 0

while(temp > 0):
    rem = temp % 10
    sum = sum + rem
    temp = temp // 10

print("Sum of its digits:", sum)