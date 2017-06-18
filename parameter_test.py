#coding:utf-8

class Person(object):
    def __new__(cls, *args, **kwargs):
        print 'test new'

    def __init__(self, name):
        self.name = name
        print 'test init'


def test_dict():
    items = [('name', 'earth'), ('port', '80')]
    print dict(items)
    print dict((['name', 'earth'], ['port', '80']))
    dict1 = {}.fromkeys(('x', 'y'), -1)
    dict2 = {}.fromkeys(('x', 'y'))
    print 'dict1: ', dict1
    print 'dict2: ', dict2
    pass


def test_merge_list(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return test_merge_list(l1, l2, tmp)


def binarysearch(lis, value):
    low, high = 0, len(lis)-1
    while low < high:
        print low, high
        mid = (low + high)/2
        if lis[mid] > value:
            high = mid
        elif lis[mid] < value:
            low = mid + 1
        else:
            return mid
    print 'value not in list.'


def  coinChange(values, money, coinsUsed):
    #values    T[1:n]数组
    #valuesCounts   钱币对应的种类数
    #money  找出来的总钱数
    #coinsUsed   对应于目前钱币总数i所使用的硬币数目
    # for cents in range(1, money+1): # money=63





        minCoins = 63     #从第一个开始到money的所有情况初始   63
        for value in values:#[ 25, 21, 10, 5, 1]
            if value <= 63:
                temp = coinsUsed[63 - value] + 1  #1
                if temp < minCoins:
                    minCoins = temp  #1
        coinsUsed[63] = minCoins
        print('面值为：{0} 的最小硬币数目为：{1} '.format(63, coinsUsed[63]) )

if __name__ == '__main__':
    values = [ 25, 21, 10, 5, 1]
    money = 63
    coinsUsed = {i:0 for i in range(money+1)}
    coinChange(values, money, coinsUsed)

# h