class TakeSkip:

    def __init__(self,step,count):
        self.step = step
        self.count = count
        self.counter = 0 

    def __iter__(self):
        return self

    def __next__(self):
        current = self.counter*self.step
        if self.counter>= self.count:
            raise StopIteration
        self.counter +=1
        return current 

nums = TakeSkip(2,6)

for num in nums:
    print(num)