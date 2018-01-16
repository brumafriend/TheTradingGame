import sys
import time
import random

goldowned = 0
balance = 10000
gold = 1000
bitcoin = 10000
bitcoinowned = 0
possession = 0
def run():
    global gold
    global possession
    global goldowned
    global balance
    global bitcoin
    global bitcoinowned
    while True:
        command = input("Type a command: ")
        if command == "!help":
            print("")
            print("Commands:")
            print("!help - see commands.")
            print("!invest - Invest money into a currency.")
            print("!value - see the current value of all units.")
            print("!owned - see how much you own.")
            print("!balance - see how much money you have.")
            print("!progress - finalise your investments and hope for the best.")
            print("!sell - sell a number of units for money.")
            print('!save - save the game progress')
            print("")

        elif command == '!save':
            with open('savefile.txt','w') as f:
                f.write('Gold: '+str(goldowned)+' ')
                f.write('Bitcoin: '+str(bitcoinowned))
                f.close()
                print('Game Saved')
                leave = input('Would you like to quit? (1 for yes, 2 for no)')
                if leave == '1':
                    print('Quitting game...')
                    time.sleep(3)
                    quit()
                elif leave == '2':
                    print('Continuing game...')
                    time.sleep(2)
                    run()
            
        elif command == "!invest":
            print("INVEST:")
            print("Gold - 1")
            print("Bitcoin - 2")
            print("")
            time.sleep(0.2)
            print("Please enter the number which corresponds to what you would like to buy:")
            request = input("")
            if request == "1":
                print("1 unit of solid Gold is worth $%d." % gold)
                time.sleep(0.5)
                print("How many units would you like to buy?")
                try:
                    buy = int(input(""))
                except ValueError:
                    print("You can't buy a fraction of a unit.")
                    run()
                cost = buy * gold
                if cost > balance:
                    print("You do not have enough money to make this purchase!")
                else:
                    print("You have spent $%d..." % cost)
                    time.sleep(0.2)
                    print("Buying %d units..." % buy)
                    time.sleep(1)
                    goldowned += buy
                    balance -= cost
                    print("You now own a total of %d units of Gold." % goldowned)
                    time.sleep(0.2)
                    print("You now have $%d." % balance)
            elif request == "2":
                print("The current cryptocurrency you can invest in is Bitcoin")
                print("1 Bitcoin is worth $%d." % bitcoin)
                time.sleep(0.5)
                print("How much would you like to invest in Bitcoin?")
                try:
                    amount = int(input("$"))
                except ValueError:
                    print("Please enter a number.")
                    run()
                multiple = (1/bitcoin)
                bitcoins = amount * multiple
                if amount > balance:
                    print("You do not have enough money to make this purchase!")
                else:
                    print("That is worth: "+str(bitcoins)+" Bitcoins")
                    time.sleep(0.5)
                    print("You have spent $%d..." % amount)
                    time.sleep(1)
                    bitcoinowned += bitcoins
                    balance -= amount
                    print("You now own a total of "+str(bitcoinowned)+" Bitcoins")
                    time.sleep(0.2)
                    print("You now have $%d." % balance)
            else:
                print("No number matches your request!")
                continue

        elif command == "!owned":
            print("YOUR POSSESSIONS:")
            print("Gold = %d units." % goldowned)
            print("Cryptocurrency = "+str(bitcoinowned)+" Bitcoins")
            print("")

        elif command == "!balance":
            print("BANK ACCOUNT:")
            print("You have $%d." % balance)

        elif command == "!progress":
            print("Are you sure you would like to go forward? You will not be able to go back.")
            time.sleep(0.2)
            print("(If you progress, a week will pass and the values of units may change)")
            time.sleep(0.1)
            print("1=yes/2=no")
            progress = input("")
            if progress == "1":
                print("Finalising investments...")
                time.sleep(0.3)
                print("A week is passing...")
                time.sleep(0.5)
                if random.randint(0,100) < (1000):
                    gold += (random.randint(-250,250))
                    print("Gold is now worth $%d." % gold)
                    bitcoin += (random.randint(-250,250))
                    print("Bitcoin is now worth $"+str(bitcoin)+".")
            else:
                continue
            
        elif command == "!value":
            print("VALUES:")
            print("Gold = $%d/unit" % gold)
            print("Bitcoin = $"+str(bitcoin)+"/coin")
            print("")

        #IN PROGRESS \/
        elif command == "!sell":
            print("SELL:")
            print("Sell Gold - 1")
            print("Sell Bitcoin - 2")
            print("")
            print("Please enter the number which corresponds to what you would like to sell.")
            sell = input("")
            if sell == "1":
                print("You have chosen to sell your gold.")
                print("You currently have: %d units of gold" % goldowned)
                time.sleep(1)
                print("How many units of gold would you like to sell?")
                goldchosen = int(input(""))
                if goldchosen > goldowned:
                    print("You can't sell more gold than you have.")
                elif goldchosen < 0:
                    print("You can't sell negative units.")
                else:
                    time.sleep(0.1)
                    gmoney = goldchosen * gold
                    print("You have sold gold for $%d." % gmoney)
                    balance = balance + gmoney
                    print("You now have $%d." % balance)
            elif sell == "2":
                #IN PROGRESS
                print("You have chosen to sell your bitcoin.")
                print("You currently have: %d bitcoins" % bitcoinowned)
                time.sleep(1)
                bmoney = bitcoin * bitcoinowned
                print("You have sold your bitcoins for $%d." % bmoney)
                balance = balance + bmoney
                print("You now have $%d." % balance)
            else:
                print("No number matches your input!")

        
        else:
            print("Incorrect command!")

        if balance < 0:
            print("You have run out of money.")
            time.sleep(0.2)
            if possession == 0:
                print("Game over.")
                time.sleep(5)
                Return
            else:
                continue
            #TO DO ^
            

print("Welcome to Crypto!")
time.sleep(0.5)
print("Your goal is to make as much money as possible.")
time.sleep(1)
print("Type !help to see commands.")
run()
