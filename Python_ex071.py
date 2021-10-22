print("Практикум 1:")

print("Max")
print("Sergeevic")
print("Tukmachev")

print("\nПрактикум 2:")
a = 12
if a < 10:
    print("a smaller 10")
elif a >= 10:
    print("a equal or bigger 10")

print("\nПрактикум 3:")
n = int(input("Enter integer number: "))
if n <= 10:
    print("small")
elif n > 10 and n <= 25:
    print("middle")
else:
    print("big")

print("\nПрактикум 4:")
n1, n2 = int(input()), int(input())
print(n1 % n2)

print("\nПрактикум 5:")
p1, p2 = int(input()), int(input())
print(p1 / p2)

print("\nПрактикум 6:")
age = int(input("Enter AGE: "))
if age <= 5:
    print("baby")
elif age > 5 and age <= 12:
    print("child")
elif age > 12 and age <= 19:
    print("teenager")
elif age > 19 and age <= 45:
    print("adult")
else:
    print("old")
