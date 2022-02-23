import tkinter as tk
from tkinter import ttk
from Kali import *

def callbackFunc():
    wallet = Wallet(int(walletString.get()))
    for i in range(int(timesString.get())):
        wallet.BetByKali(int(oddsString.get()), float(winrateString.get()))
    wallet.ShowRecord()
    print(wallet.record)
     
app = tk.Tk() 
app.geometry('200x150')

labelWallet = tk.Label(app, text = "本金")
labelWallet.grid(column=0, row=0, sticky=tk.W)
labelOdds = tk.Label(app,text = "賠率(不含本金)")
labelOdds.grid(column=0, row=1, sticky=tk.W)
labelWinrate = tk.Label(app,text = "勝率")
labelWinrate.grid(column=0, row=2, sticky=tk.W)
labelTimes = tk.Label(app,text = "次數")
labelTimes.grid(column=0, row=3, sticky=tk.W)

walletString = tk.StringVar()
oddsString = tk.StringVar()
winrateString = tk.StringVar()
timesString = tk.StringVar()
entryWallet = tk.Entry(app, width=20, textvariable=walletString)
entryOdds = tk.Entry(app, width=20, textvariable=oddsString)
entryWinrate = tk.Entry(app, width=20, textvariable=winrateString)
entryTimes = tk.Entry(app, width=20, textvariable=timesString)

entryWallet.grid(column=1, row=0, padx=10)
entryOdds.grid(column=1, row=1, padx=10)
entryWinrate.grid(column=1, row=2, padx=10)
entryTimes.grid(column=1, row=3, padx=10)

resultButton = tk.Button(app, text = 'Get Result',command=callbackFunc)

resultButton.grid(column=0, row=4, pady=10, sticky=tk.W)

resultString=tk.StringVar()
resultLabel = tk.Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=4, padx=10, sticky=tk.W)

app.mainloop()