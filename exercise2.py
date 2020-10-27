i = 1
while i <= 10:
    print(i)
    i+=1


x = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in x:
    if (i>150):
        break
    if i%5 == 0:
        print(i)

print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")


print("second no. pattern")
x = 7
for y in range(1,7):
    for z in range(1,y+1):
        print(z, end=' ')
    print('')

sum1 = 0
n = int(input("Please enter number "))
for i in range(1, n + 1, 1):
    sum1 += i
print("\n")
print("Sum is: ", sum1)


x = 2
for i in range(1,11):
    i*=2
    print( x '*'i = "i" )
                         # 2*1=2

x = [10, 20, 30, 40, 50]


for i in range(-10,6):
    print(i)

for i in range(5):
    print(i)
else:
    print('done')


x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in x[1::2]:
    print(i, end=" ")


#I have 1000 dollars so I can buy 3 football for 450.00 dollars.
p = 1000
r = 54
t = 85

#print("i have {} dollars so i can buy {} footballs for {} dollars".format(p,r,t))
print(f"i have {p} dollars so i can buy {r} footballs for {t} dollars")

