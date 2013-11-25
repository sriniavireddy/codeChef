import sys

def atm(cash,bal):
    if cash % 5 != 0 or cash > (bal-0.50) :
        return bal
    else:
        return bal-cash-0.50

lis = sys.stdin.readline().split()
cash = int(lis[0])
bal = float(lis[1])
print("%.2f" % float(atm(cash,bal)))

    
