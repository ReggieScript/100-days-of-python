import time


def time_management(function):
    def warp_fun():
        before = time.time()
        function()
        after = time.time()
        time_elapsed = after - before
        print(f"The function took {time_elapsed} seconds!")
    return warp_fun

@time_management
def fast():
    time.sleep(2)
    print("I have awoken!")

@time_management
def slow():
    time.sleep(60)
    print("*yawn*")

fast()
slow()