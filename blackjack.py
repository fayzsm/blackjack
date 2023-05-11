
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare(total, total_comp):
    if total == 21:
        return "You win!"
    elif total_comp == 21:
        return "You lost!"
    elif total >21:
        return "You lost!"
    elif total_comp >21:
        return "You win!"
    elif total > total_comp:
        return "You win!"
    elif total < total_comp:
        return "You lost!"
    else:
        return "Draw"
    
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def play():
    play=False
    flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if flag == 'y':
        play = True

    player_cards= [random.choice(cards),random.choice(cards)]
    computer_cards=[random.choice(cards)]

    while play:
        total = calculate_score(player_cards)
        print (f"Your cards: {player_cards}, current score: {total}")
        print(f"Computer's first card: {computer_cards}")
        total_comp = calculate_score(computer_cards)
        while total_comp < 17:
            computer_cards.append(random.choice(cards))
            total_comp = calculate_score(computer_cards)

        if total == 21 or total_comp == 21 or total > 21:
            play =  False
        else: 
            if total != 21:
                getcard=input("Type 'y' to get another card, type 'n' to pass: " )
                if getcard == 'y':
                    player_cards.append(random.choice(cards))
                    total = calculate_score(player_cards)
                else:
                    play = False
        
        

    print(f"Your final hand: {player_cards}, final score: {total}")
    print(f"Computer's final hand: {computer_cards}, final score: {total_comp}")
    print(compare(total, total_comp))

flag = input("Do you want to play again? Type 'y' or 'n': ")
while flag != 'y' and flag != 'n':
    flag = input("Please type 'y' or 'n': ")
if flag == 'y':
    play()

play()     

