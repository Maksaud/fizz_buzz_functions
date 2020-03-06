number = ""

while number != "penpinapplespen":
    number = int(input("Enter a number: "))
    temp_num = number
    number = 0
    while number <= (temp_num):
        number += 1
        if number % 3 == 0 and number % 5 == 0:
            print('boringbuzz', number)
        elif number % 3 == 0:
            print('boring', number)
        elif number % 5 == 0:
            print('buzz', number)
        else:
            print(number)