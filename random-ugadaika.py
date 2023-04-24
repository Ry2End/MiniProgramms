from random import *  #random lib
import time           #for sleep()

prog_number = randint(1,100)

def is_valid(input_number):
    return input_number.isdigit() and 1 <=int(input_number) <= 100

def lets_play():
    count = 0
    while True:
        user_number = input('''Попробуй угадать число от 1 до 100 (включительно)
    q - выход \n''')
        if user_number == 'q':
            print(f'Сдался! Фу!\nЗагаданное число: {prog_number}\n')
            break
                        
        if not is_valid(user_number):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if int(user_number) < int(prog_number):
            print('Ваше число МЕНЬШЕ загаданного')
            count += 1
        elif int(user_number) > int(prog_number):
            print('Ваше число БОЛЬШЕ загаданного')
            count += 1
        else:
            print('ТЫ ПОБЕДИЛ! ГЦ!')
    return count
        
def check_replay(answer):
    if answer.lower() == 'y':
        print(f'Твоё число поыток угадать было: {lets_play()}')
        check_replay(input('Спасибо, что играли в числовую угадайку. Может, сыграем ещё один раз?\n Y - Да, N - Нет\n'))
    elif answer.lower() == 'n':
        print('Жаль.', end = ' ')   
        print('Надеюсь, ты вернёшься(нет)')        
    else:
        check_replay(input('Я не понял ответа >< \nМожет, сыграем ещё один раз?\n Y - Да, N - Нет\n'))

print("Добро пожаловать в числовую угадайку\n")
time.sleep(1)
print(f'Твоё число попыток угадать было: {lets_play()}')
time.sleep(1)
print()
check_replay(input('Спасибо, что играли в числовую угадайку. Может, сыграем ещё один раз?\n Y - Да, N - Нет\n'))




