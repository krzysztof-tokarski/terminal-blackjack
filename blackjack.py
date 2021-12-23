import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        all_cards = []
        self.all_cards = all_cards
        for suit in suits:
            for rank in ranks:
                all_cards.append(Card(suit,rank))    
        
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def remove_one(self):
        return self.all_cards.pop(0)
    

game_on = True

player_bank = 0

while game_on:
    
    player_turn = True
    dealer_turn = True
    
    while player_bank == 0:
        player_deposit = input("How much are you willing to deposit? \n")
        try:
            int(player_deposit)
        except:
            print("Sorry, I do not understand, please try again.\n")
            continue   
        if int(player_deposit) > 0:
            player_bank = int(player_deposit)
        else:
            print("You need to wage something to play here.\n")
            continue
        
    player_bet = 0
            
    while not 0 < int(player_bet) <= player_bank:
        test = input(f"How much are you willing to bet this round? Your current deposit equals {player_bank} $. \n")
        try:
            int(test)
        except:
            print("Sorry, I do not understand, please try again.\n")
            continue   
        if 0 < int(test) <= player_bank:
            player_bet = int(test)
        else:
            print("You have to wage SOMETHING, and your wager may not exceed your current deposit.\n")
            continue
            
    deck = Deck()
        
    deck.shuffle()

    dealer_value = 0
        
    for card in deck.all_cards[0:2]:
        dealer_value += card.value
            
    if dealer_value == 22:
        dealer_value = 12

    player_value = 0   
        
    for card in deck.all_cards[2:4]:
        player_value += card.value
            
    if player_value == 22:
        player_value = 12
        print("Two Aces already... One's value shall equal 11, the other's shall equal 1.")
                
    print(f"I get {deck.all_cards[0]}, the other shall remain face down.\n")
        
    print(f"You get {deck.all_cards[2]} and {deck.all_cards[3]}.\n")
        
    deck.all_cards = deck.all_cards[4:]
    

    
    while player_turn == True:

        print(f"Current total value of your cards equals {player_value}.\n")
        
        if player_value > 21:
            print("You exceeded 21, I win this round.\n")
            player_bank -= player_bet 
            player_turn = False
            dealer_turn = False
            break
            
        if player_value == 21:
            print("You have got exact 21, looks like I lose this round...\n")
            player_bank += player_bet
            player_turn = False
            dealer_turn = False
            break

        choice = None
            
        while choice not in ["Y","y","N","n"]:
            choice = input("Do you hit or do you stand[Y/N]?\n ")
            if choice not in ["Y","y","N","n"]:
                print("Sorry, I do not understand, please try again.\n")
            else:
                continue
            
        if choice in ["Y","y"]:
            next_card = deck.remove_one()
                
            print(f"You get {next_card}.\n")
                
            if next_card.value < 11:
                player_value += next_card.value
            else:
                check = player_value + next_card.value
                if 21 < check <= 31:
                    player_value += next_card.value - 10
                    print ("Looks like while pulling that Ace you have exceeded 21, so it shall count as 1 instead of 11.\n")
                else:
                    player_value += next_card.value
        if choice in ["N","n"]:
            player_turn = False
            print("Looks it's my turn now.\n")
            break
            

    
    while dealer_turn == True:
        
        print(f"Current total value of my cards equals {dealer_value}.")
        
        if dealer_value > 21:
            
            print("I have exceeded 21, you win this round.\n")
            player_bank += player_bet
            player_turn = False
            dealer_turn = False
            break
        
        if dealer_value > player_value:
            
            print("Looks like total value of my cards exceeded total value of your cards. I win this round.\n")
            player_bank -= player_bet
            player_turn = False
            dealer_turn = False
            break
        
        while not dealer_value > player_value:
            
            print("Looks like I have to pull another one.")
            
            next_card = deck.remove_one()
                
            print(f"I get {next_card}.\n")

            if next_card.value < 11:
                dealer_value += next_card.value
            else:
                check = dealer_value + next_card.value;
                if 21 < check <= 31:
                    dealer_value += next_card.value - 10
                    print ("Looks like while pulling that Ace I have exceeded 21, so it shall count as 1 instead of 11.\n")
                else:
                    dealer_value += next_card.value
    
    
    final = None
    
    while final not in ["Y","y","N","n"]:
        final = input("Do we play another round [Y/N]?\n")
        if final in ["N","n"]:
            game_on = False
            break
        if final in ["Y","y"]:
            continue
        else:
            print("Sorry, I do not understand, please try again.\n")
