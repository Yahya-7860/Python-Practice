def greet(func):
    def wrapper():
        print("Bich Wale function ke upar")
        func()
        print("Bich Wale function ke niche")
    return wrapper


@greet
def add():
    print('Bich Wala Function')


add()
