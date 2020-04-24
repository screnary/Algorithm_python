import pdb


def sort_and_print(chars_arr):
    res = ""
    counts = [0] * 256
    ascii_arr = [ord(c) for c in chars_arr]
    for i in range(len(chars_arr)):
        counts[ascii_arr[i]] += 1
    for i in range(256):
        if counts[i] > 1:
            res = res + chr(i)
            # pdb.set_trace()
    return res


def longest_repeat_char(chars_arr):
    len_str = len(chars_arr)
    if len_str < 2:
        return chars_arr
    # sliding window
    i = 0
    cur_char = chars_arr[0]
    cur_max = 1
    his_char = chars_arr[0]
    his_max = 1
    while i+1 < len_str:
        if chars_arr[i+1] == cur_char:
            cur_max += 1
            i += 1
        else:
            # update history_char and max
            if his_max < cur_max:
                his_char = cur_char
                his_max = cur_max
            elif his_max == cur_max and his_char > cur_char:
                his_char = cur_char
            # update chr_char and cur_max
            cur_char = chars_arr[i+1]
            cur_max = 1
            i += 1
    return his_char*his_max


if __name__ == '__main__':
    # chars_arr = input()
    # res = sort_and_print("ABCABCdd")
    res = longest_repeat_char("aaabbbbcccccccccczzzzzzzzzz")
    print(res)
