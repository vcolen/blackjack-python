import random
from art import logo


def pick_card():
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_deck)
    return card


def check_score(cards):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

    if sum(cards) > 21:
        return 0


def show_results(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if player_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def blackjack():
    player_cards = [pick_card(), pick_card()]
    computer_cards = [pick_card(), pick_card()]
    print(f"Your cards are {player_cards}, a total of {sum(player_cards)}")
    player_choice = input(
        f"Computer's first card is {computer_cards[0]}. Do you want to take another card? (y/n)?\n>> ")

    while player_choice == "y":
        player_cards.append(pick_card())
        player_choice = input(
            f"Your cards are {player_cards}, a total of {sum(player_cards)}. Do you want to take another card? ("
            f"y/n)\n>> ")

    while sum(computer_cards) < 17:
        computer_cards.append(pick_card())

    player_final_score = sum(player_cards)
    computer_final_score = sum(computer_cards)
    print(f"Your score: {player_final_score}")
    print(f"Computer's score: {computer_final_score}")
    print(show_results(player_final_score, computer_final_score))
    return


while input("Do you want to play a game of black jack?(y/n)\n>> ") == "y":
    print(logo)
    blackjack()
