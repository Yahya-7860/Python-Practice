def shamin(func):
    def wrapper(*args, **kwarg):
        print(f'{func.__name__}')
        func(*args, **kwarg)
        for arg in args:
            print(arg)
    return wrapper

@shamin
def yahya(a, b):
    print(f'Name : {a}, Surname : {b}')

yahya("taimoor", "raza")
