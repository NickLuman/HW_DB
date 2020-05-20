from hash_functions import *


class Hash(object):
    def __init__(self, size=10, _filling_coe=0.6, _extension_coe=1.5 ):
        self.current_size = size
        self.keys = [None] * self.current_size
        self.values = [None] * self.current_size

        self.start_size = size 

        self.filling_coe = _filling_coe
        self.extension_coe = _extension_coe

        self.tomb_stone = '0x10101010-XX-XX-ERR'


    def put(self, key, value):
        pos = hasher(key, self.current_size)

        while self.keys[pos] != None and self.keys[pos] != key and self.keys[pos] != self.tomb_stone:
            pos = rehasher(pos, self.current_size)
        
        if self.keys[pos] == None or self.keys[pos] == self.tomb_stone:
            self.keys[pos] = key
            self.values[pos] = value
        else: 
            self.values[pos] = value

        if self.filling_checker():
            self.fitter()
       
       
    def get(self, key):
        start = hasher(key, self.current_size)
        pos = start
    
        while self.keys[pos] != None:
            if self.keys[pos] == key:
                return self.values[pos]
            else: 
                pos = rehasher(pos, self.current_size)
                if pos == start:
                    return None
        return None


    def delete(self, key):
        if self.keys.count(key) == 0:
            return

        pos = self.keys.index(key)

        self.keys[pos] = self.tomb_stone
        self.values[pos] = self.tomb_stone


    def filling_checker(self) -> bool:
        flag = False
        if self.keys.count(None) + self.keys.count(self.tomb_stone) \
             < self.current_size * self.filling_coe:
            flag = True
        return flag
        

    def fitter(self):
        self.current_size = int(self.current_size * self.extension_coe) 
                
        new_hash = Hash(size=self.current_size)

        for i in range(len(self.keys)):
            if self.keys[i] != None and self.keys[i] != self.tomb_stone:
                new_hash.put(self.keys[i], self.values[i])

        self.keys = new_hash.keys
        self.values = new_hash.values


    def __getitem__(self, key):
        return self.get(key)


    def __setitem__(self, key, value):
        self.put(key, value)
    
 
