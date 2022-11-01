"""
class for sorting an array of T's, A's, and M's
"""

class SortTAM:
    def __init__(self, tam):
        self.tamuk = [c for c in tam]
        # if the last character in the string is '#', remove from array
        if self.tamuk[-1] == '#':
            self.tamuk = self.tamuk[:-1]
    
    # sorts the tamuk array
    def sort_tam(self):
        last_t = -1
        first_m = len(self.tamuk)
        i = 0
        while(i < first_m):
            if self.tamuk[i] == 'M':
                while(self.tamuk[first_m - 1] == 'M'):
                    first_m -= 1
                if i < first_m - 1:
                    self.swap(i, first_m - 1)
                    first_m -= 1
            if self.tamuk[i] == 'T':
                if i > last_t + 1:
                    self.swap(i, last_t + 1)
                last_t += 1
            i += 1
    # swaps elements in the i-th and j-th position of the array tamuk
    def swap(self, i, j):
        self.tamuk[i], self.tamuk[j] = self.tamuk[j], self.tamuk[i]


def main():
    raw_input = input("Please enter a string of T's, A's, and M's in any order (i.e. MMAATT):")
    st = SortTAM(raw_input)
    st.sort_tam()
    print(f'The sorted string is {"".join(st.tamuk)}')

if __name__ == '__main__':
    main()