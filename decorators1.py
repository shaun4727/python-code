def start_end_decorator(func):
    def wrapper(*args,**kwargs):
        print('Start')
        val = func(*args,**kwargs)
        print('End')
        return val
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# print_name = start_end_decorator(print_name)

@start_end_decorator
def func(x):
    return x+5

print(func(10))
# print_name()