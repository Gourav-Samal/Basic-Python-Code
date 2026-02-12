n = int(input("Enter the number:"))
t = 0
for i in range(1, n+1):
    if n % i == 0:
        t = t + 1
if t == 2:
    print("n is Prime number")
else:
    print("n is not prime number")