import unittest
from sort_tam import SortTAM

class TestSortTAM(unittest.TestCase):
    # test already sorted
    def test_already_sorted(self):
        tam = 'TTAAAMMMM'
        st = SortTAM(tam)
        st.sort_tam()
        self.assertEqual(''.join(st.tamuk), tam)
    
    #test a string with all 3 types of letters
    def test_normal(self):
        tam = 'ATMTTAMMAM'
        st = SortTAM(tam)
        st.sort_tam()
        self.assertEqual(''.join(st.tamuk), 'TTTAAAMMMM')
    
    #test a string with only Ts and Ms
    def test_tm(self):
        tam = 'MTMMMTTTMTM'
        st = SortTAM(tam)
        st.sort_tam()
        self.assertEqual(''.join(st.tamuk), 'TTTTTMMMMMM')
    
    #test a string with only As and Ms
    def test_am(self):
        tam = 'AMMMAAMAMAM'
        st = SortTAM(tam)
        st.sort_tam()
        self.assertEqual(''.join(st.tamuk), 'AAAAAMMMMMM')
    
    #test a string with only As and Ts
    def test_at(self):
        tam = 'ATAATATTATA'
        st = SortTAM(tam)
        st.sort_tam()
        self.assertEqual(''.join(st.tamuk), 'TTTTTAAAAAA')

if __name__ == '__main__':
    unittest.main()