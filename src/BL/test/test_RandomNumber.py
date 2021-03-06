# third party modules
import pytest
# user modules
from BL_main.RandomNumber import Number, Numbers, InvalidArgumentExceptionOfNumber
def test_NumberClass_InvalidException_underNumber():
    '''
    Test argument. under number.
    '''
    with pytest.raises(InvalidArgumentExceptionOfNumber):
        Number.create(1)
    Number.create(2)
def test_NumberClass_InvalidException_overNumber():
    '''
    Test argument. over number.
    '''
    with pytest.raises(InvalidArgumentExceptionOfNumber):
        Number.create(100)
    Number.create(99)
def test_NumberClass_CreateTargetNumber():
    '''
    Test NumberClass initialize. 
    '''
    actual = Number.create(3)
    assert actual.value == 3
    
    actual2 = Number.create(3)
    assert actual == actual2

    actual3 = Number.create(4)
    assert actual != actual3

def test_NumbersClass():
    '''
    Test NumbersClass initialize
    '''
    numbers = Numbers.create()
    count = 0
    while(not numbers.EOF):
        count += 1
        numbers.pop()
      
    # Can getting 98 Values
    actual = 98
    assert actual == count
    