import random

COLORS = ['R', 'G', 'B', 'Y', "W", 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def guess_code():
    while True:
        guess = input('Guess: ').upper().split()

        if len(guess) != CODE_LENGTH:
            print(f'You must guess {CODE_LENGTH} colors.')
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f'Invalid color: {color}. Try again')
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {

    }
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        color_counts[color] = color_counts.get(color, 0) + 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f'Welcome to mastermind, you have {TRIES} to guess the code...')
    print('The valid colors are ', COLORS)
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f'You guessed the code in {attempts} tries!')
            break

        print(f'correct position: {correct_pos} | incorrect position: {incorrect_pos}')
    else:
        print("You ran out of tries, the code was: ",code)

if __name__ == '__main__':
    game()