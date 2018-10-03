

def song(strings=3, counts=3, end_song=0):
    one_string = 'la-' * counts
    if len(one_string) > 0:
        one_string = one_string[:-1]
    result = ("." if end_song == 0 else "!")
    one_string = one_string + result + "\n"
    return one_string * strings

print(song(3, 0, 1))
