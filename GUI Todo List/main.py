from function import read_todo,write_todo
import PySimpleGUI as psg


app_lable = psg.Text("have a great dat!")
app_lable_name = psg.Text("Todo list")
todo_input = psg.InputText(tooltip="Enter a Todo", key="todo")
button_add = psg.Button("add a Todo")

win = psg.Window("Todo List", layout=[[app_lable],[app_lable_name],[todo_input,button_add]])
while True:
    event, value = win.read()
    match event:
        case "add a Todo":
            todos = read_todo()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            write_todo(todos)
        case psg.WIN_CLOSED:
            break

win.close()
