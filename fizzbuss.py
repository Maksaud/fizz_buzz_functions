


def check_num(num, mod):
    return num % mod == 0


def check_if_buzz(temp_num, num):
    if check_num(num, 5) and check_num(num, 3):
        return ('boringbuzz', num)
    elif check_num(num, 3):
        return ('buzz', num)
    elif check_num(num, 5):
        return ('boring', num)
    else:
        return num




