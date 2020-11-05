def print_result(func, *args):
    def dec(args):
        print(func.__name__)
        func_result = func(args)
        if type(func_result) is list:
            for i in func_result:
                print(i)
        elif type(func_result) is dict:
            for name, value in func_result.items():
                print('{} = {}'.format(name, value))
        else:
            print (func_result)
        return func_result
    return dec


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()