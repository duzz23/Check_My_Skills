class L:
    def __init__(self, values):
        self.v = values

    def __iter__(self):
        print("Интопритатор")
        self.i = 0
        return self

    def __next__(self):
        print('Next')
        if self.i == len(self.v):
            raise StopIteration
        else:
            self.i += 1
            return self.v[self.i -1]

print('***' * 20)
s = L([1,2,3,4])
for i in s:
    print(i)
