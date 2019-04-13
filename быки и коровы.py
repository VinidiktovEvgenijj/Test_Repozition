import random


def all_answers():
    ans = []
    for i in range(10000):
        x = str(i).zfill(4)
        if len(set(map(int, x))) == 4:
            ans.append(list(map(int, x)))
    return ans


def one_answer(ans):
    x = random.choice(ans)
    return x


def input_number():
    while True:
        y = input('Введите 4 неповторяющиеся цифры')
        if len(y) != 4 or not y.isdigit():
            print('Вы ввели что то не то!\n Попробуйтеснова')
            continue
        y = list(map(int, y))
        if len(set(y)) == 4:
            break
    return y


def check(nums, tru_nums):
    bulls = 0
    cows = 0
    for i, num in enumerate(nums):
        if num in tru_nums:
            if nums[i] == tru_nums[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def extra_answer(ans, enemy_try, bull, cows):

    for num in ans[:]:
        bull_1 = check(num, enemy_try)
        cows_1 = check(num, enemy_try)
        if bull_1 != bull or cows_1 != cows:
            ans.remove(num)
    return ans


print('Игра быки и коровы')

variant = all_answers()
player = input_number()
computer = one_answer(variant)

while True:
    print('=' * 15, 'ход игрока', '=' * 15)
    number = player
    bulls, cows = check(number, computer)
    print('быки', bulls, 'коровы', cows)
    if bulls == 4:
        print('победил игрок')
        print("компьютер загадал число", variant)
        break
