"""Закодируйте любую строку из трех слов по алгоритму Хаффмана."""
from collections import Counter
a = 'life python apple'

class Haffm_tr:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def inputs_data(n):
    strings = Counter(n)

    if len(strings) <= 1:
        node = Haffm_tr(None)

        if len(strings) == 1:
            node.left = Haffm_tr([key for key in strings][0])
            node.right = Haffm_tr(None)

        strings = {node: 1}

    while len(strings) != 1:
        my_tree = Haffm_tr(None)
        now = strings.most_common()[:-3:-1]

        if isinstance(now[0][0], str):
            my_tree.left = Haffm_tr(now[0][0])

        else:
            my_tree.left = now[0][0]

        if isinstance(now[1][0], str):
            my_tree.right = Haffm_tr(now[1][0])

        else:
            my_tree.right = now[1][0]

        del strings[now[0][0]]
        del strings[now[1][0]]
        strings[my_tree] = now[0][1] + now[1][1]

    return [i for i in strings][0]




def user(first, coding=dict(), code=''):

    if first is None:
        return

    if isinstance(first.value, str):
        coding[first.value] = code
        return coding

    user(first.left, coding, code + '0')
    user(first.right, coding, code + '1')

    return coding



prob =''
test = inputs_data(a)

encode = user(test)
print(a)
print(encode)
c = "".join(encode[i]  for i in a)
print(c)


