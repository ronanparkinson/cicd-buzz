import unittest
import sys
sys.path.append('../')
from buzz import generator
from buzz import div
from buzz import multi
from buzz import sub

def test_addition():
    sum = generator.addition(4, 5)
    print(sum)
    assert sum == 9
    
def test_div():
    sum = div.div(4, 2)
    print(sum)
    assert sum == 2
    
def test_multi():
    sum = multi.multi(3, 4)
    print(sum)
    assert sum == 12
    
def test_sub():
    sum = sub.sub(4, 1)
    print(sum)
    assert sum == 3