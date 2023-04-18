class FlatIterator:

    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.main_cursor = 0
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor +=1

        if  self.cursor > len(self.main_list[self.main_cursor])-1:
            self.main_cursor += 1
            self.cursor = 0

        if self.main_cursor > len(self.main_list)-1:
            raise StopIteration

        return self.main_list[self.main_cursor][self.cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    for i in FlatIterator(list_of_lists_1):
        print(i)

if __name__ == '__main__':
    test_1()