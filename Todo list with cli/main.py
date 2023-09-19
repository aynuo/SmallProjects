todos = []

with open("todos.txt", "r") as file:
    file.readlines()

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
            new_todo = input("enter a new todo: ")
            todos[number] = new_todo

        case "show":
            for index, todo in enumerate(todos):
                index = index + 1
                print(f"{index} => {todo}")

        case "complete":
            done_number = int(input("enter your todo number to delete:")) - 1
            todos.pop(done_number)

        case "exit":
            break

print("bye")
