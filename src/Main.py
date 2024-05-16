#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## B-CNA-410-MAR-4-1-trade-elisa.huang
## File description:
## trade
##

import sys
import math

class Settings:
    def __init__(self):
        self.data = ""

    def setSetting(self, input):
        self.data = input
        setattr(self, self.data[0], self.data[1])

class Candles:
    def __init__(self, input):
        self.data = "".join(input).split(",")
        self.pair = self.data[0]
        self.date = int(self.data[1])
        self.high = float(self.data[2])
        self.low = float(self.data[3])
        self.open = float(self.data[4])
        self.close = float(self.data[5])
        self.volume = float(self.data[6])
    
    def getMedian(self):
        return (self.open + self.close) / 2
    
    def getClose(self):
        return self.close
    
    def getOpen(self):
        return self.open
    
    def getHigh(self):
        return self.high
    
    def getLow(self):
        return self.low

    def getLowHighPart(self):
        lowDistance = self.close - self.low if self.close < self.open else self.open - self.low
        highDistance = self.high - self.close if self.close > self.open else self.high - self.open
        totalDistance = lowDistance + highDistance
        return ((lowDistance / totalDistance) * 100, (highDistance / totalDistance) * 100)

class Stacks:
    def __init__(self):
        self.data = ""

    def addStack(self, input):
        self.data = "".join(input).split(",")
        for stacks in self.data:
            splited = stacks.split(":")
            setattr(self, splited[0], float(splited[1]))
    
    def getStack(self, stackType):
        return getattr(self, stackType)
    
    def hasStack(self, stackType):
        return hasattr(self, stackType)

class Algorithm:

    def __init__(self):
        self.buying = False
        self.selling = False

    def getBuying(self):
        return self.buying
    
    def getSelling(self):
        return self.selling
    
    def run(self):
        self.buying = True
        self.selling = False

class Bot:
    def __init__(self):
        self.settings = Settings()
        self.candles = []
        self.stacks = Stacks()
        self.data = ""
        self.algo = Algorithm()

    def run(self):
        while True :
            read = input()
            if len(read) == 0:
                continue
            self.processInput(read)

    def getValueBuyable(self, ammountSpendable):
        btcPrice = self.candles[-1].getMedian()
        return ammountSpendable / btcPrice
    
    def getValueSellable(self, ammountWanted):
        btcPrice = self.candles[-1].getMedian()
        return ammountWanted / btcPrice

    def processInput(self, input):
        self.data = input.split(" ")
        if (self.data[0] == "settings"):
            self.settings.setSetting(self.data[1:])
        if (self.data[0] == "update" and self.data[1] == "game" and self.data[2] == "next_candles"):
            self.addCandles(self.data[3:])
        if (self.data[0] == "update" and self.data[1] == "game" and self.data[2] == "stacks"):
            self.stacks.addStack(self.data[3:])
        if (self.data[0] == "action"):
            self.algo.run()
            if (self.algo.getBuying() and (self.stacks.hasStack("USDT") and self.stacks.getStack("USDT") > 51)):
                print(f'buy USDT_BTC {self.getValueBuyable(50)}', flush=True)
            elif (self.algo.getSelling() and (self.stacks.hasStack("BTC") and self.stacks.getStack("BTC") > self.getValueSellable(50))):
                print(f'sell USDT_BTC {self.getValueSellable(50)}', flush=True)
            else:
                print("no_moves")
        self.data = ""

    def addCandles(self, input):
        tempCandle = Candles(input)
        self.candles.append(tempCandle)

    def getListForGroundhog(self):
        list = []
        for candle in self.candles:
            list.append(candle.getMedian())
        return list

if __name__ == "__main__":
    bot = Bot()
    bot.run()
