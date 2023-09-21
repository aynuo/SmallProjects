with open("todos.txt", "r") as file:
    todos = file.readlines()

while True:
    user_action = input("--enter add, show, edit, complete or exit--? ").strip(" ")

    match user_action:
        case "add":
            todo = input("Enter a new todo: ") + "\n"
            todos.append(todo)
            with open("todos.txt", "w") as write_file:
                write_file.writelines(todos)

        case "edit":
            number = int(input("enter your todo number for edit>> ")) - 1
            new_todo = input("enter a new todo: ") + "\n"
            todos[number] = new_todo
            with open("todos.txt", "w") as write_edit:
                write_edit.writelines(todos)

        case "show":
            new_todos = [item.strip("\n") for item in todos]
            for index, item in enumerate(new_todos):
                index = index + 1
                print(f"{index} => {item}")

        case "complete":
            done_number = int(input("enter your todo number to delete:")) - 1
            todos.pop(done_number)
            with open("todos.txt", "w") as write_complete:
                write_complete.writelines(todos)

        case "exit":
            break

print("bye")
