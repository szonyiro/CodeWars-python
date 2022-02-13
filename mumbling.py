# s = "ZpglnRxqenU"
#
# 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnn-Uuuuuuuuuuu'
# should equal
# 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu'


def accum(s):
    new_s = []
    for count, char in enumerate(s):
        new_s.append((char) * (count + 1))
        for i in range(len(new_s)):
            new_s[i] = new_s[i].capitalize()
    return "-".join(new_s)


# print(accum(s))
