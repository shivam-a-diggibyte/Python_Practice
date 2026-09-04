try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print(f"You entered {number}.")