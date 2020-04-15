card_list=[]

def show_menu():
    print("*"*50)
    print("欢迎使用，名片管理系统v.1 ")
    print("")
    print("1.新增名片")
    print("")
    print("2.显示全部")
    print("")
    print("3.查询名片")
    print("*" * 50)
def new_card():
    print("-" * 50)
    print("新增名片")
    name=input("输入姓名：")
    phone=input("输入电话：")
    card_dit={"name":name,
               "phone":phone}
    card_list.append(card_dit)

    print(card_list)

    print("添加 %s 成功" % name)

def show_all():
    print("-" * 50)
    print("显示所有")
    for name in ["姓名","电话"]:
        print(name,end="\t\t")
    print("")
    print("=" * 50)
    for card_dit in card_list:
        print("%s\t\t%s" %(card_dit["name"],
                           card_dit["phone"]))




def search_car():
    print("-"*50)
    print("搜索名片")
