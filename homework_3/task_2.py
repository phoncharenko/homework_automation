
def second_item(*args):
    x = list(set(args))
    x.sort()
    return x[1]
