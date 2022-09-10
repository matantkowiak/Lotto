from random import randint


def lotto_game():
    # User selectable numbers including errors
    your_numb = []
    while len(your_numb) < 6:
        try:
            numb_type = int(input("Type your number from 1 to 49:"))
            if numb_type in range(1,49):
                if numb_type in your_numb:
                    print("You have already chosen that number")
                else:
                    your_numb.append(numb_type)
            else:
                print("Your number is out of range")
        except ValueError:
            print("Type a number")
    sorted_your_numb = sorted(your_numb)
    print(f"Your number: {' '.join(str(el) for el in sorted_your_numb)}")
    # selected numbers by the computer
    drawn_numbers = []
    for _ in range(6):
        drown = randint(1, 49)
        if drown not in drawn_numbers:
            drawn_numbers.append(drown)
    sorted_draw_number = sorted(drawn_numbers)
    print(f"Drawn number: {' '.join(str(el) for el in sorted_draw_number)}")
    # checking how many numbers are the same
    hits = 0
    for element in your_numb:
        if element in drawn_numbers:
            hits += 1
    print(f"You hits {hits}")

lotto_game()

