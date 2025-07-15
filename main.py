import pytest
import selene
import math
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





