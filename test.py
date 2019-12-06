#简单测试
#%%
[x * x for x in range(0, 10)]


#%%
def triangles(n):
    L = [1]
    tem = 0
    while (tem < n):
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
        tem = tem + 1


s = triangles(6)
for i in s:
    print(i)

#%%
from functools import reduce


#%%
def fun(x):
    return x * x


def sum(x, y):
    return x + y


l = map(fun, [1, 2, 3])
[x for x in l]

#%%
reduce(sum, [1, 2, 3])


#%%
def is_odd(x):
    return x % 2 == 1


l = filter(is_odd, [1, 2, 3, 4, 5, 6])
[x for x in l]


#%%
def fun(x):
    l = list(range(2, x))
    i = 0
    while i < len(l):
        j = i + 1
        while j < len(l):
            if l[j] % l[i] == 0:
                l.remove(l[j])
                j = j - 1
            j = j + 1
        i = i + 1
    return l


fun(100)


#%%
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n != 0


def primes_1():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes_1():
    if n < 1000:
        print(n)
    else:
        break
#%%


def fun(x):
    def fun1(a):
        return a % x == 0

    return fun1


l = filter(fun(3), [1, 2, 3, 4, 5, 6])

[x for x in l]

#%%
l = [3, -2, 9, 6, -1, 0]
sorted(l)


def fun(x):
    return -x


import numpy as np

sorted(l, key=fun, reverse=True)


def fun1(x):
    return x[1]


l = [('xiaoming', 90), ('xiaohong', 96), ('xiaolan', 91)]
sorted(l)
sorted(l, key=fun1)


#%%
def fun(*args):
    def fun1():
        n = 0
        for x in args:
            n = n + x
        return n

    return fun1


fun(1, 2, 3)


#%%
def fun():
    l = []
    for i in range(1, 4):

        def f():
            j = i * i
            return j

        l.append(f)
    return l


f1, f2, f3 = fun()
f1()

#%%
l = map(lambda x: x * x, [1, 2, 3])
list(l)

#%%


def log(func):
    def fun(*args, **agrs1):
        print('funciton:%s' % func.__name__)
        return func(*args, **agrs1)

    return fun


@log
def now():
    print('2019-10-01')


now()
#%%

int('123')
i = int('123', base=16)
print(i)
print(bin(123))
import functools
int2 = functools.partial(int, base=2)
int2('100')
#%%

#命令行运行，加参数
'a test on module'
import sys


def fun():
    args = sys.argv
    if len(args) == 1:
        print('hello,world')
    elif len(args) == 2:
        print('hello,%s' % args[1])
    else:
        print('too many argments')


fun()
l = sys.argv
for i in l:
    print(i)


#%%
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))


stu1 = Student('xiaoming', 90)
stu2 = Student('xiaohong', 95)
stu1.print_score()
stu2.print_score()


# %%
class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))


stu1 = Student('xiaoming', 90)
stu1._Student__score = 95
stu1.print_score()
print(stu1._Student__name)
print(hasattr(stu1, 'name'))
getattr(stu1, 'name')


# %%
class Animal():
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def fun1(self):
        print('this is a dog...')


animal1 = Animal()
animal2 = Dog()
animal1.run()
animal2.run()
animal2.fun1()

print(type(animal1), '***')
print(isinstance(animal1, Animal))
print(isinstance(animal2, Animal))
print(dir(Animal))
print(hasattr(animal1, 'name'))
print(hasattr(animal1, 'run'))
print(hasattr(stu1, 'name'))


# getattr(stu1,'name')
# %%
class Student():
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


stu1 = Student('xiaoming')
stu2 = Student('xiaohong')
print(stu1.count)


# %%
class Student():
    __slots__ = ('name', 'age')


stu1 = Student()
stu1.name = 'xiaoming'
print(stu1.name)

# print(stu1.age)
# stu1.score=90


# %%
class Student():
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, age):
        if age < 100 and age > 0:
            self._score = age


stu1 = Student()
stu1.score = 90
print(stu1.score)

# %%
