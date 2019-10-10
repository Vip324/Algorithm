import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс для внутренних узлов, у них есть потомки
    def go_to(self, code, acc):
        self.left.go_to(code, acc + "0")
        self.right.go_to(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев, у них нет потомков, но есть значение символа
    def go_to(self, code, acc):
        code[self.char] = acc or "0"


def alg_huff(s):  # алгоритм Хаффмана
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    # print(h)

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1
    # print(h)

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.go_to(code, "")

    return code


my_str = input('Введите строку прописными английскими буквами : ')
print()
print(f'Ваша строка в двоичной кодировке имеет вид :')
print("".join(f'{ord(ch):b}' for ch in s))
print()

code_dict = alg_huff(my_str)

encoded = "".join(code_dict[ch] for ch in s)
print(f'Строка закодированная алгоритмом Хаффмана имеет вид :')
print(encoded)
