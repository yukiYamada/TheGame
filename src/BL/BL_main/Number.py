class Number:
    def create(number):
        if (number > 99) :
            raise InvalidArgumentExceptionOfNumber("over number")
        if (number < 2):
            raise InvalidArgumentExceptionOfNumber("under number")
        return ""

class InvalidArgumentExceptionOfNumber(Exception):
    pass
