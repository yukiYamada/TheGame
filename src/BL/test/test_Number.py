#third
import pytest
#user
from BL_main.Number import *

def test_Number_InvalidException_underNumber():
    """
    Test argument. under number.
    """
    with pytest.raises(InvalidArgumentExceptionOfNumber):
        dummy = Number.create(1)
    dummy = Number.create(2)
def test_Number_InvalidException_overNumber():
    """
    Test argument. over number.
    """
    with pytest.raises(InvalidArgumentExceptionOfNumber):
        dummy = Number.create(100)
    dummy = Number.create(99)

