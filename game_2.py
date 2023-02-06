import random

variants = ['камень', 'бумага', 'ножницы']
count_you_hand = 0
count_computer_hand = 0
draw = 0
while True:
    your_hand = input('Сделайте выбор предмета: ')
    computer_hand = random.choice(variants) # такой рандом выбирает случайный элемент из списка

    print('Вы выбрали:', your_hand)
    print('Компьютер выбрал:', computer_hand)

    if your_hand not in variants:
        print('неверная команда')
        exit(0)
        

    if your_hand == computer_hand:
        print("Ничья")
        draw += 1

    if your_hand == 'камень':
        if computer_hand == 'бумага':
            print('Вы проиграли')
            count_computer_hand += 1
        else:
            print('Вы победили')
            count_you_hand += 1
    if your_hand == 'бумага':
        if computer_hand == 'ножницы':
            print('Вы проиграли')
            count_computer_hand += 1
        else:
            print('Вы выйграли')
            count_you_hand += 1
    if your_hand == 'ножницы':
        if computer_hand == 'камень':
            print('Вы прогирали')
            count_computer_hand += 1
        else:
            print('Вы выйграли')
            count_you_hand += 1


    print(f'Общий счет: \nВы:{count_you_hand}, Компьютер:{count_computer_hand}, Ничья: {draw}')