# 元祖的定义
# Tuple（元祖）与列表类似，不同之处在于元祖的元素不能修改
# 元祖 表示对个元素组成的序列
# 元祖在python开发中 有特定的应用场景
# 用于存储一串信息，数据之间使用，分隔
# 元祖用（）定义
# 元祖的索引从0开始
# 索引就是数据在元祖中的位置编号
# info_tuple=('zhangsan',18,1.75,'zhangsan')
# info_tuple1=(0,)
# print(info_tuple[0])
# print(info_tuple.index(18))
# print(info_tuple.count('zhangsan'))
# print(len(info_tuple))

# 循环遍历
# 取值就是从元祖中获取存储在指定位置的数据
# 遍历就是从头到尾依次从元祖中获取数据
# for 循环内部使用的变量 in 元祖
# for item in info:
#     循环内部针对元祖元素进行操作
#     print（item）
# 在python中，可以使用for循环遍历所有非数字类型的变量：列表、元祖、字典以及字符串
# 提示：在实际开发中，除非能够确认元祖中的数据类型，否则针对元祖的循环遍历需求不是很多
info_tuple=('zhangsan',18,1.75)
for my_info in info_tuple:
    #使用格式字符串拼接 my_info 这个变量不方便
    #因为元祖中通常保存的数据类型是不同的
    print(my_info)
# 元祖应用场景：
# # 函数的参数和返回值，一个函数可以接收任意多个参数，或者一次返回多个数据
# # 有关函数的参数和返回值
# # 格式字符串，格式化字符串后面的（）本质就是一个元祖
# # 让列表不可以被修改，以保护数据安全


#格式化字符串后面的‘（）’本质上就是元祖
print('%s 的年龄是 %d 身高是 %.2f' %('小明',18,1.75))
print('%s 的年龄是 %d 身高是 %.2f' %info_tuple)

info_str='%s 的年龄是 %d 身高是 %.2f' %info_tuple
print(info_str)

# 元祖和列表之间的转换
# 使用list函数可以把元祖转换成列表
# list（元祖）
# 使用tuple函数可以把list转换成元祖
# tuple（列表）
num_list=[1,2,3]
print(type(num_list))
num_tuple=tuple(num_list)
print(type(num_tuple))
tuple_1=(1,2,3)
print(type(tuple_1))
print(type(list(tuple_1)))
