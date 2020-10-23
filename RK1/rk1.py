# используется для сортировки
from operator import itemgetter


class Constr:
    """Синтаксическая конструкция"""

    def __init__(self, id, name, size, lang_id):
        self.id = id
        self.name = name
        self.size = size
        self.lang_id = lang_id


class Lang:
    """Язык программирования"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ConstrLang:
    """Конструкции языка программирования"""

    def __init__(self, lang_id, constr_id):
        self.lang_id = lang_id
        self.constr_id = constr_id


# Языки программирования
langs = [
    Lang(1, 'Python'),
    Lang(2, 'Java'),
    Lang(3, 'C++'),

    Lang(4, 'Basic'),
    Lang(5, 'Fortran'),
    Lang(6, 'Pascal'),
]

# Синтаксичнские конструкции
constrs = [
    Constr(1, 'A1 конструкция', 10, 1),
    Constr(2, 'B1 конструкция', 30, 2),
    Constr(3, 'A2 конструкция', 10, 2),
    Constr(4, 'A3 конструкция', 25, 3),
    Constr(5, 'B2 конструкция', 10, 3),
    Constr(6, 'D1 конструкция', 15, 3),
]

langs_constrs = [
    ConstrLang(1, 1),
    ConstrLang(2, 2),
    ConstrLang(2, 3),
    ConstrLang(3, 4),
    ConstrLang(3, 5),
    ConstrLang(3, 6),

    ConstrLang(4, 1),
    ConstrLang(4, 2),
    ConstrLang(4, 3),
    ConstrLang(5, 4),
    ConstrLang(6, 1),
    ConstrLang(6, 5),
    ConstrLang(6, 6),
]


def main():

    one_to_many = [
        (c.name, c.size, l.name)
        for l in langs
        for c in constrs
        if c.lang_id == l.id
    ]

    many_to_many_temp = [
        (l.name, cl.lang_id, cl.constr_id)
        for l in langs
        for cl in langs_constrs
        if l.id == cl.lang_id
    ]

    many_to_many = [
        (c.name, lang_name)
        for lang_name, lang_id, constr_id in many_to_many_temp
        for c in constrs
        if c.id == constr_id
    ]

    print('\nЗадание 1')
    result_1 = list(filter(lambda i: i[0][0] == 'B', one_to_many))
    print(result_1)

    print('\nЗадание 2')
    result_2_unsorted = []

    for l in langs:
        constrs_of_lang = list(filter(lambda i: i[2] == l.name, one_to_many))
        if len(constrs_of_lang) > 0:
            constr_sizes = [size for _, size, _ in constrs_of_lang]
            constr_sizes_max = max(constr_sizes)
            result_2_unsorted.append((l.name, constr_sizes_max))

    result_2 = sorted(result_2_unsorted, key=itemgetter(1), reverse=True)
    print(result_2)

    print('\nЗадание 3')
    result_3 = sorted(many_to_many, key=itemgetter(0))
    print(result_3)

if __name__ == '__main__':
    main()
