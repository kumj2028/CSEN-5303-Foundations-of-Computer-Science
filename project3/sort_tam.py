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
        a = m = -1
        for i in range(len(self.tamuk)):
            if self.tamuk[i] == 'T':
                if a > -1:
                    self.swap(a, i)
                    a += 1
                elif m > -1:
                    self.swap(m, i)
                    m += 1
            if self.tamuk[i] == 'A':
                if m > -1:
                    self.swap(m, i)
                    if a == -1:
                        a = m
                    m += 1
                elif a == -1:
                    a = i
            if self.tamuk[i] == 'M':
                if m == -1:
                    m = i
    
    # swaps elements in the i-th and j-th position of the array tamuk
    def swap(self, i, j):
        self.tamuk[i], self.tamuk[j] = self.tamuk[j], self.tamuk[i]


def main():
    raw_input = input("Please enter a string of T's, A's, and M's in any order (i.e. MMAATT):")
    st = SortTAM(raw_input)
    st.sort_tam()
    print(f'The sorted array is {st.tamuk}')

if __name__ == '__main__':
    main()