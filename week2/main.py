
i = 10
j = 6
k: int = int(i / j)
print(k)
f = 10.5

i = i + 10
i += 7
i -= 3
i += j

i *= 2.5

j /=3

i += j

print(i)
print(j)

b:bool = True

b = (i > 9)

s:str = "Bryan"

print(s)

sf = f"Hello {s}"

if i < 0:
    print("i is negative")

if i >= 0:
    print("i is positive")

if i >= 0 and i < 10:
    print("i is between 0 and 10")

if i == 10 or i == 20:
    print("i is divisible by 10")

if i == 10:
    print(i)
else:
    print("i is not 10")

if i == 10:
    print("Whatever")
elif (i ==11):
    print("Whatever")
elif (i ==12):
    print("Whatever")

def say_hello(name:str) -> str:
    print(f"Hello {name}")
    return name

name = input("Enter your name:")
say_hello(name)

print("Hello")