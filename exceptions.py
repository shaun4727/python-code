x = 5
assert (x>=0), 'x is not positive'

y = 4
if y < 0:
    raise Exception('x should be positive')

# try catch
try:
    a = 5 + '10'
except Exception as e:
    print(e)


# custom class
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x<2:
        raise ValueTooSmallError('Value is small',x)    

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message,e.value)
