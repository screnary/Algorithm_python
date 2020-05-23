import sys

def main():
    # input processing
    in_list = []
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        in_list.append(line)
    splitter = in_list.pop(0)
    n_node = len(in_list)

    res = []
    tmp = []
    isValid = True
    for i in range(n_node):
        idx, name = in_list[i].split(',')
        if not idx.isdigit():
            isValid = False
        if name == splitter:
            if len(tmp) != 0:
                res.append(tmp)
                tmp = []
            continue
        tmp.append(in_list[i])
    if tmp:
        res.append(tmp)
    n_group = len(res)
    if isValid:
        print(n_group)
        for i in range(n_group):
            if len(res[i]) == 1:
                print(res[i])
            else:
                print("|".join(res[i]))
    else:
        print(0)


# if __name__ == '__main__':
#     inlist = ['*',
#             "1,name1",
#             "2,name2",
#             "3,*",
#             "4,name4",
#             "5,name5"]
