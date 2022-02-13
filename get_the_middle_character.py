"""You are going to be given a word. Your
job is to return the middle character of
the word. If the word's length is odd, return
the middle character. If the word's length
is even, return the middle 2 characters."""

def get_middle(s):
    str_len = len(s)
    if str_len % 2 > 0:
        pos = int(str_len / 2)
        return s[pos]
    if str_len % 2 == 0:
        pos1 = int((str_len / 2 - 1))
        pos2 = int((str_len / 2 + 1))
        return s[pos1: pos2]
    else:
        return s


print(get_middle("abcd"))
print(get_middle("abcdf"))