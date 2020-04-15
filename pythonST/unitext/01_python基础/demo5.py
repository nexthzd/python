# 函数：
# 所谓函数：就是把具有独立功能的代码块，组织为一个小模块，在需要的时候，调用
# 函数的使用包含两个步骤:
# 1.定义函数--封装 独立的功能
# 2.调用函数--享受 封装 的成果
# 函数作用，在开发程序时，使用函数可以提高编写的效率以及代码的重用
# 函数的定义 格式如下：
# def 函数名()：
#     函数封装的代码
# def是英文名define的缩写
# 函数名称应该能够表达函数封装代码的功能，方便后续的调用
# 函数名称 的命名应该符合标识符的命名规则
# 1.可以右字母、下划线和数字组成  2.不能以数字开头  3.不能与关键字重名


# def say_hello():#注意：定义好函数之后，只表示这个函数封装了一段代码而已，如果不主动调用函数，函数是不会主动执行的
#     print('hello 1')
#     print('hello 2')
#     print('hello 3')
# #  函数名()即可完成对函数的调用
# say_hello()

# name='xiaoming'
# # python解释器知道下方定义了一个函数，不会执行代码，需要调用后才会去执行
#
#
# def say_hello():
#     """哈哈哈"""
#     print('hello 1')
#     print('hello 2')
#     print('hello 3')
# print(name)
# # 只有在程序中，主动调用函数，才会让函数执行
# say_hello() #不可将函数调用定义在上方，因为在使用函数名  调用函数之前必须保证py已经知道函数的存在
# print(name)

# 函数的参数

# def sum_2num():
#     """对两个数字的求和"""
#     num1=10
#     num2=20
#
#     result=num1+num2
#     print('%d+%d=%d' %(num1,num2,result))
# sum_2num()

# 函数参数的使用
# 在函数名的后面的小括号内部填写参数
# 多个参数之间使用 ， 分隔
# def sum_2num(num1,num2):
#     result=num1+num2
#     print('%d+%d=%d' %(num1,num2,result))
# sum_2num(67,89)

#
# 形参和实参
# 形参：定义函数时，小括号中的参数，是用来接收参数用的，在函数内部作为变量使用
# 实参：调用函数时，小括号中的参数，是用来吧数据传递到函数内部用的
#
# 函数的返回值
# 一个函数执行结束后，告诉调用者一个结果，以便调用者针对具体的结果后续处理
# 返回值 是函数 完成工作后 最后给调用者一个结果
# 在函数中使用return关键字可以返回结果
# 调用函数一房，可以使用变量 来 接收函数的返回结果
# 注意：return表示返回，后续的代码都不会被执行
#
# def sum_2num(num1,num2):
#     """对两个数的求和"""
#     # return num1+num2
#     result=num1+num2
#
#     #可以使用返回值，告诉调用函数一方计算结果
#     return result
#     #return 下方对齐的代码永远不会被执行，因为是返回
#
#     # 调用函数，并使用result 变量接收计算结果
# result_sum=sum_2num(67,89)
#
# print('计算结果是：%d' %result_sum)

# 函数的嵌套调用
# 一个函数里面又调用了另外一个函数，这就是函数嵌套调用
# 如果函数test2中，调用了另一个函数test1
# 那么执行调用test1时，会先把函数中test1中的任务执行完，才会回到test2中调用函数test1中的位置，继续执行后续代码
# #
# def test1():
#     print('*' * 50)
#     print('test 1')
#     print('*' * 50) def test2():
#     print('*' * 50)
#     print('test 2')
#     print('*' * 50)
#     test1()
#     print('-' * 50)
# test2()


def test1():
    print('*' * 50)
def test2():
    print('-' * 50)
    #函数的调用
    test1()
    print('+' * 50)
test2()

def print_line(char,times):
    """

    @param char: 分隔线使用的分隔字符
    @param times: 分隔线重复的次数
    """
    print(char * times)
def print_lines(char,times):
    row=0
    while row<5:
        print_line(char,times)
        row+=1
print_lines('-',20)
# 使用模块中的函数
# 模块是python程序架构的一个核心概念
# 模块 就好比是一个工具包，要想使用这个工具包中的工具，就需要导入import这个模块
# 每一个以扩展名py结尾的python源代码文件都是一个模块
# 在模块中定义的全局变量、函数都是模块能够提供给外界直接使用的工具

# 模块名也是一个标识符
# 标识符可以由字母、下划线和数字组成
# 不能以数字开头
# 不能与关键字重名
# 注意：如果在python文件起名时，以数字开头是无法在pycharm中通过导入这个模块












