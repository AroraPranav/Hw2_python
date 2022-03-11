# doubler
def doubler(n):
    def wrap():
        n()
        n()

    return wrap
