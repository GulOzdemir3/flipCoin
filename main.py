import random


def flipCoin():
    random_coin = random.randint(1, 2)
    if random_coin == 1:
        side = "heads"
    else:
        side = "tails"
    return side


choice = str(input("Heads or tails?: ").capitalize())
result = flipCoin().capitalize()

if result == choice:
    print("You won!")
elif result != choice:
    print("You lost!")

print("The coin landed on {}".format(result))