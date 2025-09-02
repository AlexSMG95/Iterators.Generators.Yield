import types


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_idx = 0
        self.inner_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Если внешний индекс вышел за пределы — конец итерации
        if self.outer_idx >= len(self.list_of_list):
            raise StopIteration

        # Текущий элемент
        current_list = self.list_of_list[self.outer_idx]

        # Если внутренний индекс вышел за пределы, переходим к следующему списку
        if self.inner_idx >= len(current_list):
            self.outer_idx += 1
            self.inner_idx = 0
            return self.__next__()

        item = current_list[self.inner_idx]
        self.inner_idx += 1
        return item

def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print("test_1 OK")


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print("test_2 OK")

if __name__ == '__main__':
    test_1()
    test_2()