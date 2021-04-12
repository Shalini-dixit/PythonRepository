class Dictionary_Iterator:

    def __init__(self, dict : {}):
        self.dict = dict
        self.dict_list = list(dict)
        self.pos=0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.pos>= len(self.dict_list):
           raise StopIteration
        key = self.dict_list[self.pos]
        value = self.dict[key]
        pair = "( {},'{}')".format(key,value)
        self.pos+=1
        return pair

        
iterator = Dictionary_Iterator({"one": "1", 2: "2"})

for pair in iterator:
    print(pair)