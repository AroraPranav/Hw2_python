def func_counter(func):
    def wrap(*args, **kwargs):
        wrap.counter += 1
        return func(*args, **kwargs)
    wrap.counter = 0
    return wrap
