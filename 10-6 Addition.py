print("Enter 'q' if you want to quit, else continue using the program.\n")

while True:

    try:
        userInput = input("Please enter first number: ")

        if userInput == 'q':
            break

        userInput = int(userInput)

        userInput2 = input("Enter another number: ")

        if userInput2 == 'q':
            break

        userInput2 = int(userInput2)

    except ValueError:
        print("A number was needed")

    else:
        sum = userInput + userInput2
        print("The sum between " + str(userInput) + " and " + str(userInput2) + " is " + str(sum) + ".")


