class CountdownIterartor():

    def __init__(self, count):
        self.count = count
        self.state = count
    def __iter__(self):
        return self

    def __next__(self):
        current = self.state
        if current <0:
            raise StopIteration
        self.state -=1
        return current

    def return_value(self):
        lst=[]
        n=0
        while True:
            try:
                lst.append(next(self))
                n+=1
            except StopIteration:
                return lst
        


c = CountdownIterartor(10)
nums = c.return_value()


for num in nums:
    print(num)