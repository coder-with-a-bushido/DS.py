class HashTable:

    def __init__(self, len=4):
        self.arr = [None]*len
        self._total_occupied = 0

    def _get_index(self, key):
        length = len(self.arr)
        return hash(key) % length

    def _is_full(self):
        is_full = self._total_occupied > (len(self.arr)*0.75)
        return is_full

    def _double(self):
        new_table = HashTable(len=len(self.arr)*2)
        for index in range(len(self.arr)):
            if self.arr[index] is not None:
                for kv_pair in self.arr[index]:
                    new_table.set_pair(key=kv_pair[0], val=kv_pair[1])
        self.arr = new_table.arr

    def set_pair(self, key, val):
        index = self._get_index(key=key)
        if(self.arr[index] is None):
            self.arr[index] = []
            self.arr[index].append([key, val])
            self._total_occupied += 1
        else:
            for kv_pair in self.arr[index]:
                if(kv_pair[0] == key):
                    kv_pair[1] = val
                    break
            else:
                self.arr[index].append([key, val])

        if(self._is_full()):
            self._double()

    def get_val(self, key):
        index = self._get_index(key=key)
        if(self.arr[index] is None):
            raise KeyError
        else:
            for kv_pair in self.arr[index]:
                if(kv_pair[0] == key):
                    return kv_pair[1]
            raise KeyError

    def __getitem__(self, key):
        return self.get_val(key=key)

    def __setitem__(self, key, val):
        return self.set_pair(key=key, val=val)

    def __len__(self):
        count = 0
        for index in range(len(self.arr)):
            if(self.arr[index] is not None):
                count += len(self.arr[index])
        return count


if(__name__ == '__main__'):
    map = HashTable()
    map['name1'] = 'val1'
    map['name2'] = 49087
    map[323] = 'bhjfeu'
    map['3kjdsb'] = '@#$%^&'
    map['height'] = 78.08
    print(map['name1'])
    print(map[323])
    print(map['height'])
    print(len(map))
