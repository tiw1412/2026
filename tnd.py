from time import time, sleep

def timer(func):
    def wrapper():
        first_time = time()
        func()
        # sleep(2)
        second_time = time()
        exit_time = second_time - first_time
        print(exit_time)
    return wrapper

@timer
def just_print():
    print('just_')

just_print()

def dec(count):
     def repeat(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)
        return wrapper
     return repeat

@dec(3)
def larprinter():
    print('3')

larprinter()