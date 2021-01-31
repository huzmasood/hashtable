class HashTable:
    def __init__(self, size=9973):
        self.size = size
        self.array = [[] for i in range(self.size)]
        self.itemlst = []

    def __hashed(self, key):
        hash = ''
        for i in str(key):
            hash += str(ord(i) - 22)
        return int(hash) % self.size

    def __setitem__(self, key, value):
        flag = True
        for i in self.array[self.__hashed(key)]:
            if i[0] == key:
                x = i[1]
                i[1] = value
                flag = False
                self.itemlst.remove((key, x))
                self.itemlst.append((key, value))
        if flag == True:
            self.array[self.__hashed(key)].append([key, value])
            self.itemlst.append((key, value))

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.pop(key)

    def get(self, key):
        for i in self.array[self.__hashed(key)]:
            if i[0] == key:
                return i[1]
        raise KeyError(key)

    def pop(self, key):
        for i in self.array[self.__hashed(key)]:
            if i[0] == key:
                self.itemlst.remove((key, self.get(key)))
                self.array[self.__hashed(key)].remove(i)
                return
        raise KeyError(key)

    def clear(self):
        self.array = [[] for i in range(self.size)]
        self.itemlst = []

    def items(self):
        return f"hashtable_items({self.itemlst})"

    def keys(self):
        keylst = []
        for i in self.itemlst:
            keylst.append(i[0])
        return f"hashtable_keys({keylst})"

    def values(self):
        valuelst = []
        for i in self.itemlst:
            valuelst.append(i[1])
        return f"hashtable_values({valuelst})"