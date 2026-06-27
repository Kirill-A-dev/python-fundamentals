number = int(input("Guess the number: "))
secret = 7
while number != secret :
    if number > secret:
        print("Too big!")

    else :
        print("Too small!")

    number = int(input("Guess the number: "))

print("You win!")
