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
class Numbers:
    '''
    Number First Class Collection
    '''
    def create():
        '''
        Standard Factory
        '''
        return Numbers()
    def __init__(self):
        '''
        Constractor
        '''
        self._numbers = []
        self.EOF = False
        self._currentIdx = 0
        self._numbers = self._createNumbers()
    def _createNumbers(self):
        '''
        initial numbers creater
        @returns
        ---------
        initial numbers instance.
        '''
        numbers = []
        for i in range(98):
            numbers.append(Number.create(i + 2))
        return numbers
    def pop(self):
        '''
        pop out number.
        @returns
        --------
        poped number object.
        '''
        self._currentIdx += 1
        self._check_EOF()
        return self._numbers[self._currentIdx - 1]
    def _check_EOF(self):
        '''
        Set EOF To True, if _currentIdx exceeds max numbers(98)
        '''
        if 98 <= self._currentIdx:
            self.EOF = True
#Exceptions
class InvalidArgumentExceptionOfNumber(Exception):
    pass