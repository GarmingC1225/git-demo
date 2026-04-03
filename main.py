def simple_todos():#简单待办事项
    todo = []#列表
    while True :
        print("1.添加事项")
        print("2.查看事项")
        print("3.退出")
        choice = input('请输入选项：')

        if choice == '1':
            task = input("请输入事项：")
            todo.append(task)
            print(f"已添加事项:{task}")
            print('已添加事项:%s'% task)
            print('已添加事项:{0}'.format(task))
        elif choice == '2':
            if len(todo) == 0:
                print("无事项")
            else:
                for i,task in enumerate(todo,1):#枚举遍历
                    print(f'事项{i}.{task}')
                    print('事项%d.%s' % (i, task))
                    print('事项{0}.{1}'.format(i, task))

        elif choice == '3':
            break
        else:
            print("请输入正确的选项")


simple_todos()#调用函数