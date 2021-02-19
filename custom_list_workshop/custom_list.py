from typing import List, Dict


class CustomListException(Exception):
    pass


class CustomList:
    def __init__(self, *args):
        self.sequence = list(args)

    def append(self, value) -> List:
        self.sequence += [value]
        return self.sequence

    def remove(self, index):
        try:
            value = self.sequence[index]
            del self.sequence[index]
            return value
        except IndexError:
            raise CustomListException('Custom List does not found element on given index')
        except TypeError:
            raise CustomListException('Wrong type index, must be Integer')

    def get(self, index):
        try:
            value = self.sequence[index]
            return value
        except IndexError:
            raise CustomListException('Custom List does not found element on given index')
        except TypeError:
            raise CustomListException('Wrong type index, must be Integer')

    def extend(self, iterable) -> List:
        try:
            self.sequence += list(iterable)
            return self.sequence
        except TypeError:
            raise CustomListException('Given value must be iterable')

    def insert(self, index, value) -> List:
        if isinstance(index, int) and index >= len(self.sequence):
            raise CustomListException('Custom List does not found element on given index')

        try:
            rest_of_list = self.sequence[index:]
            self.sequence = self.sequence[:index]
            self.sequence += [value]
            self.sequence += list(rest_of_list)
            return self.sequence
        except TypeError:
            raise CustomListException('Wrong type index, must be Integer')

    def pop(self):
        if not self.sequence:
            raise CustomListException('you can not pop from empty list')
        value = self.sequence[-1]
        del self.sequence[-1]
        return value

    def clear(self) -> None:
        self.sequence = []

    def index(self, value) -> int:
        if value not in map(lambda x: x, self.sequence):
            raise CustomListException('Value not in list')

        for i, val in enumerate(self.sequence):
            if val == value:
                return i

    def count(self, value) -> int:
        if value not in map(lambda x: x, self.sequence):
            return 0
        result = [v for v in self.sequence if v == value]
        return len(result)

    def reverse(self) -> None:
        self.sequence = self.sequence[::-1]

    def copy(self):
        result = [el for el in self.sequence]
        return CustomList(*result)

    def size(self) -> int:
        return len(self.sequence)

    def add_first(self, value) -> None:
        self.sequence = [value] + self.sequence

    def dictionize(self) -> Dict:
        if len(self.sequence) == 0:
            return {}
        if len(self.sequence) % 2 != 0:
            self.sequence.append('')

        keys = [self.sequence[i] for i in range(len(self.sequence)) if i % 2 == 0]
        values = [self.sequence[i] for i in range(len(self.sequence)) if i % 2 != 0]
        return dict(zip(keys, values))

    def move(self, amount) -> List:
        try:
            self.sequence = self.sequence[amount:] + self.sequence[:amount]
            return self.sequence
        except TypeError:
            raise CustomListException('Wrong type index, must be Integer')

    def sum(self) -> int:
        types = (int, float)
        result = 0
        for el in self.sequence:
            if type(el) in types:
                result += el
            else:
                result += len(str(el))

        return result

    def overbound(self) -> int:
        types = (int, float)
        biggest_el = -999999999999999999999999
        idx = 0
        for i, el in enumerate(self.sequence):
            if type(el) in types and el > biggest_el:
                biggest_el = el
                idx = i
            else:
                if len(str(el)) > biggest_el:
                    biggest_el = len(str(el))
                    idx = i
        return idx

    def underbound(self) -> int:
        types = (int, float)
        biggest_el = 999999999999999999999999
        idx = 0
        for i, el in enumerate(self.sequence):
            if type(el) in types and el < biggest_el:
                biggest_el = el
                idx = i
            else:
                if len(str(el)) < biggest_el:
                    biggest_el = len(str(el))
                    idx = i
        return idx

    def __repr__(self):
        return f'{self.sequence}'

    def __str__(self):
        return f'{" ".join(map(str, self.sequence))}'

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        return self.sequence[index]

    def __setitem__(self, index, value):
        self.sequence[index] = value
