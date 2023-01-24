num = input("enter a number: ")

n = str(len(num))

#print(int(n) + int(n+n) + int(n+n+n))

sum = 0
for i in range(1, 4):
    sum = sum + int(n * i)

print(sum)

