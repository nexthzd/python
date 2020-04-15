# 字典
# dictionary(字典)是出列表之外 python之中最灵活的数据类型
# 字典同样可以用来存储多个数据
#   通常用于存储描述一个物体相关的信息
# 和列表区别
#   列表是有序的对象集合
#   字典是无序的对象集合
# 字典用{} 定义
# 字典使用键值对存储数据，键值对之间使用，分隔
# 键key是索引
# 值value是数据
# 键和值之间用：分隔
# 键必须是唯一的
# 值可以是任何数据类型，但键只能使用字符串、数字或元祖
#字典是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序和定义的顺序是不一样的
# xiaoming={'name':'小明',
#           'age':18,
#           'hight':176,
#           'weght':60,
#           'gender':True}
# print(xiaoming['name'])#取值的时候，如果指定的key不存在会报错
# #增加修改字典：key存在，会修改已存在的key，不存在则新增键对值
# xiaoming['position']='IT'
# xiaoming['name']='小哥'
#
# xiaoming.pop('name')#删除
# #统计键值对数量
# print(len(xiaoming))
#
# #合并字典，需注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
# temp_dict ={'height':1.75,
#             'age':'20'}
# xiaoming.update(temp_dict)
#
# #清空字典
# xiaoming.clear()
# print(xiaoming)

#循环遍历
# 遍历就是依次从字典中获取所有键值对

xiaoming_dict={'name':'xiaoming',
               'qq':'1234567',
               'phone':'13455555'}
#迭代遍历字典
#变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:
    print(xiaoming_dict[k])
#      print('%s - %s' %(k,xiaoming_dict[k]))
# # 应用场景
# 尽管可以使用 for in 遍历字典
# 但是在开发中，更多的应用场景是：
#     使用多个键对值，存储描述一个物体 的相关信息--描述更复杂的数据信息
#     将多个字典放在一个列表中，再进行遍历，在循环体内部针对每一个字典进行相同的处理
# card_list=[{'name':'张三',
#             'qq':'1234',
#             'phone':'10086'},
#            {'name':'lisi',
#             'qq':'123',
#             'phone':'1134'}
#            ]
# for card_info in card_list:
#     print(card_info)






