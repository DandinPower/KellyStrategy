import matplotlib.pyplot as plt
import math
import random

POSITIVE_INFINITY = 10000000

def Kali(odds, winrate):
    return ((odds * winrate) - 1 + winrate)/odds

#回傳下注結果
def GetBetResult(winrate):
    time = POSITIVE_INFINITY * winrate
    bet = random.randint(1,POSITIVE_INFINITY)
    if (bet <= time):
        return True
    else:
        return False

class Wallet:
    def __init__(self, balance):
        self.balance = balance 
        self.record = [balance]

    def Bet(self,odds,winrate,size):
        if(GetBetResult(winrate)):
            #self.balance += self.balance*size*odds
            betSize = size * self.balance
            self.balance -= betSize
            self.balance += ((odds + 1) * betSize)
        else:
            betSize = size * self.balance
            #self.balance -= self.balance*size 
            self.balance -= betSize
        self.record.append(self.balance)

    def BetByKali(self, odds, winrate):
        size = Kali(odds,winrate)
        #print(size)
        self.Bet(odds,winrate,size)

    def BetBySelf(self, odds, winrate, size):
        self.Bet(odds,winrate,size)

    def ShowRecord(self):
        #intRecord = []
        length = len(self.record)
        x = []
        for i in range(length):
            #intRecord.append(int(self.record[i]))
            x.append(i)
        #print(x)
        plt.plot(x,self.record, c = "r")
        plt.show()

def main():
    #print(Kali(1,0.6))
    wallet = Wallet(7000)
    for i in range(10):
        wallet.BetByKali(1, 1)
    wallet.ShowRecord()
    #print(wallet.record)

if __name__ == '__main__':
    main()