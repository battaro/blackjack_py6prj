#importing libraries that i will use in this code
import random
import os
import platform
from art import logo

#this function can clear the console
def clear():
    """Clear the console."""
    #cls for windows and clear for other operating systems
    if platform.system() == "Windows": #is this operating system windows ?
        os.system("cls") 
    else:
        os.system("clear")

#this function will return a random choice from the list down below
def pick_random_cards():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #list have all cards on the game
    card = random.choice(cards)
    return card

#this function will return the score of the deck either player or computer's deck
def calculate_score(deck):
    """return the score of the deck you want"""
    score = sum(deck) #sum function can calculate return the sum of all numbers in any list you want

    #cheking the blackjack
    if sum(deck) == 21 and len(deck) == 2:
        return 0
        
    #checking the ace
    if 11 in deck and sum(deck) > 21:
        index_of_11 = deck.index(11)
        deck[index_of_11] = 1 #converting to number one
        score = sum(deck)
    return score

#this function will compare the player and computer score and return the final result of the game
def compare(p_score, c_score):
    """ compare the scores """
    if p_score > 21 and c_score > 21:
        return "You went over. You lose 😤"
    
    if c_score == p_score:
        return "Draw 🙃"
    
    elif c_score == 0: #blackjack
        return "Lose, opponent has Blackjack 😱"
        
    elif p_score == 0: #blackjack
        return "Win with a Blackjack 😎"
    
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    
    elif p_score > 21:
        return "You went over. You lose 😭"

    elif p_score > c_score:
        return "You win 😃"
        
    elif c_score > p_score:
        return "You lose 😤"


def the_game():
    """  the game :| """
    print(logo) #logo from art.py 

    #creating the variables that i will use 
    GameEnded = False
    player_deck = [pick_random_cards(), pick_random_cards()]
    computer_deck = [pick_random_cards(), pick_random_cards()]
    
    
    while GameEnded != True:
        player_score = calculate_score(player_deck)
        computer_score = calculate_score(computer_deck)

        print(f"    Your cards: {player_deck}, current score: {player_score}")
        print(f"    Computer's first card: {computer_deck[0]}")
        
        if computer_score == 0 or player_score == 0 or player_score > 21:
            GameEnded = True
        else:
            another_cardq = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_cardq == "y":
                player_deck.append(pick_random_cards()) #adding another card for player's deck
            else:
                GameEnded = True

    #if the computer score less than 17 and not equal to zero then append random cards until go 17 and uper 
    while computer_score < 17 and computer_score != 0 :
        computer_deck.append(pick_random_cards())
        computer_score = calculate_score(computer_deck)
                        
    print(f"    Your final hand: {player_deck}, final score: {[player_score]}")
    print(f"    Computer's final hand: {computer_deck}, final score: {computer_score}")
        
    result = compare(player_score,computer_score)
    print(result)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  the_game()
else: #i didn't knew that i can use else with while 
    print("Bye Bye thx for playing <3")
