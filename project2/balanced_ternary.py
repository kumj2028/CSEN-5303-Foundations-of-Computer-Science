"""
class for converting an integer from decimal to balanced ternary
"""
# used to read the lookup csv file
import csv

class BalancedTernary:
    INTERVALS = ((1, 1), (2, 4), (5, 13), (14, 40), (41, 121))
    lookup_table = {}
    with open('tests/lookup.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            lookup_table[int(row[0])] = list(map(int, row[1:]))

    def __init__(self, dlist, alg_flag='interval'):
        self.dlist = dlist
        self.btlist = []
        self.convert(alg_flag)
    
    # converts the decimal integers in dlist to balanced ternary in btlist
    def convert(self, alg_flag='interval'):
        for i in self.dlist:
            # itv_flag tells method whether to use interval method
            match alg_flag:
                case 'interval':
                    self.btlist.append(BalancedTernary.decimal_to_balanced_ternary_interval(i))
                case 'ternary':
                    self.btlist.append(BalancedTernary.decimal_to_balanced_ternary(i))
                case 'lookup':
                    self.btlist.append(BalancedTernary.lookup_table[i])
    
    # converts an integer to a balanced ternary list using pure math
    @staticmethod
    def decimal_to_balanced_ternary(i):
        bt = []
        j = abs(i)
        n = 0
        while (j > 0):
            j, rem = divmod(j, 3)
            if rem == 2:
                if i > 0:
                    bt.append(-3**n)
                else:
                    bt.append(3**n)
                j += 1
            elif rem == 1:
                if i > 0:
                    bt.append(3**n)
                else:
                    bt.append(-3**n)
            n += 1
        # since we want the largest power of three first, we reverse the order
        bt.reverse()
        return bt

    # converts an integer to a balanced ternary list using intervals
    @staticmethod
    def decimal_to_balanced_ternary_interval(i):
        bt = []
        # interval method only supports integers in the range -121 to 121
        if (abs(i) > 121):
            raise ValueError('number out of range (must be between -121 and 121)')
        while (i != 0):
            for n, (a, b) in enumerate(BalancedTernary.INTERVALS):
                if a <= abs(i) <= b:
                    if i > 0:
                        bt.append(3**n)
                        i -= 3**n
                    else:
                        bt.append(-3**n)
                        i -= -3**n
        return bt

def main():
    raw_input = input("Please enter a list of integers between -121 and 121, each separated by a space(i.e. 36 -74 13):")
    dlist = list(map(int, raw_input.split()))
    bt = BalancedTernary(dlist, alg_flag='ternary')
    for n in range(len(dlist)):
        result = ''
        for m in range(len(bt.btlist[n])):
            if m == 0:
                result += str(bt.btlist[n][m])
            else:
                if bt.btlist[n][m] < 0:
                    result += ' - ' + str(-bt.btlist[n][m])
                else:
                    result += ' + ' + str(bt.btlist[n][m])
        print(f'{dlist[n]} = {result}')

if __name__ == '__main__':
    main()