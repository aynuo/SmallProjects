def write_todos(todos_arg):
    """ This Function Write Output In The todos.txt """
    with open("todos.txt", mode="w") as file_local:
        file_local.writelines(todos_arg)