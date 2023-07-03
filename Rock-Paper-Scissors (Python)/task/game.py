import random


def rps_game():
    user_name = input('Enter your name: ')
    print(f'Hello, {user_name}')
    rating_dict = {}
    try:
        with open('rating.txt', 'r') as rating_r:
            rating_rl = rating_r.readlines()
            for line in rating_rl:
                line_list = line.strip().split(' ')
                rating_dict[line_list[0]] = int(line_list[1])
    except:
        pass
    if not user_name in rating_dict:
        rating_dict[user_name] = 0
    rps_list = input().split(',')
    if len(rps_list) <= 1:
        rps_list = ['rock', 'paper', 'scissors']
    print('Okay, let\'s start')
    while True:
        user_input = input()
        choice = random.choice(rps_list)
        if user_input == '!rating':
            print(f'Your rating: {rating_dict[user_name]}')
        elif user_input == '!exit' or user_input == 'Bye!':
            with open('rating.txt', 'w') as rating_w:
                for user in rating_dict:
                    print(f'{user} {rating_dict[user]}\n', file=rating_w)
            break
        elif user_input == choice:
            rating_dict[user_name] += 50
            print(f'There is a draw {choice}')
        elif user_input not in rps_list:
            print('Invalid input')
        else:
            i, j, k = rps_list.index(user_input), rps_list.index(choice), int(len(rps_list) / 2)
            diff = max(i, j) - min(i, j)
            winner = j
            if diff <= k:
                if i > j:
                    winner = i
            else:
                if i < j:
                    winner = i
            if winner == i:
                rating_dict[user_name] += 100
                print(f'Well done. The computer chose {choice} and failed;')
            else:
                print(f'Sorry, but the computer chose {choice}')




rps_game()
