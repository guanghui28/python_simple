import random

random_number = random.randint(1, 20)

def choose_range():
    while True:
        top_of_range = input('Type top range number: ')
        if top_of_range.isdigit():
            top_of_range = int(top_of_range)
            return top_of_range
        print('Your choose is invalid.Your must input an integer number')

def main():
    top_of_range = choose_range()
    random_number = random.randint(1, top_of_range)
    count = 0
    while True:
        your_answer = input(f'Please guess from (1,{top_of_range}) !. Press "r" to quit ')
        if your_answer == 'r':
            break
        
        if your_answer.isdigit():
            your_answer = int(your_answer)
            if your_answer == random_number:
                print(f"Your win after guessed {count} times!")
                break
            elif your_answer < random_number:
                print('Your answer is too lower than random number. Choose again!')
            else:
                print('Your answer is higher than random number. Choose again!')
        else:
            print('Your answer is not valid. Please input an integer number')
        count+=1

main()
