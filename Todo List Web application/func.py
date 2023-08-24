FILEPATH = "todos.txt"

def get_todo(filepath=FILEPATH):
    with open(filepath, mode="r") as file:
        todos = file.readlines()
    return todos

def write_todos(new_todo):
    with open("todos.txt" , mode="w") as file:
        file.writelines(new_todo)
