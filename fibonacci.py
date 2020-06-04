n = int(input("How many terms? "))

a, b = 0, 1
count = 0

if n <= 0:
   print("Please enter a positive integer")

else:
   print("Fibonacci sequence:")
   while count < n:
       print(a)
       c = a+b
       a = b
       b= c
       count+=1
