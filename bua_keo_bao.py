import random


choices = ['bua', 'keo', 'bao']

def check_result(your_choice, bot_choice):
    if (your_choice == 'bua' and bot_choice == 'keo') or (your_choice == 'bao' and bot_choice == 'bua') or (your_choice == 'keo' and bot_choice == 'bao'):
        print(f'Bot choice: {bot_choice}. You win!!!')
        return 1
    elif your_choice == bot_choice:
        print(f'Bot choice: {bot_choice}. Draw!!!')
        return 0
    else:
        print(f'Bot choice: {bot_choice}. You lose!')
        return -1

def main():
    score = 0
    count = 0
    while True:
        your_choice = input('Hay chon (bua, keo, bao). Break the game "r": ').lower()
        if your_choice == 'r':
            print(f'You play {count} games reaches {score} scores')
            break
        if your_choice not in choices:
            print('Your choice is invalid. Please try again!')
        else:
            bot_choice = choices[random.randint(0, 2)]
            score += check_result(your_choice, bot_choice)
            count +=1

main()
