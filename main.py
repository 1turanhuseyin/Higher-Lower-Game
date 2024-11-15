from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


score = 0
game_should_continue = True

account_b = random.choice(data)
data.remove(account_b)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    data.remove(account_b)

    print(f"\n" * 21)
    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B':\t").lower()
    print()

    while guess != "a" and guess != "b":
        print("You entered a wrong value! Type 'A' or 'B'\n")
        guess = input("Who has more followers? Type 'A' or 'B':\t").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
    else:
        print(f"\n" * 21)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_or_finish = input("Would you like to start a new game? Type (Y)es or (N)o\t").lower()

        while continue_or_finish != "y" and continue_or_finish != "n":
            print("You entered a wrong value! Type 'Y' or 'N'\n")
            continue_or_finish = input("Would you like to start a new game? Type (Y)es or (N)o\t").lower()

        if continue_or_finish == "y":
            score = 0
            game_should_continue = True
        else:
            print("Good bye!")
            game_should_continue = False


