import random

class SlotMachine:
    symbols=['A','B','C','D']  #Define symbols
    def __init__(self, balance):
        self.balance=balance

    def spin_reel(self):
        return random.choice(self.symbols)  #Spin the reel and get a random symbol

    def play(self):
        while True:
            print("Press enter to play (q to quit)")
            choice=input()
            if choice.lower()=='q':
                break
            lines=int(input("Enter the number of lines to bet on (1-3): "))
            if lines not in [1, 2, 3]:
                
                print("Invalid input. Please enter a number between 1 and 3.")
                continue
            bet_per_line=float(input("What would you like to bet on each line? $"))
            total_bet=bet_per_line*lines
            if total_bet>self.balance:
                print("Insufficient balance.")
                continue
            
            print(f"You are betting ${bet_per_line} on {lines} lines. Total bet is equal to: ${total_bet}")
            #Generate symbols for each line
            symbols=[]
            for j in range(3):
                line=[]
                for j in range(3):
                    line.append(self.spin_reel())
                symbols.append(line)

            for i,line in enumerate(symbols,start=1):
                print(" | ".join(line))  
            winnings=self.calculate_winnings(symbols)
            self.balance+=winnings-total_bet
            
            print(f"You won ${winnings}.")
            winning_lines=[]
            for i,line in enumerate(symbols, start=1):
                if self.check_win(line):
                    winning_lines.append(i)

            if winnings > 0:
                print(f"You won on lines: {','.join(map(str,winning_lines))}")
            print(f"Current balance is ${self.balance}")

    def calculate_winnings(self,symbols):
        total_winnings=0
        for line in symbols:
            if self.check_win(line):
                total_winnings+=10  #Arbitrary winning amount
        return total_winnings

    def check_win(self, line):
        return all(symbol==line[0] for symbol in line)

balance=100  #Initial balance
slot_machine=SlotMachine(balance)
slot_machine.play()
