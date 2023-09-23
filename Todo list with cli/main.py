with open("todos.txt", "r") as file:
    todos = file.readlines()

while True:
    user_action = input("--enter add, show, edit, complete or exit--? ").strip(" ")

    if "add" in user_action:
        todo = user_action[4:] + "\n"
        todos.append(todo)
        with open("todos.txt", "w") as write_file:
            write_file.writelines(todos)

    elif "edit" in user_action:
        number = int(user_action[5]) - 1
        new_todo = input("enter a new todo: ") + "\n"
        todos[number] = new_todo
        with open("todos.txt", "w") as write_edit:
            write_edit.writelines(todos)

    elif "show" in user_action:
        new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(new_todos):
            index = index + 1
            print(f"{index} => {item}")

    elif "complete" in user_action:
        done_number = int(user_action[9]) - 1
        todos.pop(done_number)
        with open("todos.txt", "w") as write_complete:
            write_complete.writelines(todos)

    elif "exit" in user_action:
        break

    else:
        print("Command Is Not Valid. Try Again")

print("bye")
