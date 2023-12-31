from function import write_todos
import time

# open todos txt file
with open("todos.txt", "r") as file:
    todos = file.readlines()

time_string = time.strftime("%m/%d/%Y , %H:%M:%S")
print(time_string)

while True:
    # ask for operation
    user_action = input("--enter add, show, edit, complete or exit--? ").strip(" ")

    # add operation
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos.append(todo)
        write_todos(todos)

    # edit operation
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5]) - 1
            new_todo = input("enter a new todo: ") + "\n"
            todos[number] = new_todo
            write_todos(todos)
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
            write_todos(todos)
        except IndexError:
            print("There is no item with this number.")
            continue

    # exit operation
    elif user_action.startswith("exit"):
        break

    else:
        print("Command Is Not Valid. Try Again")

print("bye")
