import time


def calculate_time(f):
    def wrap():
        time_i= time.time()
        f()
        time_f = time.time()
        print("Total time " + str(time_f - time_i))

    return wrap


@calculate_time
def print_smthng():
    print("hey")


print_smthng()
