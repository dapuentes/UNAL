class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        hash_value = 5381
        for char in key:
            hash_value = (hash_value * 33) ^ ord(char)
        return hash_value

    def set_item(self, key, value):
        index = self._hash(key) % self.size
        while self.table[index]:
            if self.table[index][0] == False:
                break
            if self.table[index][0] == key:
                self.table[index][1].append(value)
                return
            index = (index + 1) % self.size
        self.table[index] = [key, [value]]

    def get_item(self, key):
        index = self._hash(key) % self.size
        while self.table[index]:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def remove_item(self, key):
        index = self._hash(key) % self.size
        while self.table[index]:
            if self.table[index][0] == key:
                self.table[index] = [False, []]
                return
            index = (index + 1) % self.size
        return None

    def keys(self):
        all_keys = []
        for i in range(self.size):
            if self.table[i]:
                all_keys.append(self.table[i][0])
        return all_keys

    def print_table(self):
        types = []
        aux = 0

        for _, val in enumerate(self.table):
            if val:
                type_name = val[0]
                pokemon = val[1]

                if type_name not in types:
                    types.append(type_name)
                    print("tipo", type_name, ":")

                for poke in pokemon:
                    print(poke)

                aux = max(aux, len(pokemon))
                print("\n")

        
        aux_type = None
        aux_count = 0
        for _, val in enumerate(self.table):
            if val and len(val[1]) == aux:
                aux_type = val[0]
                aux_count = len(val[1])
                break

        print("El tipo con mayor número de Pokemon es", aux_type, "con", aux_count, "Pokemon")


# Ejemplo de uso
hash_table = HashTable(10)

n = int(input())  

for _ in range(n):
    a = input().split("-")
    b = a[0]
    c = a[1]
    d = a[2]
    hash_table.set_item(d, f"{c}:{b}")

hash_table.print_table()
