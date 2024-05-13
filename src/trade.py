#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## B-CNA-410-MAR-4-1-trade-elisa.huang
## File description:
## trade
##

import sys
import math

# settings player_names player0
# settings your_bot player0
# settings timebank 2000
# settings time_per_move 100
# settings candle_interval 3600
# settings candle_format pair,date,high,low,open,close,volume
# settings candles_total 556
# settings candles_given 336
# settings initial_stack 1000
# settings transaction_fee_percent 0.2

class Settings:
    def __init__(self):
        self.data

    def setSetting(self, input):
        self.data = input.split(" ")
        setattr(self, self.data[0], self.data[1])
        

# update game next_candles USDT_BTC,1620550800,58400,57589.94,58159.59,57952.52,168676077.6
# update game next_candles USDT_BTC,1620554400,58052.33,57535.61,57952.53,57955.04,142785493.3
# update game next_candles USDT_BTC,1620558000,58200,57865.85,57955.04,57907.49,125199288.1
# update game next_candles USDT_BTC,1620561600,58000,56235.66,57907.49,56433.53,418959979.9

class Candles:
    def __init__(self):
        self.data

    def setSetting(self, input):
        self.data = input.split(" ")
        setattr(self, self.data[0], self.data[1])

class Bot:
    def __init__(self):
        self.settings = Settings()
        self.data
        self.candles
    def processInput(self, input):
        self.data = input.split(" ")
        if (self.data[0] == "settings"):
            self.settings.setSetting(self.data[1:])
        if (self.data[0] == "update" and self.data[1] == "game"):
            self.addCandle(self.data[1:])
    def addCandles(self, input):
        self

def main(void):
    bot = Bot()
    while (1) :
        read = input()
        print(read)
    return 0
