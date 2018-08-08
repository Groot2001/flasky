# coding=utf-8

def dec1(func):
    print("1111")
    def one():
        print("2222")
        func()
        print("3333")
    return one

def dec2(func):
    print("aaaa")
    def two():
        print("bbbb")
        func()
        print("cccc")
    return two

@dec1
@dec2
def test():
    print("test test")

#预期：
'''
aaaa    #先从里层dec2调用test开始执行：dec2先执行打印aaaa，然后遇到函数two定义（暂时未调用two故直接返回two函数引用）
1111    #从dec2函数返回two退出后，到dec1调用dec2打印1111
2222    #因为dec1调用的dec2还有嵌套调用test，故继续调用dec1的one函数，打印2222
bbbb    #继续调用one函数里的func即dec1的引用，因为之前dec1已经返回了two函数引用，即调用的是two函数，依次打印：bbbb test test cccc
test test
cccc
3333    #当two函数执行完，从dec1返回到dec2的func调用处，此时继续执行打印3333

'''


test()