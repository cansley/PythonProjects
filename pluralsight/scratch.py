
class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

    def getList(self):
        return list(range(self.n))

    def buildList(self):
        val = []
        int = 0
        while int < self.n:
            val.append(int)
            int += 1

        return val