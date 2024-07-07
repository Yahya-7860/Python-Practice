import time


def timeChecking(func):
    def wrapper():
        a = time.time()
        func()
        b = time.time()
        print(f"{b-a} time taken to complete")
    return wrapper


@timeChecking
def func():
    time.sleep(2)
    print("Function Chal Gaya")


func()
