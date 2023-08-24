import streamlit as st
import func

todos = func.get_todo()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)

todos = func.get_todo()

st.title("My Todo App")
st.subheader("This is my sub header")
st.write("this app is to increase your productivity!")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")
