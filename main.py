# def simple_todos():#简单待办事项
#     todo = []#列表
#     while True :
#         print("1.添加事项")
#         print("2.查看事项")
#         print("3.退出")
#         choice = input('请输入选项：')
#
#         if choice == '1':
#             task = input("请输入事项：")
#             todo.append(task)
#             print(f"已添加事项:{task}")
#             print('已添加事项:%s'% task)
#             print('已添加事项:{0}'.format(task))
#         elif choice == '2':
#             if len(todo) == 0:
#                 print("无事项")
#             else:
#                 for i,task in enumerate(todo,1):#枚举遍历
#                     print(f'事项{i}.{task}')
#                     print('事项%d.%s' % (i, task))
#                     print('事项{0}.{1}'.format(i, task))
#
#         elif choice == '3':
#             break
#         else:
#             print("请输入正确的选项")
#
#
# simple_todos()#调用函数

def todo_with_status():
    todos = []

    def add_todo(task, priority = "中"):
        '''添加代办事项'''
        todo = {    #字典
            'id': len(todos) + 1,
            'task': task,
            'status': '未完成',
            'priority': priority,
            'create_time': ''   #后边添加时间处理
        }
        todos.append(todo)
        return todo

    def show_todos():
        '''显示所有代办事项'''
        if not todos:
            print("暂无待办事项")
            return

        print('\n待办事项列表：')
        for todo in todos:
            if todo['status'] == '已完成':
                status_icon = "√"
            else:
                status_icon = '0'
            print(f"{todo['id']}.[{status_icon}]{todo['task']}(优先级：{todo['priority']})")    #打印1.[√]任务(优先级：中级)

    def complete_todo(todo_id):
        """标记为已完成"""
        try:
            todo = todos[todo_id - 1]
            todo["status"] = "已完成"
            print(f"已完成: {todo['task']}")
        except IndexError:  # 异常处理
            print("ID不存在")
