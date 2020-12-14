def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for item in items:
            if args[0] in item:
                yield item[args[0]]
    else:
        for item in items:
            new_item = {}
            for arg in args:
                if arg in item:
                    new_item[arg] = item[arg]
            yield new_item


if __name__ == '__main__':

    goods = [
       {'title': 'Ковер', 'price': 2000, 'color': 'green'},
       {'title': 'Диван', 'price': 5300, 'color': 'black'},
       {'title': 'Шторы', 'price': 1500, 'color': 'crimson'},
    ]

    print(list(field(goods)))
