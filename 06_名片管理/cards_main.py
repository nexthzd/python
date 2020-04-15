import cards_tools
#无线循环，由用户主动决定什么时候退出循环
while True:
    #显示功能菜单
    cards_tools.show_menu()
    action_str=input("执行的操作：")
    print('选择操作 %s' %action_str)
    if action_str in ["1","2","3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str=="2":
            cards_tools.show_all()
        # 查询名片
        elif action_str=="3":
            cards_tools.search_car()
    # 如果在开发程序时，不希望立刻编写分支内部的代
    # 码，可以使用pass关键字，表示一个占位符，能够保证程序代码结构正确
    # 程序运行时，pass关键字不会执行任何操作1
    elif action_str=='0':
        print('welcom next time')
        break
        # pass
    else:
        print('false')