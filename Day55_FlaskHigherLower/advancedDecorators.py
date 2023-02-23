
def sum_dec(function):
    def wrapper(*args):
        print(f"You called {function.__name__} ({args})")
        result = 0
        for item in args:
            result +=item
        print(f"It returned: {result}")   
    return wrapper

@sum_dec
def a_function(*args):
    print(None)

a_function(1,2,3)