import random
from IPython.display import clear_output

class Deck:                                             #So what are the things we need to know about the object, "DECK"?  Well that would be the suit and the number.
    def __init__(self):
        self.deck_of_cards = []                         #This will be the deck
        card_types = ["spades", "hearts", "diamonds", "clubs"]
        for type in card_types:
            for i in range(2, 15):                      #nested for loop to add 13 cards per "type" 2-14(ace)
                self.deck_of_cards.append((type, i))    #Now let's fill up the deck with some tuples

    def shuffle(self):
        random.shuffle(self.deck_of_cards)      #built in shuffling function

    def add_card(self):
        return self.deck_of_cards.pop(0)        #The ability to remove one card at a time from the deck, to be dealt(popped) to the player or the computer


class Human:                                    # Ok, now what are the things we need to know about the human?  This ended up being used for both players.
    def __init__(self, name, cards, score):     # These attributes are going to apply to the player and the computer but I don't feel like renaming it
        self.name = name
        self.cards = cards
        self.score = score
        self.bet = 0               # A little something extra because I must be a masochist.  Also it's not included in the other attributes because the dealer will never be betting and I made dealer and player subclasses of Human.

    def print_info(self):          # Prints the current game status
        print("{} got cards : {}. Total score is {}".format(self.name,self.cards, self.score))   #Learned a little trick called .format

    def sum(self):                 # Method to calculate the sum of the cards held by the player/dealer. Returns a number
        sum = 0
        for card in self.cards:    #looping through the tuples in self.cards...
            sum = sum + card[1]    #and adding the values from the index 1 position
        return sum

    def check_sum(self):           # Method to see if you BUSTED.  Does the same as above but returns a boolean
        sum = 0
        for card in self.cards:
            sum = sum + card[1]
        if sum > 21:
            return True
        else:
            return False


class Player(Human):                           # Bringing all those Human attributes down into this Player class
    def __init__(self, name, cards, score):
        super().__init__(name, cards, score)  

    def list_cards(self):                      # Method to print all the cards held by the player
        for card in self.cards:
            print(card[0], card[1])


class Dealer(Human):                           # Same as above
    def __init__(self,name, cards, score):
        super().__init__(name, cards, score)  

    def list_cards(self):                      # Same as above
        for i in range(len(self.cards) - 1):   #This makes it so it doesn't show the last card
            card = self.cards[i]               
            print(card[0], card[1])            
        print("hidden card")                   # The last card of the dealer is hidden

    def show_cards(self):                      # Method to reveal and print all the cards held by the dealer
        for i in range(len(self.cards)):
            card = self.cards[i]
            print(card[0], card[1])


def main():
    def start():
        while True:
            player1.cards = []            #create an empty list that will hold the cards of the freshly initialized player(initialized at bottom)
            dealer1.cards = []            #same as above
            clear_output()
            for i in range(2):
                player1.cards.append(game.add_card())  # add 2 cards for the player
                dealer1.cards.append(game.add_card())  # add 2 cards for the dealer
            print("{}'s cards:".format(player1.name))  #
            player1.list_cards()                       
            if player1.check_sum():                    #run the check_sum method on player1 to see if it's TRUE, since in this game you could technically start with 2 14's
                print("You Lose")
                break

            while dealer1.sum() < 17:                  #Dealer always hits under 17
                dealer1.cards.append(game.add_card())  #add card for dealer if needed
            print("{}'s cards:".format(dealer1.name))
            dealer1.list_cards()   
            gaming()                                   #let's get gaming

    def gaming():
        while True:
            answer = input ("If you want to hit, enter: hit.  If you want to stand, enter: stand. ") # ask the player what they want to do after receiving their cards
            if answer.lower() == "hit":               #hit mechanics
                clear_output()
                player1.cards.append(game.add_card()) #adding card for player if needed
                if player1.check_sum():               #checking if the sum of player one's cards is more than 21                    
                    print("{}'s cards:".format(player1.name))
                    player1.list_cards()
                    print("{}'s cards:".format(dealer1.name))
                    dealer1.list_cards()    
                    print ("You lose!")
                    clear_output()
                    break
                print("{}'s cards:".format(player1.name))
                player1.list_cards()
                print("{}'s cards:".format(dealer1.name))
                dealer1.list_cards()    

            elif answer.lower() == "stand":                      #stand mechanics
                clear_output()
                if dealer1.check_sum():                          #Seeing if the dealer busted
                    print("{}'s cards:".format(player1.name))
                    player1.list_cards()
                    print("{}'s cards:".format(dealer1.name))
                    dealer1.show_cards()
                    print ("You win! ")
                    clear_output()
                    break
                else:
                    dealer1.show_cards()                             #Everyone's got all their cards. Time to compare 
                    if player1.sum() > dealer1.sum():                #win 
                        print("{}'s cards:".format(player1.name))
                        player1.list_cards()
                        print("{}'s cards:".format(dealer1.name))
                        dealer1.show_cards()
                        print("You win! ")

                    elif dealer1.sum() > player1.sum():              #lose       
                        print("{}'s cards:".format(player1.name))
                        player1.list_cards()
                        print("{}'s cards:".format(dealer1.name))
                        dealer1.show_cards()
                        print("You lose! ")
 
                    else:                                            #draw
                        print("{}'s cards:".format(player1.name))
                        player1.list_cards()
                        print("{}'s cards:".format(dealer1.name))
                        dealer1.show_cards()
                        print("It's a draw")
                    break
            else:
                print("Wrong input")

    
    player1 = Player(input("Enter your name: "), [], 0)             #initializing player with a name, an empty list of cards, and a score
    clear_output()
    dealer1 = Dealer("Dealer",[],0)                                 #initialize Dealer with the same
    clear_output()
    game = Deck()                                       # Creating a new instance of the deck class called 'game'
    game.shuffle()                                      # start by shuffling the cards, which is a method of the deck class
    while True:
        answer = input("Are you ready to play? y/n")    #Now that everything is initialized...
        clear_output()
        if answer.lower() == "y":
            start()
        elif answer.lower() == "n":
            break
        else:
            print("I think your finger slipped")

main()

#I know the output isn't beautiful, but it works.  I don't really have a good grasp of clear_output.  And sorry I'm weirdly late turning everything in. For whatever reason, my brain thought it would be a good idea to do a bunch of work and then turn it in.  I guess it's because I'm under a lot of stress with this class and it's making me act weird and panicky.  Anyway, enjoy!