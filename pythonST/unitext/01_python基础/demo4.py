# 顺序--从上向下，顺序执行代码
# 分支--根据条件判断，决定执行代码的分支
# 循环--让特定代码重复执行

# while循环
# # 初始条件设置--通常是重复执行的 计数器
# # while 条件（判断 计数器 是否达到 目标次数）：
# #     条件满足时，做的事情1
# #     条件满足时，做的事情2
# #     条件满足时，做的事情3
# #     处理条件（计数器+1）
#
# i =0
# while i<5:
#     print('hello python')
#    # i=i+1
#     i+=1
# print('循环结束后，i=%d' %i)
# python中赋值运算符
# 加法赋值运算符+= 乘法赋值运算符*= 以此类推-= /= //=(取整除赋值运算符) %=（取余数赋值运算符）**=（幂赋值运算符）
# c=a+b 将a+b的运算结果赋值为c
# c+=a 等效于c=c+a
# c-=a 等效于c=c-a
# ...
# python中的计算方法（程序计数法 从0开始)--几乎所有的程序语言都选择从0开始

#循环计算
# 1.在while上方定义一个变量，用于存放最终计算成果，2.在循环体内部，每次循环都用最新计算结果，更新之前定义的变量
# 计算0-100之间所有数字累计求和结果
# result=0
# i=0
# while i<=100:
#     print('i=',i)
#     result += i
#     print('result=',result)
#     i += 1
# print('0-100之间的结果 %d' %result)
#计算0-100之间所有偶数的累计求和结果 （1.编写循环确认要计算的数字，添加结果变量，在循环内部处理计算结果）
# result=0
# i=0
# while i<=100:
#     if i%2==0:
#         print('i=', i)
#         #当i这个变量是偶数时，才进行操作
#         result += i
#         print('result=',result)
#     i += 1

# # break和continue
# break和continue是专门在循环中使用的关键字
# break某一条满足时，退出循环，不再执行后续重复的代码
# continue某一条件满足时，不执行后续重复的代码,其他条件都需要执行
# break和continue只针对当前所在循环有效

# i=0
# while i<10:
#     if i==3:
#         break
#     print(i)
#     i +=1

# i=0
# while i<10:
#     #continue 某一条件满足时，不执行后续重复的代码
#     #i==3
#     if i==3:
#         # 注意：在循环中，如果使用continue这个关键字，在使用关键字之前，需要确认循环的计算是否修改
#         # 否则可能会导致死循环
#         i+=1
#         continue
#     print(i)
#     i+=1
# #while循环嵌套 while循环嵌套就是：while里面还有while
# while条件1：
#     条件满足时，做的事情1
#     条件满足时，做的事情2
#
#     while条件2：
#          条件满足时做的事情1
#          条件满足时做的事情2
#
#          处理条件2
#     处理条件1
# row=1
# while row<=5:
#     print('*'*row)
#     row+=1
# 对print函数的使用做一个增强 1.在默认情况下，print函数输出之后，会自动在内容末尾增加换行
# 不换行处理语法：print('*',end='')
# print("*",end="--")
# print("*")

# row=1
# while row<=5:
#     # 每一行要打印的星星就是和当前行数是一致的
#     # 增加一个小循环，专门负责当前行中，每一列的星星显示
#     # 定义一个列计数器变量
#     col=1
#     # 开始循环
#     while col <=row:
#         print('*',end='')
#         col+=1
#     print('')#这行代码的目的，就是在一行星星输出完成之后，添加换行
#     row+=1

# 1.打印9行小星星
row=1
while row<=9:
    col=1
    while col<=row:
        # print("*",end=" ")
        print("%d*%d= %d"  %(col,row,col*row),end="\t")
        col+=1
    print("")
    row+=1
# \t 在控制台输出一个 制表符，协助在输出文本时 垂直方向  保持对齐
print('1\t2\t3')
print('10\t20\t30')
# \n 在控制台输出一个 换行符
print('hello\n python')
#\"可以在控制台输出双引号，\转义字符
print("hello\"hello")














