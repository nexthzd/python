# print('hello python')
# print('hello world')
# print('你好世界')
# print('hello hello')
#
# print(10//2)
# print(9//2)
# print(2**3)
# print(9%2)
# print('_'*10)
# print('__________')
# print('喜欢张狗子'*2)
# qq_number='123456'
# qq_passwd='wwwww'
# print(qq_number)
# print(qq_passwd)

# #变量定义
# prices=8.6
# weight=7.5
# money=prices*weight
# money=money-5  #1.直接使用之前已经定义的变量，2.变量名只有在第一次出现才是定义变量 3.变量名再次出现，
#                # 不是定义变量，而是直接使用之前定义过的变量 4.程序中可以修改之前定义的变量
# print(money)

#变量类型
#在Python，定义变量时是不要指定变量类型
#在运行时候，python解释器会根据赋值语句等号右侧数据在自动推导出变量中保存数据的准确类型
# name='小明'
# age=18
# gender=True #是 布尔类型
# height=1.75
# weight =75
# print(name)

# if 语句
# 如果条件满足，才做某件事情（可以做if模块下带缩进的代码，如果不满足跳过带缩进的代码执行顶格代码）
# 如果 条件不满足，就做另外一件事情，或者什么都不做
# if 要判断的条件：
#     条件成立时，要做的事情（注意：代码的缩进为一个tab键，或者4个空格--建议使用空格，python开发中，tab和空格不要混用）
#else：
#     条件不成立时，要做的事情（可以做else模块下带缩进的代码）
# age=int(input('请输入年龄：')) #注意：两种不同的类型是不能进行比较的，所以将该字段转换成int格式
# if age >=18:
#     print('可以进入网吧')
# else:
#     print('不可以进入')
#     print('回家写作业')

#逻辑运算
#条件1 and 条件2  两个条件同时满足，返回true  ：与
#条件1 or 条件2,  两个条件只要有一个满足  返回true  ：或
#not 条件  条件取反  ：非
#
# age =120
# if age>=0 and age<=120:
#     print('true')
# else:
#     print('false')
#
# py_score=5
# c_score=70
# if py_score>=60 or c_score>=60:
#     print('true')
# else:
#     print('false')
# #定义一个布尔型变量is_employee，
# # 在开发中，通常希望某个条件不满足时，执行一些代码，可以用not
# # 另外，如果需要拼接复杂逻辑计算条件，同样也有可能使用到not
# is_employee=True
# if not is_employee:
#     print('不允许进入')
# elif（elif和else都必须和if联合使用，而不能单独使用；可以将if else和elif以及各自缩进的代码，看成一个完整的代码块）
#增加一些条件，条件不同，需要执行的代码也不同时，就可以使用elif
# if 条件1：
#     条件1满足执行的代码
# elif 条件2：
#     条件2满足时，执行的代码
# elif 条件3：
#      条件3满足时，执行的代码
# else：
#      以上条件都不满足时，执行的代码
# holiday_name=input('请输入节日：')
# if holiday_name=='情人节':
#     print('开房')
# elif holiday_name=='平安夜':
#     print('开房加1')
# elif holiday_name=='生日':
#     print ('可能还是开房')
# else:
#     print ('好好学习')
# if 的嵌套（应用场景就是在之前条件满足的前提下，再增加额外的判断；除了缩进之外和之前的没有区别）
# if 条件1：
#     条件1 满足执行的代码
#     if 条件1 基础上的条件2：
#         条件2 满足时，执行的代码
#     else：
#          条件2 不满足时，执行的代码
# else:
#     条件1 不满足时，执行的代码
# has_ticket=True
# kife_length=15
# if  has_ticket:
#     print('有车票，准备安检')
#     if kife_length>20:
#         print('您携带的刀太长，有%d公分长' %kife_length)
#         print('不允许上车')
#     else:
#         print('通过安检')
# else:
#     print('买票')
#综合应用--石头剪刀布
import random
palyer=int(input('输入数字比比运气：'))
computer=random.randint(1,3)
print('玩家选择%d - 电脑选择%d' %(palyer,computer))
if ((palyer==1 and computer==2)
        or(palyer==2 and computer==3)
        or(palyer==3 and computer==1)):
    print('你可真是C位小公主')
elif palyer>3:
    print('请输入1、2、3任意一个数字')
elif palyer==computer:
    print('看不出来小公举运气和我一样好')
else:
    print('运气也是实力的一种必要条件')

#随机数处理
# random.randint(a,b),返回[a，b]之间的整数，包含a和b
# eg：
# random.randint(12,20)#生成的随机数12<=n<=20
# random.randint(20,20)#生成的结果永远为20
# random.randint(20,10)#该语句是错误的，下限必须小于上限









