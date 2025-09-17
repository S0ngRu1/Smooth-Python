# -*- coding: utf-8 -*-
# @Time : 2024/9/27 23:20
# @Author : CSR
# @File : 1-1 一摞有序的纸牌.py

import collections
from random import choice

#collections：这是Python标准库中的一个模块，提供了许多有用的容器类型，比如deque、Counter、OrderedDict等。
# namedtuple：用以构建只有少数属性但没有方法的对象，命名元组允许你通过属性名称来访问元组中的元素，而不是通过索引。
# 'Card'：这是命名元组的名称，它将作为返回的类的名称。['rank', 'suit']：这是一个字符串列表，定义了命名元组中的字段名称。在这个例子中，每个Card对象将有两个属性：rank和suit

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    #  __getitem__ 方法提供 提取 元素 的功能： deck[0]
    def __getitem__(self, item):
        return self._cards[item]

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print(choice(deck))
    print(deck[:3])
    print(deck[12::13])

    #仅仅实现了 __getitem__ 方法，这一摞牌就变成可迭代的了
    # in 运算符会按顺序做一次迭代搜索
    for card in deck:
        print(card)

    # 反向迭代
    for card in reversed(deck):
        print(card)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    for card in sorted(deck, key=spades_high):
        print(card)
