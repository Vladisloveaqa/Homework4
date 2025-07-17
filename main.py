import pytest
import selene
import math
import random
def test_greeting():
    a = "Владислав"
    age=26
    output = f"Привет,{a}! Тебе {age} лет."
    assert output == "Привет,Владислав! Тебе 26 лет."
    print(output)

def test_rectangle():
    a=10
    b=20
    perimetr= (a+b)*2
    area = a*b
    assert perimetr == 60
    assert area == 200

def test_circle():
    r=23
    area = math.pi*r**2
    length= 2 * math.pi * r
    assert area == 1661.9025137490005
    assert length == 144.51326206513048
    print(area, length)

import random

def test_random_list():
    l = [
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100),
        random.randint(1, 100)
    ]
    l.sort()
    assert isinstance(l, list)
    assert len(l) == 10
    assert all(1 <= num <= 100 for num in l)

def test_unique_elements():
    l=[1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l=list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = {
         first[0]:second[0],
         first[1]:second[1],
         first[2]:second[2],
         first[3]:second[3],
         first[4]:second[4]
         }

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second








