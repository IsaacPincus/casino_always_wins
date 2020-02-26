import numpy as np

odds = 0.001
casino_wins = 0
iterations = 1000
# extra payout, >1 good for gamblers, <1 good for casino
margin = 1.5

for i in range(iterations):
    casino_cash = 100000
    no_gamblers = 1000
    gamblers_cash = 100
    gamblers = np.ones([no_gamblers,1])*gamblers_cash
    while True:
    ##    print(str(casino_cash))
    ##    print(str(np.count_nonzero(gamblers)))
        for item, gamer in enumerate(gamblers):
            if gamer != 0:
                # always bet 10% of their holdings
                bet = int(np.ceil(gamer/100))
                payout = round((bet*margin)/odds)
                gamblers[item] = gamblers[item] - bet
                casino_cash = casino_cash + bet
                if np.random.randint(1/odds) == 0:
                    gamblers[item] = gamblers[item] + payout
                    casino_cash = casino_cash - payout

        if np.sum(gamblers) == 0:
            #print('gamblers ran out of money')
            casino_wins = casino_wins + 1
            break
        if casino_cash < 0:
            #print('casino ran out of money')
            break


print('casino won ' + str(casino_wins) + ' times out of ' + str(iterations))
print('margin was ' + str(margin))
