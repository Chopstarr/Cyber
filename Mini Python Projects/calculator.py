def calculator():
    while True:
        calc = input('Enter calculation: ')
        evaluation = eval(calc)
        print(calc)
        print(evaluation)

        ask = input("That was fun! Would you like to perform another calculation? Y or N: ").lower()

        if ask == 'y':
            continue
        elif ask == 'n':
            print("Aw, well that's too bad")
            break
        else:
            for i in range(5):
                if i == 0:
                    response = input('Please type y or n: ').lower()
                elif i == 1:
                    response = input('Ok, let’s try again — type the letter Y or the letter N: ').lower()
                elif i == 2:
                    response = input('Yeah, you’re doing this on purpose, aren’t you? ').lower()
                elif i == 3:
                    response = input('I’m not going to tell you again — Y or N: ').lower()
                else:
                    print("Alright, that's enough fun for you, go outside.")
                    return

                if response == 'y':
                    break  # restart calculator loop
                elif response == 'n':
                    print("Thanks for testing!")
                    return

print(calculator())
