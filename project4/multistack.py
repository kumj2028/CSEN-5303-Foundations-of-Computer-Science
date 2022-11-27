"""
class for storing multiple stacks in an array
"""

class StackFull(Exception):
    pass

class StackEmpty(Exception):
    pass

class MultiStack:
    def __init__(self, stk_size=3, arr_size=20):
        self.stk_size = stk_size
        self.arr_size = arr_size
        self.arr = [0] * arr_size
        self.tops = [i for i in range(-1, stk_size-1)]
        self.bots = [i for i in range(stk_size)]

    def push(self, snum, elem):
        if self.is_full(snum):
            raise StackFull
        # top of the current stack will overlap with bot of next
        if snum < self.stk_size - 1 and\
        self.tops[snum] + 1 == self.bots[snum + 1]:
            self.reorganize()
            self.push(snum, elem)
        else:
            self.tops[snum] += 1
            self.arr[self.tops[snum]] = elem
    
    def pop(self, snum):
        if self.is_empty(snum):
            raise StackEmpty
        else:
            self.tops[snum] -= 1
    
    def top(self, snum):
        if self.is_empty(snum):
            raise StackEmpty
        else:
            return self.arr[self.tops[snum]]
    
    def is_empty(self, snum):
        return self.tops[snum] < self.bots[snum]
    
    def is_full(self, snum):
        if snum == self.stk_size - 1:
            return self.tops[self.stk_size-1] == self.arr_size - 1
        else:
            return False

    def reorganize(self):
        newtops = self.make_new_tops()
        goal = -1
        for i in range(1, self.stk_size):
            # the new top does not collide
            if i == self.stk_size - 1 or newtops[i] < self.bots[i + 1]:
                # there are earlier stacks waiting for this stack to resolve first
                if goal > -1:
                    for j in range(i, goal - 1, -1):
                        top_dif = newtops[j] - self.tops[j]
                        for k in range(newtops[j], self.bots[j] + top_dif - 1, -1):
                            self.arr[k] = self.arr[k - top_dif]
                        self.tops[j] = newtops[j]
                        self.bots[j] = self.bots[j] + top_dif
                    goal = -1
                else:
                    top_dif = newtops[i] - self.tops[i]
                    for k in range(newtops[i], self.bots[i] + top_dif - 1, -1):
                        self.arr[k] = self.arr[k - top_dif]
                    self.tops[i] = newtops[i]
                    self.bots[i] = self.bots[i] + top_dif
            # the new top collides with an old bot
            else:
                # set the goal if it's not set
                if goal == -1:
                    goal = i
    
    def make_new_tops(self):
        newtops = [0] * self.stk_size
        stk_sizes = [0] * self.stk_size
        gaps = [0] * self.stk_size
        # initialize gaps to be the same as size of each stack
        for i in range(self.stk_size):
            cur_size = self.tops[i] - self.bots[i] + 1
            stk_sizes[i] = cur_size
            gaps[i] = max(cur_size, 1)
        # reduce gaps until the stacks and gaps all fit
        min_gaps = 0
        while(sum(stk_sizes) + sum(gaps) > self.arr_size):
            for i in range(self.stk_size):
                gaps[i] -= 1
                if gaps[i] < 1:
                    gaps[i] = 1
                    min_gaps += 1
                if min_gaps == self.stk_size:
                    raise(StackFull)
        newtops[0] = self.tops[0]
        for i in range(1, self.stk_size):
            newtops[i] = newtops[i-1] + gaps[i-1] + stk_sizes[i]
        return newtops