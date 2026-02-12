n = int(input("Enter the number: "))
x = int(str(n)[::-1])
if n == x:
    print("Pallindome Number")
else:
    print("Not pallindrome Number")
    