# 列表定义：
# list是python中使用最频繁的数据类型，在其他语言中通常叫做数组
# 专门用于存储一串信息
# 列表用[]定义，数据之间使用 '，'分隔
# 列表的索引从0开始，索引就是数据在列表中的位置编号，索引又可以被称为下标
# 注意：从列表中取值时，如果超出索引范围，程序会报错
# name_list=['zhang','li','wang']
# len(列表)#获取列表的长度n+1
# 列表count（数据）数据在列表中出现的次数
# 列表sort()升序排序
# 列表sort(reverse=True)降序排序
# 列表reverse反转/逆转
# del[索引]删除指定的索引数据
# 列表remove(数据)删除第一个出现的指定数据
# 列表pop删除末尾数据
# 列表pop[索引]删除指定的索引数据
# 列表insert(索引，数据)在指定位置插入数据
# 列表append（数据）在末尾追加数据
# 列表extend(列表2)将列表2中的数据追加到列表1中
# 列表[索引]从列表中取值
# # 列表index(数据)获得数据第一次出现的索引
# print(name_list)
# print(name_list[0])#取值和取索引
# print(name_list.index('wang'))#知道数据的内容，想确定数据在列表中的位置，
# # 使用index方法需要注意，如果传递的数据不存在列表中，程序会报错
# name_list[0]='zhangsan'
# print(name_list)
# name_list.append('小可爱')
# print(name_list)
# name_list.insert(0,'哈哈')
# name_list.insert(0,'哈哈')
# print(name_list)
# insert_1=['huhu','lili','lala',5555]
# name_list.extend(insert_1)
# print(name_list)
# print(name_list.count('哈哈'))
# print(name_list.index('lili'))
# # 列表中删除数据
# name_list.remove('哈哈')#删除指定的数据
# print(name_list)
# name_list.pop()#默认删除最后一个数据
# print(name_list)
# name_list.pop(2)#指定删除索引位置的数据
# print(name_list)
# print(name_list)
# del name_list[1]
# print(name_list)
# name_list.clear()
# print(name_list)

# 列表统计
# name_li=['张三','李四','wnagwu','wangxiaoer','张三']
# list_len=len(name_li)
# print('列表中包含 %d个元素' % list_len)
# print(len(name_li))
# count =name_li.count('张三')
# print('张三出现的 %d 次' %count)
#
# name_list1=['zhangsan','lisi','wangwu','wangxiaoer']
# num_list=[6,8,4,1,10]
# # name_list1.sort()
# # num_list.sort()
# # name_list1.sort(reverse=True)
# # num_list.sort(reverse=True)
# name_list1.reverse()
# num_list.reverse()
# print(name_list1)
# print(num_list)
#
# 循环遍历
# 遍历  就是从头到尾依次从列表中获取数据
#    在循环体内部针对每一个元素，执行相同操作
# 在python中为了提高列表的遍历效率，专门提供的迭代iteration遍历
# 使用for就能够实现迭代遍历
# for 循环内部使用的变量 in 列表
# # for name in name_list
# #     循环内部针对列表元素进行操作
# #     print（name）
name_li=['张三','李四','wnagwu','wangxiaoer','张三']
"""
顺序的从列表中依次获取数据，每一次循环过程中，数据都会保存在my_name 这个变量中，
在循环体内部可以访问到当前这一次获取到的数据

"""
for my_name in name_li:
    print('my name is %s' % my_name)