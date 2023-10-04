def read_todo():
    """
        this function open todos.txt file and read data
    """
    with open("todos.txt", mode="r") as file:
        todos = file.readlines()
    return todos


def write_todo(new_todo):
    with open("todos.txt", mode="w") as file:
        file.writelines(new_todo)

