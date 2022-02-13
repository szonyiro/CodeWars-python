# s = "ZpglnRxqenU"
# 
# Sample 
# 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnn-Uuuuuuuuuuu'
# should equal
# 'Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu'


def accum(s):
    new_s = []  # creares new list
    for count, char in enumerate(s):  # gets the index for ech letter from sting
        new_s.append(char * (count + 1))  # appends to new list each letter multiplied by its index
        for i in range(len(new_s)):  # loop through the new_s list and capitalize the first letter of each element
            new_s[i] = new_s[i].capitalize()
    return "-".join(new_s)  # joins each element into 1 string, separated by - character


# print(accum(s))
