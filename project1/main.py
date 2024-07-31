import random
'''
1:rock
0:paper
-1:scissor
'''
machine=random.choice([0,1,-1])
user=input("scissor paper rock:")
dict={"r":1,"p":0,"s":-1}
dict_for_game={1:"rock",0:"paper",-1:"scissor"}

you = dict[user]

print(f"computer chose:{dict_for_game[machine]}\n you choose:{dict_for_game[you]}")

if machine == user:
        print("It's a draw!!")
else:
        if (machine == 1 and user == 0) or (machine == 0 and user == -1) or (machine == -1 and user == 1):
            print("You win!!")
        else:
            print("You lose!!")
        
