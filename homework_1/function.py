
def repeat(s, exclaim):
    """

    :param s:
    :param exclaim:
    :return:
    """
    result = str(s * 3)
    if exclaim:
        result += '!!!'
        return result

r = repeat('123', True)
r = str(r)
print(r)