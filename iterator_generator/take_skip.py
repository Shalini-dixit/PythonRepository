class TakeSkip:

    def __init__(self,step,count):
        self.step = step
        self.count = count
        self.counter = 0 

    def __iter__(self):
        return self

    def __next__(self):
        current = self.counter*self.step
        self.counter +=1
        return current 

    def take_skip(self):
        skip_list = []
        n=0
        while n<self.count:
            skip_list.append(next(self))
            n+=1
        return skip_list

nums = TakeSkip(2,6).take_skip()

for num in nums:
    print(num)