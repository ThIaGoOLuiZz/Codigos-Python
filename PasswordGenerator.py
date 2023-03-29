import random

leters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
password = []
repetition = int(input("How many charaters do you need on your password?: "))
loop = 0


while(loop < repetition):
    if ((int(random.choice(numbers))) % 2) == 0:
        password.append(random.choice(leters))
        loop = loop + 1
        continue
    
    else:
        password.append(int(random.choice(numbers)))
        loop = loop + 1
        continue

print("\nThis is your new password!")
print("___________________________\n")
for x in password:
    print(x, end="")
    
print("")
print("___________________________")