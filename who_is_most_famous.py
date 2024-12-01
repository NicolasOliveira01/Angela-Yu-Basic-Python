from art import logo, vs
from game_data import data
from random import randint

#print(logo)



def most_famous():
    is_end_game = False
    score = 0
    index_a = 0
    index_b = 0
    a = {}
    b = {}
    while not is_end_game:
        if score == 0:
            index_a = randint(0, len(data)-1)
            a = data[index_a]
            data.pop(index_a)
            index_b = randint(0, len(data)-1)
            b = data[index_b]
            data.pop(index_b)
            print(a)
            print(b)
        else:
            a = b
            print(a)
            index_b = randint(0, len(data)-1)
            b = data[index_b]
            data.pop(index_b)
            print(b)

        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")

        bigger = input("Who has more followers? Type 'a' or 'b': ")
        a_follower = a['follower_count']
        b_follower = b['follower_count']
        if bigger == 'a':
            if b_follower > a_follower:
                is_end_game = True
                print(f"Sorry, that's wrong. Final score {score}")
                return
        elif bigger == 'b':
            if a_follower > b_follower:
                is_end_game = True
                print(f"Sorry, that's wrong. Final score {score}")
                return
        score+=1
        print("\n" * 10)
        print(f"Your Right! Current score: {score}")

most_famous()
