number=int(input("Enter the Range Number:"))
a=0
b=1
for number in range(0, number):
   if (number <= 1):
      Next = number
   else:
      Next = a + b
      a = b
      b = Next
   print(Next, end=", ")