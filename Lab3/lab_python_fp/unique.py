from gen_random import gen_random

class unique(object):
    def __init__(self, items, **kwargs):

        self.unique_list = []
        self.items = iter(items)
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):

        item = self.items.__next__()
        if type(item) is str and self.ignore_case:
            item = item.lower()
        if item in self.unique_list:
            return self.__next__()
        else:
            self.unique_list.append(item)
            return item

    def __iter__(self):
        return self

if __name__ == '__main__':
    data = ['A', 'a', 'a', 'A', 'C', 'B', 'b', 'c']

    for i in unique(data, ignore_case = "True"):
        print(i)