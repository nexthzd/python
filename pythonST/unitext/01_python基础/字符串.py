# 字符串定义：
# 字符串就是一串字符，是编程语言中表示的数据类型
# 在python中可以使用一对双引号“或者一对单引号‘ 定义一个字符串
# 虽然可以使用\"或者\'做字符的转义，但在实际开发中：
#     如果字符串内部需要使用“，可以使用’定义字符串
#     如果字符串内部需要使用‘，可以使用“定义字符串
# 可以使用索引获取一个字符串中 指定位置的字符，索引计数从0开始
# 也可以使用for循环遍历字符串中每一个字符
# 大多数编程语言都是使用“来定义字符串
# str1="hello python"
# str2="我的外号是'大西瓜'"
# print(str2)
# print(str1[6])
#
# # for i in str2:
# #      print(i)
# print(len(str1))
# print(str1.count('hello'))
# print(str1.index('o'))
# 字符串的常用操作
# str.isspace（），如果str中只包含空格，则返回true
# isalnum（），如果str至少有一个字符并且所有字符都是字母或者数字则返回true
# isalpha（），如果str中至少有一个字符并且所有字符都是字母则返回true
# isdecima（），如果str只包含数字则返回true，全角数字
# 字符串的转义字符
# \t 在控制台输出一个制表符，协助在输出文本时  垂直方向保持对其
#  \n 在控制台输出一个换行符
# space_str="   \t\n\r "
# print(space_str.isspace())#只包含空格(空白字符)  返回true
# num_str ='\u00b2'  #判断是否包含数字，包含返回true，不能有小数点  unicode 字符串（2,3可判断）
# print(num_str)
# print(num_str.isdecimal())
# print(num_str.isdigit())
# print(num_str.isalnum())
#
# hello_str="hello world"
# print(hello_str.startswith("Hello"))
# print(hello_str.endswith("world"))
#
# #查找指定字符串
# # index同样可以查找指定的字符串在大字符串中的索引
# print(hello_str.find('llo'))
# #index如果指定字符串不存在，会报错
# # find如果指定字符串不存在，会返回-1
# # replace方法执行完成后，会返回一个新的字符串，不会修改原有字符串的内容
# print(hello_str.replace("world","python"))
# print(hello_str)

#要求：顺序并且居中对齐
# peom =["\t\n登鹤雀楼",
#        "王黄芝",
#        "白日依山尽\n",
#        "黄河入海流",
#        "欲穷千里目",
#        "更上一层楼"]
# for peom_str in peom:
#      print("|%s|" % peom_str.strip().center(10,"　"))
#
# # 先使用strip方法去除字符串的空白字符
peom ="登鹤雀楼=王黄芝=白日依山尽=黄河入海流=更上一层楼="
print(peom)
peom_str=peom.split("=")
print(peom_str)
# # 合并字符串
# result= " ".join(peom_str)
# print(result)
# num_str='0123456789'
# print(num_str[2:6])#2-5
# print(num_str[2:])
# print(num_str[0:6])
# print(num_str[:6])
# print(num_str[:])
# print(num_str[::2])
# print(num_str[1::2])
# print(num_str[2:-1])
# print(num_str[-2:])
# print(num_str[0::-1])
# print(num_str[-1::-1])
# print(num_str[::-1])