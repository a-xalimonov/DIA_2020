import json
import sys

from cm_timer import cm_timer_1
from print_result import print_result
from unique import unique
from field import field
from gen_random import gen_random

path = "C:/RIP_2020/Lab3/lab_python_fp/data_light.json"

with open(path, encoding='utf8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(unique(field(arg, 'job-name'), ignore_case=True)))


@print_result
def f2(arg):
    return list(filter(lambda a: a.startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda a: a + " с опытом Python", arg))


@print_result
def f4(arg):
    return list('{}, зарплата {} руб'.format(job_name, salary) for job_name, salary in zip(arg, gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))