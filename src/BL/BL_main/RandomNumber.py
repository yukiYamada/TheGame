class Number:
    '''
    Number Class.
    '''
    def create(number):
        '''
        Number Class Basic Factory.
        '''
        if (number > 99) :
            raise InvalidArgumentExceptionOfNumber("over number")
        if (number < 2):
            raise InvalidArgumentExceptionOfNumber("under number")
        return Number(number)   
    def __init__(self, number):
        '''
        Constractor.
        '''
        self.value = number
    def __eq__(self, other):
        '''
        Override Equals.
        '''
        if not isinstance(other, Number):
            return NotImplemented
        return self.value == other.value

class InvalidArgumentExceptionOfNumber(Exception):
    pass
