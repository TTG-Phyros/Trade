#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## B-CNA-410-MAR-4-1-trade-elisa.huang
## File description:
## trade
##

import sys
import math

class Pattern:
    def __init__(self):
        self.buying = False
        self.selling = False
        self.testDict = {
            "abdandonedBaby" : self.isAbdandonedBaby,
            "advancedBlockBearish" : self.isAdvancedBlockBearish,
            "beltHoldBearish" : self.isBeltHoldBearish,
            "breakawayBearish" : self.isBreakawayBearish,
            "darkCloudCover" : self.isDarkCloudCover,
            "deliberationBearish" : self.isdeliberationBearish,
            "downsideGapThreeMethodsBearish" : self.isDownsideGapThreeMethodsBearish,
            "downsideTasukiGapBearish" : self.isDownsideTasukiGapBearish,
            "dojiStarBearish" : self.isDojiStarBearish,
            "dojiGraveStoneBearish" : self.isDojiGraveStoneBearish,
            "dragonFlyDojiBearish" : self.isDragonFlyDojiBearish,
            "engulfingBearish" : self.isEngulfingBearish,
            "eveningDojiStarBearish" : self.isEveningDojiStarBearish,
            "eveningStarBearish" : self.isEveningStarBearish,
            "fallingThreeMethodsBearish" : self.isFallingThreeMethodsBearish,
            "graveStoneDojiBearish" : self.isGraveStoneDojiBearish,
            "hangingManBearish" : self.isHangingManBearish,
            "haramiBearish" : self.isHaramiBearish,
            "haramiCrossBearish": self.isHaramiCrossBearish,
            "identicalTHreeCrowsBearish" : self.isIdenticalTHreeCrowsBearish,
            "inNeckBearish" : self.isInNeckBearish,
            "kickingBearish" : self.isKickingBearish,
            "meetingLinesBearish" : self.isMeetingLinesBearish,
            "onNeckBearish" : self.isOnNeckBearish,
            "separatingLinesBearish" : self.isSeparatingLinesBearish,
            "shootingStarBearish" : self.isShootingStarBearish,
            "sideBySideWhiteLinesBearish" : self.isSideBySideWhiteLinesBearish,
            "threeBlackCrowsBearish" : self.isThreeBlackCrowsBearish,
            "threeInsideDownBearish" : self.isThreeInsideDownBearish,
            "threeLineStrikeBearish" : self.isThreeLineStrikeBearish,
            "threeOutsideDownBearish" : self.isThreeOutsideDownBearish,
            "trustingBearish" : self.isThrustingBearish,
            "triStarBearish" : self.isTriStarBearish,
            "tweezerTopBearish" : self.isTweezerTopBearish,
            "towCrowsBearish" : self.isTwoCrowsBearish,
            "upsideGapTwoCrowsBearish" : self.isUpsideGapTwoCrowsBearish,
        }

    # ABS(C2 - O2) > .5 * (H2 - L2) AND C2 > O2 AND ABS(C1 - O1) <= .05 * (H1 - L1) AND (C1 + O1) / 2 - L1 >= .4 * (H1 - L1) AND
    # (C1 + O1) / 2 - L1 <= .6 * (H1 - L1) AND L1 > H2 AND C < O AND H < L1 AND O > C2 AND (L > O2 OR C < L2)
    def isAbdandonedBaby(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]
        if (abs(candle2.getClose() - candle2.getOpen()) > 0.5 * (candle2.getHigh() - candle2.getLow()) and
            candle2.getClose() > candle2.getOpen() and
            abs(candle1.getCLose() - candle1.getOpen()) <= 0.05 * (candle1.getHigh() - candle1.getLow()) and
            (candle1.getClose() + candle1.getOpen()) / 2 - candle1.getLow() >= 0.4 * (candle1.getHigh() - candle1.getLow()) and
            (candle1.getHigh() - candle1.getLow()) / 2 - candle1.getLow() <= 0.6 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getLow() > candle2.getHigh() and
            candle0.getClose() < candle0.getOpen() and
            candle0.getHigh() < candle1.getLow() and
            candle0.getOpen() > candle2.getClose() and
            (candle0.getLow() > candle2.getOpen() or candle0.getClose() < candle2.getLow())):
            self.buying = False
            self.selling = True
            return True
        return False

    # H - L > AVGH21 - AVGL21 AND ABS(C1 - O1) > .5 * (H1 - L1) AND ABS(C2 - O2) > .5 * (H2 - L2) AND C > C1 AND C1 > C2 AND O1 > O2 AND
    # O1 < C2 AND O > O1 AND O < C1 AND H - L < .8 * (H1 - L1) AND H1 - L1 < .8 * (H2 - L2) AND H - C > O - L AND H1 - C1 > O1 - L1
    def isAdvancedBlockBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]
        def movingAverage(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL
        AVGH21, AVGL21 = movingAverage(candles[-21:])
        if (candle0.getHigh() - candle0.getLow() > AVGH21 - AVGL21 and
            abs(candle1.getClose() - candle1.getOpen()) > 0.5 * (candle1.getHigh() - candle1.getLow()) and
            abs(candle2.getClose() - candle2.getOpen()) > 0.5 * (candle2.getHigh() - candle2.getLow()) and
            candle0.getClose() > candle1.getClose() and
            candle1.getClose() > candle2.getClose() and
            candle1.getOpen() > candle2.getOpen() and
            candle1.getOpen() > candle2.getClose() and
            candle1.getOpen() > candle2.getOpen() and
            candle1.getOpen() < candle2.getClose() and
            candle0.getOpen() > candle1.getOpen() and
            candle0.getOpen() < candle1.getClose() and
            candle0.getHigh() - candle1.getLow() < 0.8 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getHigh() - candle1.getLow() < 0.8 * (candle2.getHigh() - candle2.getLow()) and
            candle0.getHigh() - candle0.getClose() > candle0.getOpen() - candle0.getLow() and
            candle1.getHigh() - candle1.getClose() > candle1.getOpen() - candle1.getLow()):
            self.buying = False
            self.selling = True
            return True
        return False

    # O = MAXO10 AND O > H1 AND O - C >= .7 * (H - L) AND H - L >= 1.2 * (AVGH10 - AVGL10) AND H - O <= .01 * (H - L) AND C >= H1 - .5 * (H1 - L1) AND H1 > L1 AND H > L AND C1 > C2 AND C2 < C3
    def isBeltHoldBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]
        candle3 = candles[-4]
        def calculate_max_open(candles):
            return max(candle.getOpen() for candle in candles)
        MAXO10 = calculate_max_open(candles[-10:])
        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL
        AVGH10, AVGL10 = calculate_moving(candles[-11:])
        if (candle0.getOpen() == MAXO10 and
            candle0.getOpen() > candle1.getHigh() and
            candle0.getOpen() - candle0.getClose() >= 0.7 * (candle0.getHigh() - candle0.getLow()) and
            candle0.getHigh() - candle0.getLow() >= 1.2 * (AVGH10 - AVGL10) and
            candle0.getHigh() - candle0.getOpen() <= 0.01 * (candle0.getHigh() - candle0.getLow()) and
            candle0.getClose() >= candle1.getHigh() - 0.5 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getHigh() > candle1.getLow() and
            candle0.getHigh() > candle0.getLow() and
            candle1.getClose() > candle2.getClose() and
            candle2.getClose() < candle3.getClose()):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C4 - O4) > .5 * (H4 - L4) AND C4 > O4 AND C3 > O3 AND L3 > H4 AND C2 > C3 AND C1 > C2 AND C < O AND L < H4 AND H > L3
    def isBreakawayBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]
        candle3 = candles[-4]
        candle4 = candles[-5]
        if (abs(candle4.getClose() - candle4.getOpen()) > 0.5 * (candle4.getHigh() - candle4.getLow()) and
            candle4.getClose() > candle4.getOpen() and
            candle3.getClose() > candle3.getOpen() and
            candle3.getLow() > candle4.getHigh() and
            candle2.getClose() > candle3.getClose() and
            candle1.getClose() > candle2.getClose() and
            candle0.getClose() < candle0.getOpen() and
            candle0.getLow() < candle4.getHigh() and
            candle0.getHigh() > candle3.getLow()):
            self.buying = False
            self.selling = True
            return True
        return False

    # C1 - O1 >= .7 * (H1 - L1) AND H1 - L1 >= AVGH10.1 - AVGL10.1 AND O > C1 AND C < C1 - .5 * (C1 - O1) AND C > O1
    def isDarkCloudCover(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL
        AVGH10_1, AVGL10_1 = calculate_moving(candles[-11:-1])

        if (candle1.getCLose() -  candle1.getOpen() >= 0.7 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getHigh() - candle1.getLow() >= AVGH10_1 - AVGL10_1 and
            candle0.getOpen() > candle1.getClose() and
            candle0.getClose() < candle1.getClose() - 0.5 * (candle1.getClose() - candle1.getOpen()) and candle0.getClose() > candle1.getOpen()):
            self.buying = False
            self.selling = True
            return True

        return False


    # ABS(C2 - O2) > .5 * (H2 - L2) AND ABS(C1 - O1) > .5 * (H1 - L1) AND C1 > C2 AND C2 > O2 AND C1 > O1 AND O > H1 AND (C + O) / 2 - L > .4 * (H - L) AND (C + O) / 2 - L < .6 * (H - L) AND ABS(C - O) < .6 * (H - L)
    def isdeliberationBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]

        if (abs(candle2.getClose() - candle2.getOpen()) > 0.5 * (candle2.getHigh() - candle2.getLow()) and
            abs(candle1.getClose() - candle1.getOpen()) > 0.5 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getClose() > candle2.getClose() and
            candle2.getClose() > candle2.getOpen() and
            candle1.getClose() > candle1.getOpen() and
            candle0.getOpen() > candle1.getHigh() and
            (candle0.getClose() + candle0.getOpen()) / 2 - candle0.getLow() > 0.4 * (candle0.getHigh() - candle0.getLow()) and
            abs(candle0.getClose() - candle0.getOpen()) < 0.6 * (candle0.getHigh() - candle0.getLow())):
            self.buying = False
            self.selling = True
            return True

        return False


    # ABS(C2 - O2) > .5 * (H2 - L2) AND ABS(C1 - O1) > .5 * (H1 - L1) AND C2 < O2 AND C1 < O1 AND H1 < L2 AND L < H1 AND H > L2 AND C > O
    def isDownsideGapThreeMethodsBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]

        if (abs(candle2.getClose() - candle2.getOpen()) > 0.5 * (candle2.getHigh() - candle2.getLow()) and
            abs(candle1.getClose() - candle1.getOpen()) > 0.5 * (candle1.getHigh() - candle1.getLow()) and
            candle2.getClose() < candle2.getOpen() and
            candle1.getClose() < candle1.getOpen() and
            candle1.getHigh() < candle2.getLow() and
            candle0.getLow() < candle1.getHigh() and 
            candle0.getHigh() > candle2.getLow() and
            candle0.getClose() > candle0.getOpen()):
            self.buying = False
            self.selling = True
            return True
        return False


    # C2 < O2 AND C1 < O1 AND H1 < L2 AND O > C1 AND O < O1 AND C > H1 AND C < L2
    def isDownsideTasukiGapBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]
        if (candle2.getClose() < candle2.getOpen() and
            candle1.getClose() < candle1.getOpen() and
            candle1.getHigh() < candle2.getLow() and
            candle0.getOpen() > candle1.getClose() and
            candle0.getOpen() < candle1.getOpen() and
            candle0.getClose() > candle0.getHigh() and
            candle0.getClose() < candle2.getLow()):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C1 - O1) > .5 * (H1 - L1) AND O > C1 AND ABS(C - O) < .05 * (H - L) AND H - L < .2 * (AVGH21 - AVGL21)
    def isDojiStarBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]

        O0, C0, H0, L0 = candle0.getOpen(), candle0.getClose(), candle0.getHigh(), candle0.getLow()
        O1, C1, H1, L1 = candle1.getOpen(), candle1.getClose(), candle1.getHigh(), candle1.getLow()
        def movingAverage(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL
        AVGH21, AVGL21 = movingAverage(candles[-21:])
        condition_1 = abs(C1 - O1) > 0.5 * (H1 - L1)
        condition_2 = O1 > C1
        condition_3 = abs(C0 - O0) < 0.5 * (H0 - L0)
        condition_4 = H0 - L0 < 0.2 * (AVGH21 - AVGL21)
        if (condition_1 and condition_2 and condition_3 and condition_4):
            self.buying = False
            self.selling = True
            return True
        return False
    
    # ABS(O - C) <= .01 * (H - L) AND (H - C) >= .95 *(H - L) AND (H > L) AND (H = MAXH10) AND (H - L) >= (AVGH10 - AVGL10)
    def isDojiGraveStoneBearish(self, candles):
        candle0 = candles[-1]

        O0, C0, H0, L0 = candle0.getOpen(), candle0.getClose(), candle0.getHigh(), candle0.getLow()
        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL
        AVGH10, AVGL10 = calculate_moving(candles[-11:])
        def calculate_max_high(candles):
            return max(candle.getHigh() for candle in candles)

        MAXH10 = calculate_max_high(candles[-10:])
        condition_1 = abs(O0 - C0) <= 0.1 * (H0 - L0)
        condition_2 = (H0 - C0) >= 0.95 * (H0 - L0)
        condition_3 = (H0 > L0)
        condition_4 = (H0 == MAXH10)
        condition_5 = (H0 - L0) >= (AVGH10 - AVGL10)
        if (condition_1 and condition_2 and condition_3 and condition_4 and condition_5):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(O - C) <= .02 * (H - L) AND (H - C) <= .3 * (H - L) AND (H - L) >= (AVGH10 - AVGL10) AND (H > L) AND (H = MAXH10)
    def isDragonFlyDojiBearish(self, candles):
        candle0 = candles[-1]

        O0, C0, H0, L0 = candle0.getOpen(), candle0.getClose(), candle0.getHigh(), candle0.getLow()
        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL
        AVGH10, AVGL10 = calculate_moving(candles[-11:])
        def calculate_max_high(candles):
            return max(candle.getHigh() for candle in candles)

        MAXH10 = calculate_max_high(candles[-10:])

        condition_1 = abs(O0 - C0) <= 0.2 * (H0 - L0)
        condition_2 = (H0 - C0) <= 0.3 * (H0 - L0)
        condition_3 = (H0 - L0) >= (AVGH10 - AVGL10)
        condition_4 = (H0 > L0)
        condition_5 = (H0 == MAXH10)
        if (condition_1 and condition_2 and condition_3 and condition_4 and condition_5):
            self.buying = False
            self.selling = True
            return True
        return False

    # C1 > O1 AND O - C >= .7 * (H - L) AND C < O1 AND O > C1 AND H - L >= 1.2 * (AVGH10 - AVGL10)
    def isEngulfingBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]

        O0, C0, H0, L0 = candle0.getOpen(), candle0.getClose(), candle0.getHigh(), candle0.getLow()
        O1, C1 = candle1.getOpen(), candle1.getClose()

        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL
        AVGH10, AVGL10 = calculate_moving(candles[-11:])
        
        condition_1 = C1 > O1
        condition_2 = O0 - C0 >= 0.7 * (H0 - L0)
        condition_3 = C0 < O1
        condition_4 = O0 > C1
        condition_5 = H0 - L0 >= 1.2 * (AVGH10 - AVGL10)

        if (condition_1 and condition_2 and condition_3 and condition_4 and condition_5):
            self.buying = False
            self.selling = True
            return True
        return False
    
    # ABS(C2 - O2) > .5 * (H - L) AND C2 > O2 AND ABS(C1 - O1) < .05 * (H1 - L1) AND H1 - L1 < .2 * (AVGH21.1 - AVGL21.1) AND O1 > C2 AND C < O
    def isEveningDojiStarBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]

        O0, C0 = candle0.getOpen(), candle0.getClose()
        O1, C1, H1, L1 = candle1.getOpen(), candle1.getClose(), candle1.getHigh(), candle1.getLow()
        O2, C2, H2, L2 = candle2.getOpen(), candle2.getClose(), candle2.getHigh(), candle2.getLow()

        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL

        AVGH21_1, AVGL21_1 = calculate_moving(candles[-22:-1])

        condition_1 = abs(C2 - O2) > 0.5 * (H2 - L2)
        condition_2 = C2 > O2
        condition_3 = abs(C1 - O1) < 0.05 * (H1 - L1)
        condition_4 = H1 - L1 < 0.2 * (AVGH21_1 - AVGL21_1)
        condition_5 = O1 > C2
        condition_6 = C0 < O0

        if (condition_1 and condition_2 and condition_3 and condition_4 and 
            condition_5 and condition_6):
            self.buying = False
            self.selling = True
            return True

        return False


    # C2 - O2 >= .7 * (H2 - L2) AND H2 - L2 >= AVGH10.2 - AVGL10.2 AND C1 > C2 AND  O1 > C2 AND H - L >= AVGH10 - AVGL10 AND O - C >= .7 * (H - L) AND O < O1 AND O < C1
    def isEveningStarBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]

        O0, C0, H0, L0 = candle0.getOpen(), candle0.getClose(), candle0.getHigh(), candle0.getLow()
        O1, C1 = candle1.getOpen(), candle1.getClose()
        O2, C2, H2, L2 = candle2.getOpen(), candle2.getClose(), candle2.getHigh(), candle2.getLow()

        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL

        AVGH10_2, AVGL10_2 = calculate_moving(candles[-13:-3])
        AVGH10, AVGL10 = calculate_moving(candles[-11:])

        condition_1 = C2 - O2 >= 0.7 * (H2 - L2)
        condition_2 = H2 - L2 >= AVGH10_2 - AVGL10_2
        condition_3 = C1 > C2
        condition_4 = O1 > C2
        condition_5 = H0 - L0 >= AVGH10 - AVGL10
        condition_6 = O0 - C0 >= 0.7 * (H0 - L0)
        condition_7 = O0 < O1
        condition_8 = O0 < C1

        if (condition_1 and condition_2 and condition_3 and condition_4 and 
            condition_5 and condition_6 and condition_7 and condition_8):
            self.buying = False
            self.selling = True
            return True

        return False


    # ABS(C4 - O4) > .5 * (H4 - L4) AND C4 < O4 AND ABS(C3 - O3) < ABS(C4 - O4) AND ABS(C2 - O2) < ABS(C4 - O4) AND ABS(C1 - O1) < ABS(C4 - O4) AND L3 >= L4 AND H3 <= H4 AND L2 >= L4 AND H2 <= H4 AND L1 >= L4 AND H1 <= H4 AND H2 > H3 AND H1 > H2 AND C < O AND C < C4
    def isFallingThreeMethodsBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
        candle2 = candles[-3]
        candle3 = candles[-4]
        candle4 = candles[-5]

        O0, C0 = candle0.getOpen(), candle0.getClose()
        O1, C1, H1, L1 = candle1.getOpen(), candle1.getClose(), candle1.getHigh(), candle1.getLow()
        O2, C2, H2, L2 = candle2.getOpen(), candle2.getClose(), candle2.getHigh(), candle2.getLow()
        O3, C3, H3, L3 = candle3.getOpen(), candle3.getClose(), candle3.getHigh(), candle3.getLow()
        O4, C4, H4, L4 = candle4.getOpen(), candle4.getClose(), candle4.getHigh(), candle4.getLow()

        condition_1 = abs(C4 - O4) > 0.5 * (H4 - L4)
        condition_2 = C4 < O4
        condition_3 = abs(C3 - O3) < abs(C4 - O4)
        condition_4 = abs(C2 - O2) < abs(C4 - O4)
        condition_5 = abs(C1 - O1) < abs(C4 - O4)
        condition_6 = L3 >= L4 and H3 <= H4
        condition_7 = L2 >= L4 and H2 <= H4
        condition_8 = L1 >= L4 and H1 <= H4
        condition_9 = H2 > H3
        condition_10 = H1 > H2
        condition_11 = C0 < O0
        condition_12 = C0 < C4

        if (condition_1 and condition_2 and condition_3 and condition_4 and 
            condition_5 and condition_6 and condition_7 and condition_8 and 
            condition_9 and condition_10 and condition_11 and condition_12):
            self.buying = False
            self.selling = True
            return True

        return False

    # ABS(C - O) < (H - L) / 3 AND O > C1 AND (C + O) / 2 - L < .4 * (H - L) AND H = MAXH10
    def isGraveStoneDojiBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]

        O, C, H, L = candle0.getOpen(), candle0.getClose(), candle0.getHigh(), candle0.getLow()
        C1 = candle1.getClose()

        def calculate_max_high(candles):
            return max(candle.getHigh() for candle in candles)

        MAXH10 = calculate_max_high(candles[-10:])

        condition_1 = abs(C - O) < (H - L) / 3
        condition_2 = O > C1
        condition_3 = (C + O) / 2 - L < 0.4 * (H - L)
        condition_4 = H == MAXH10
        if condition_1 and condition_2 and condition_3 and condition_4:
            self.buying = False
            self.selling = True
            return True
        return False


    
    #  ABS(C >= O) * O + ABS(C < O) * C - L >= 2 * ABS(C - O) AND (C + O) / 2 - L > 2 * (H - (C + O) / 2) AND ABS(C - O) > .01
    def isHangingManBearish(self, candles):
        candle0 = candles[-1]

        if (abs(candle0.getClose() >= candle0.getOpen()) * candle0.getOpen() + abs(candle0.getClose() < candle0.getOpen()) * candle0.getClose() - candle0.getLow() >= 2 * abs(candle0.getClose() - candle0.getOpen()) and
            (candle0.getClose() + candle0.getOpen()) / 2 - candle0.getLow() > 2 * (candle0.getHigh() - (candle0.getClose() + candle0.getOpen()) / 2) and abs(candle0.getClose() - candle0.getOpen()) > 0.01):
            self.buying = False
            self.selling = True
            return True

        return False

    # C1 - O1 >= .7 * (H1 - L1) AND H1 - L1 >= AVGH10.1 - AVGL10.1 AND C < O AND O < C1 AND C > O1 AND O - C <= .6 * (C1 - O1)
    def isHaramiBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]

        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL

        C1, O1, H1, L1 = candle1.getClose(), candle1.getOpen(), candle1.getHigh(), candle1.getLow()
        C, O = candle0.getClose(), candle0.getOpen()

        AVGH10_1, AVGL10_1 = calculate_moving(candles[-11:-1])

        condition_1 = C1 - O1 >= 0.7 * (H1 - L1)
        condition_2 = H1 - L1 >= AVGH10_1 - AVGL10_1
        condition_3 = C < O
        condition_4 = O < C1
        condition_5 = C > O1
        condition_6 = O - C <= 0.6 * (C1 - O1)

        if (condition_1 and condition_2 and condition_3 and condition_4 and 
            condition_5 and condition_6):
            self.buying = False
            self.selling = True
            return True

        return False


    # ABS(C1 - O1) > .5 * (H - L) AND C1 > O1 AND H < C1 AND L > O1 AND ABS(C - O) < .2 * (H - L)
    def isHaramiCrossBearish(self, candles):
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (abs(candle1.getClose() - candle1.getOpen()) > 0.5 * (candle0.getHigh() - candle0.getLow()) and
            candle1.getClose() > candle1.getOpen() and
            candle0.getHigh() < candle1.getClose() and
            candle0.getLow() > candle1.getOpen() and
            abs(candle0.getClose() - candle0.getOpen()) < 0.2 * (candle0.getHigh() - candle0.getLow())):
            self.buying = False
            self.selling = True
            return True
        return False

    # C2 < O2 AND C1 < O1 AND C < O AND C < L1 AND C1 < L2 AND O = C1 AND O1 = C2
    def isIdenticalTHreeCrowsBearish(self, candles):
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (candle2.getClose() < candle2.getOpen() and
            candle1.getClose() < candle1.getOpen() and
            candle0.getClose() < candle0.getOpen() and
            candle0.getClose() < candle1.getLow() and
            candle1.getClose() < candle2.getLow() and
            candle0.getOpen() == candle1.getClose() and
            candle1.getOpen() == candle2.getClose()):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C1 - O1) >.5 * (H1 - L1) AND C1 < O1 AND O < L1 AND C >= C1 AND C < 1.05 * C1
    def isInNeckBearish(self, candles):
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (abs(candle1.getClose() - candle1.getOpen()) > 0.5 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getClose() < candle1.getOpen() and
            candle0.getOpen() < candle1.getLow() and
            candle0.getClose() >= candle1.getClose() and
            candle0.getClose() < 1.05 * candle1.getClose()):
            self.buying = False
            self.selling = True
            return True
        return False


    # C = L AND O = H AND H > L AND H < L1 AND C1 = H1 AND O1 = L1 AND H1 > L1
    def isKickingBearish(self, candles):
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (candle0.getClose() == candle0.getLow() and
            candle0.getOpen() == candle0.getHigh() and
            candle0.getHigh() > candle0.getLow() and
            candle0.getHigh() < candle1.getLow() and
            candle1.getClose() == candle1.getHigh() and
            candle1.getOpen() == candle1.getHigh() and
            candle1.getOpen() == candle1.getLow() and
            candle1.getHigh() > candle1.getLow()):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C1 - O1) > .5 * (H1 - L1) AND C1 > O1 AND (C1 + O1) / 2 > H2 AND ABS(C - O) > .5 * (H - L) AND C < O AND (C + O) / 2 > H1 AND C = C1
    def isMeetingLinesBearish(self, candles):
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (abs(candle1.getOpen() - candle1.getOpen()) > 0.5 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getClose() > candle1.getOpen() and
            (candle1.getClose() + candle1.getOpen()) / 2 > candle2.getHigh() and
            abs(candle0.getClose() - candle0.getOpen()) > 0.5 * (candle0.getHigh() - candle0.getLow()) and
            candle0.getClose < candle0.getOpen() and (candle0.getClose() + candle0.getOpen()) / 2 > candle1.getHigh() and
            candle0 == candle1.getClose()):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C1 - O1) > .5 * (H1 - L1) AND C1 < O1 AND O < L1 AND C = L1
    def isOnNeckBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]

        if (abs(candle1.getClose() - candle1.getOpen()) > 0.5 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getClose() < candle1.getOpen() and
            candle0.getOpen() < candle1.getLow() and
            candle0.getClose() == candle1.getLow()):
            self.buying = False
            self.selling = True
            return True
        return False

    # C1 > O1 AND C < O AND O = O1
    def isSeparatingLinesBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]
    
        if (candle1.getClose() > candle1.getOpen() and
            candle0.getClose() < candle0.getOpen() and
            candle0.getOpen() == candle1.getOpen()):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(O-C)<=.2*(H-L) AND ABS(O-C)>=.1*(H-L) AND (H-O)>=.5*(H-L) AND (H-C)>=.5*(H-L) AND (O-L)<=.05*(H-L) OR (C-L)<=.05*(H-L) AND (H-L)>=.8*(AVGH10-AVGL10) AND (O>=(L1+.5*(H1-L1))) AND (C>=(L1+.5*(H1-L1))) AND (H=MAXH5) AND (H>L)
    def isShootingStarBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]

        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL

        def calculate_max_high(candles):
            return max(candle.getHigh() for candle in candles)

        H, L, O, C = candle0.getHigh(), candle0.getLow(), candle0.getOpen(), candle0.getClose()
        H1, L1 = candle1.getHigh(), candle1.getLow()

        AVGH10, AVGL10 = calculate_moving(candles[-10:])
        MAXH5 = calculate_max_high(candles[-5:])

        condition_1 = abs(O - C) <= 0.2 * (H - L)
        condition_2 = abs(O - C) >= 0.1 * (H - L)
        condition_3 = (H - O) >= 0.5 * (H - L)
        condition_4 = (H - C) >= 0.5 * (H - L)
        condition_5 = (O - L) <= 0.05 * (H - L) or (C - L) <= 0.05 * (H - L)
        condition_6 = (H - L) >= 0.8 * (AVGH10 - AVGL10)
        condition_7 = O >= (L1 + 0.5 * (H1 - L1))
        condition_8 = C >= (L1 + 0.5 * (H1 - L1))
        condition_9 = H == MAXH5
        condition_10 = H > L

        if (condition_1 and condition_2 and condition_3 and condition_4 and 
            condition_5 and condition_6 and condition_7 and condition_8 and 
            condition_9 and condition_10):
            self.buying = False
            self.selling = True
            return True

        return False


    # C2 < O2 AND H1 < L2 AND C1 > O1 AND ABS(C1 - O1) > .95 * ABS(C - O) AND ABS(C1 - O1) < 1.95 * ABS(C - O) AND C > O AND C = C1
    def isSideBySideWhiteLinesBearish(self, candles):
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (candle2.getClose() < candle2.getOpen() and
            candle1.getHigh() < candle2.getLow() and
            candle1.getClose() > candle1.getOpen() and
            abs(candle1.getClose() - candle1.getOpen()) > 0.95 * abs(candle0.getClose() - candle0.getOpen()) and
            abs(candle1.getClose() - candle1.getOpen()) < 1.95 * abs(candle0.getClose() - candle0.getOpen()) and
            candle0.getClose() > candle0.getOpen() and candle0.getClose() == candle1.getClose()):
            self.buying = False
            self.selling = True
            return True
        return False

    # O1 < O2 AND O1 > C2 AND O < O1 AND O > C1 AND C1 < L2 AND C < L1 AND C2 < 1.05 * L2 AND C1 < 1.05 * L1 AND C < 1.05 * L
    def isThreeBlackCrowsBearish(self, candles):
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (candle1.getOpen() < candle2.getOpen() and
            candle1.getOpen() > candle2.getClose() and
            candle0.getOpen() < candle1.getOpen() and
            candle0.getOpen() > candle1.getClose() and
            candle1.getClose() < candle2.getLow() and
            candle0.getClose() < candle1.getLow() and
            candle2.getClose() < 1.05 * candle2.getLow() and
            candle1.getClose() < 1.05 * candle1.getLow() and
            candle0.getClose() < 1.05 * candle0.getLow()):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C2 - O2) > .5 * (H1 - L1) AND C2 > O2 AND C1 < O1 AND H1 < C2 AND L1 > O2 AND C < O AND C < C1
    def isThreeInsideDownBearish(self, candles):
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (abs(candle2.getClose() - candle2.getOpen()) > 0.5 * (candle1.getHigh() - candle1.getLow()) and
            candle2.getCLose() > candle2.getOpen() and
            candle1.getClose() < candle1.getOpen() and
            candle1.getHigh() < candle2.getClose() and
            candle1.getLow() > candle2.getOpen() and
            candle0.getClose() < candle0.getOpen() and
            candle0.getClose() < candle0.getClose()):
            self.buying = False
            self.selling = True
            return True
        return False

    # C3 < O3 AND C2 < O2 AND C2 < C3 AND C1 < O1 AND C1 < C2 AND O < C1 AND C > O3
    def isThreeLineStrikeBearish(self, candles):
        candle3 = candles[-4]
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (candle3.getClose() < candle3.getOpen() and
            candle2.getClose() < candle2.getOpen() and
            candle2.getClose() < candle3.getClose() and
            candle1.getClose() < candle1.getOpen() and
            candle1.getClose() < candle2.getClose() and
            candle0.getOpen() < candle1.getClose() and
            candle0.getClose() > candle3.getOpen()):
            self.buying = False
            self.selling = True
            return True
        return False

    # C1 - O1 >= .7 * (H1 - L1) AND H1 - L1 >= AVGH10.1 - AVGL10.1 AND C < O AND O < C1 AND C > O1 AND O - C <= .6 * (C1 - O1)
    def isThreeOutsideDownBearish(self, candles):
        candle0 = candles[-1]
        candle1 = candles[-2]

        def calculate_moving(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL

        C1, O1, H1, L1 = candle1.getClose(), candle1.getOpen(), candle1.getHigh(), candle1.getLow()
        AVGH10_1, AVGL10_1 = calculate_moving(candles[-11:-1])

        condition_1 = C1 - O1 >= 0.7 * (H1 - L1)
        condition_2 = H1 - L1 >= AVGH10_1 - AVGL10_1
        condition_3 = candle0.getClose() < candle0.getOpen()
        condition_4 = candle0.getOpen() < candle1.getClose()
        condition_5 = candle0.getClose() > candle1.getOpen() 
        condition_6 = candle1.getOpen() - candle0.getClose() <= 0.6 * (candle1.getClose() - candle1.getOpen())

        if condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6:
            self.buying = False
            self.selling = True
            return True

        return False


    # ABS(C1 - O1) > .5 * (H1 - L1) AND C1 < O1 AND O < L1 AND C > C1 AND C < (C1 + O1) / 2
    def isThrustingBearish(self, candles):
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (abs(candle1.getClose() - candle1.getOpen()) > 0.5 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getClose() < candle1.getOpen() and
            candle0.getOpen() < candle1.getLow() and
            candle0.getClose() > candle1.getClose() and
            candle0.getClose() < (candle1.getClose() + candle1.getOpen()) / 2):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C - O) < .05 * (H - L) AND H - L < .2 * (AVGH21 - AVGL21) AND ABS(C1 - O1) < .05 * (H1 - L1) AND H1 - L < .2 * (AVGH21.1-AVGL21.1) AND ABS(C2 - O2) < .05 * (H2 - L2) AND H2 - L2 < .2 * (AVGH21.2 - AVGL21.2) AND L2 > H1 AND L2 > H
    def isTriStarBearish(self, candles):
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]
        
        def movingAverage(candles):
            high_prices = [candle.getHigh() for candle in candles]
            low_prices = [candle.getLow() for candle in candles]
            AVGH = sum(high_prices) / len(high_prices)
            AVGL = sum(low_prices) / len(low_prices)
            return AVGH, AVGL

        H, L, H1, L1, H2, L2 = candle0.getHigh(), candle0.getLow(), candle1.getHigh(), candle1.getLow(), candle2.getHigh(), candle2.getLow()
        AVGH21, AVGL21 = movingAverage(candles[-21:])
        AVGH21_1, AVGL21_1 = movingAverage(candles[-22:-1])
        AVGH21_2, AVGL21_2 = movingAverage(candles[-23:-2])

        condition_1 = abs(candle0.getClose() - candle0.getOpen()) < 0.05 * (H - L) and H - L < 0.2 * (AVGH21 - AVGL21)
        condition_2 = abs(candle1.getClose() - candle1.getOpen()) < 0.05 * (H1 - L1) and H1 - L1 < 0.2 * (AVGH21_1 - AVGL21_1)
        condition_3 = abs(candle2.getClose() - candle2.getOpen()) < 0.05 * (H2 - L2) and H2 - L2 < 0.2 * (AVGH21_2 - AVGL21_2)
        condition_4 = L2 > H1 and L2 > H

        if condition_1 and condition_2 and condition_3 and condition_4:
            self.buying = False
            self.selling = True
            return True

        return False

    # H = H1 AND ABS(C - O) < .2 * ABS(C1 - O1) AND ABS(C1 - O1) >= .9 * (H1 - L1) AND H1 - L1 >= 1.3 * (AVGH20 - AVGL20)
    def isTweezerTopBearish(self, candles):
        high_prices = [candle.getHigh() for candle in candles[-20:]]
        low_prices = [candle.getLow() for candle in candles[-20:]]

        AVGH20 = sum(high_prices) / 20
        AVGL20 = sum(low_prices) / 20

        candle1 = candles[-2]
        candle0 = candles[-1]

        if (candle0.getHigh() == candle1.getHigh() and
            abs(candle0.getClose() - candle0.getOpen) < 0.2 * abs(candle1.getClose() - candle1.getOpen()) and
            abs(candle1.getClose() - candle1.getOpen()) >= 0.9 * (candle1.getHigh() - candle1.getLow()) and
            candle1.getHigh() - candle1.getLow() >= 1.3 * (AVGH20 - AVGL20)):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C2 - O2) > .5 * (H2 - L2) AND C2 > O2 AND L1 > H2 AND C1 < O1 AND O > C1 AND O < O1 AND C < C2 AND C > O2
    def isTwoCrowsBearish(self, candles):
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (abs(candle2.getClose() - candle2.getOpen()) > 0.5 * (candle2.getHigh() - candle2.getLow()) and
            candle2.getClose() > candle2.getOpen() and
            candle1.getLow() > candle2.getHigh() and
            candle1.getClose() < candle1.getOpen() and
            candle0.getOpen() > candle1.getClose() and
            candle0.getOpen() < candle1.getOpen() and
            candle0.getClose() < candle2.getClose() and
            candle0.getClose() > candle2.getClose()):
            self.buying = False
            self.selling = True
            return True
        return False

    # ABS(C2 - O2) > .5 * (H2 - L2) AND C2 > O2 AND L1 > H2 AND C1 < O1 AND O > O1 AND C < C1 AND C > H2
    def isUpsideGapTwoCrowsBearish(self, candles):
        candle2 = candles[-3]
        candle1 = candles[-2]
        candle0 = candles[-1]

        if (abs(candle2.getClose() - candle2.getOpen()) > 0.5 * (candle2.getHigh() - candle2.getLow()) and
            candle2.getClose() > candle2.getOpen() and
            candle1.getLow() > candle2.getHigh() and
            candle1.getClose() < candle1.getOpen() and
            candle0.getOpen() > candle1.getOpen() and
            candle0.getClose() < candle1.getClose() and
            candle0.getClose() > candle2.getHigh()):
            self.buying = False
            self.selling = True
            return True
        return False
    
    def checkPattern(self, candles):
        for name, function in self.testDict.items():
            if (function(candles) == True):
                return name

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
    
    def isDoji(self):
        maxPercentOfVariation = 0.5
        percentOfVariation = 100 - ((self.close / self.open) * 100) if self.open > self.close else 100 - ((self.open / self.close) * 100)
        if percentOfVariation < maxPercentOfVariation:
            return True
        return False

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
        self.percentOfChange = []
        self.uncertainty = False
        self.downTendance = False
        self.upTendance = False

    def getBuying(self):
        return self.buying
    
    def getSelling(self):
        return self.selling
    
    def run(self, candles):
        self.pattern = Pattern()
        self.pattern.checkPattern(candles)
        self.buying = self.pattern.buying
        self.selling = self.pattern.selling
        # self.percentOfChange = []
        # self.uncertainty = True
        # last5Candles = candles[-5:]
        # doji = 0
        # uncertainty = False
        # i = 0
        # for candle in last5Candles:
        #     percent = ((candles[(-6 + i)].getMedian() - candles[(-5 + i)].getMedian()) / candles[(-6 + i)].getMedian()) * -1
        #     self.percentOfChange.append(percent)
        #     if candle.isDoji():
        #         doji += 1
        #     i += 1
        # medianChange = 0
        # for i in range(candles.__len__()):
        #     if i >= 1:
        #         percent = ((candles[(i - 1)].getMedian() - candles[i].getMedian()) / candles[(i - 1)].getMedian()) * -1
        #         medianChange += percent
        # medianChange /= candles.__len__()
        # if doji >= 2:
        #     uncertainty = True
        # if sum(self.percentOfChange) > 0:
        #     self.upTendance = True
        # else:
        #     self.downTendance = True
        # if not uncertainty and self.downTendance and sum(self.percentOfChange) > (3  * abs(medianChange)):
        #     self.buying = True
        # if not uncertainty and self.upTendance and sum(self.percentOfChange) < (3  * abs(medianChange)):
        #     self.selling = True

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
            self.algo.run(self.candles)
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
