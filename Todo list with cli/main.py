# open todos txt file
with open("todos.txt", "r") as file:
    todos = file.readlines()

while True:
    # ask for operation
    user_action = input("--enter add, show, edit, complete or exit--? ").strip(" ")

    # add operation
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos.append(todo)
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)

    # edit operation
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5]) - 1
            new_todo = input("enter a new todo: ") + "\n"
            todos[number] = new_todo
            with open("todos.txt", "w") as write_edit:
                write_edit.writelines(todos)
        except ValueError:
            print("invalid command")
            continue

    # show operation
    elif user_action.startswith("show"):
        new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(new_todos):
            index = index + 1
            print(f"{index} => {item}")

    # complete operation
    elif user_action.startswith("complete"):
        try:
            done_number = int(user_action[9]) - 1
            todos.pop(done_number)
            with open("todos.txt", "w") as write_complete:
                write_complete.writelines(todos)
        except IndexError:
            print("There is no item with this number.")
            continue

    # exit operation
    elif user_action.startswith("exit"):
        break

    else:
        print("Command Is Not Valid. Try Again")

print("bye")
