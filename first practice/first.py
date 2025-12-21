
#1
n = int(input("Enter the number of integers: "))
total = 0

for i in range(n):
    num = int(input("Enter number: "))
    total += num

print("Sum:", total)


#----------------------------------------------------------------------------------

#2
x = float(input("Enter x: "))
y = float(input("Enter y: "))

radius = 5
distance_squared = x**2 + y**2

if distance_squared <= radius**2:
    print("Result: inside")
else:
    print("Result: outside")

#----------------------------------------------------------------------------------

a = int(input("Enter the first number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

print("Result:", max_val)

