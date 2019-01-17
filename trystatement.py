user = input("enter an integer: ")

try:
    number = int(user)
    print("You entered the number ", number)

except ValueError:
    print("intergers only\n")
