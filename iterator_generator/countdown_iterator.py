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

iterator = CountdownIterartor(10)

for num in iterator:
    print(num, end=" ")