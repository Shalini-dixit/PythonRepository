class Dictionary_Iterator:

    def __init__(self, dict : {}):
        self.dict = dict
        self.dict_list = list(dict)
        self.pos=0
        
    def __itr__(self):
        return self

    def __next__(self):
        if self.pos>= len(self.dict_list):
            StopIteration()
            return
        key = self.dict_list[self.pos]
        value = self.dict[key]
        pair = "( {},'{}')".format(key,value)
        self.pos+=1
        return pair

    def dict_iter(self):
        pass
        
d = Dictionary_Iterator({"one": "1", 2: "2"})
print(next(d))
print(next(d))
print(next(d))