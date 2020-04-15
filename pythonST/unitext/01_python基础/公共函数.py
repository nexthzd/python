# 公共方法
# python内置函数：可以不用通过import导入直接就可以使用的函数
# len(item):计算容器中的元素个数
# del(item):删除变量
# max(item):返回容器中最大值，如果是字典，只针对key比较
# min(item):返回容器中最小值，如果是字典，只针对key比较
# cmp(item1,item2)：比较两个值，-1小于/0相等/1大于，python3中取消该函数
# 注意：字符串比较符合以下规则："0"<"A"<"a"

# 切片：‘0123456789’[::-2] 97531 支持类型，字符串、列表、元祖
# 切片使用索引值来限定范围，从一个打的字符串中切除小的字符串
# 列表和元祖都是有序的集合，都能够通过索引值获取到对应的数据
# 字典是一个无序的集合，使用键值对保存数据

# 5.3 运算符
print([1,2] *5)
print((1,2)*5)
print('tt'*2)
print('hello'+'py')
print((2,3)+(3,4))
print([5,6]+[5,6])
print(3in(1,2))#元素是否存在  字符串、列表、元祖、字典只能判断key
print('a'in'yfgj')
print(3in[45,90,34])
print(3in{'k':4,'9':3})

# 5.4 玩着的for循环
# for 变量 in  集合：
    # 循环体代码
# else：
     # 没有通过break退出循环，循环结束后，会执行的代码
for num in [1,2,3]:
    print(num)
    if num==2:
        break
else:
    # 如果循环体内部使用break退出了循环那么else下方的代码不会被执行
    print('hui')
print("xunh")

dit=[{'a':2,"b":4,},
     {"a":4,"b":6}]
# 搜索指定的数字
find_num='2'
for i in dit:
    print(i)
    if i['a']== find_num:
        print('zhaodao %s' %find_num)


