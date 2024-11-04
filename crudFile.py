import json

def file_loader():
    try:
        with open("todos.txt", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def save_dataHelper(todos):
    with open("todos.txt", "w") as file:
        json.dump(todos, file)

def create_todo(todos):
    todo = input("Enter your todo: ")
    title = input("Enter your title: ")
    todos.append({"title": title, "todo": todo})
    save_dataHelper(todos)

def list_todos(todos):
    print("\n List Of Todos:")
    print("*"*20)
    for index, todo in enumerate(todos,start=1):
        print(f"{index}.{todo['todo']}, Title: {todo['title']}")  
    print("*"*20)    

def  update_todo(todos):
    todo_index = int(input("Enter the index of the todo to update: ")) - 1
    if todo_index >= 0 and todo_index < len(todos):
        new_todo = input("Enter the new todo: ")
        new_title = input("Enter the new title: ")
        todos[todo_index] = {"title": new_title, "todo": new_todo}
        save_dataHelper(todos)
        print("Todo updated successfully!")

def delete_todo(todos):
    todo_index = int(input("Enter the index of the todo to delete: ")) - 1
    if todo_index >= 0 and todo_index < len(todos):
        del todos[todo_index]
        save_dataHelper(todos)
        print("Todo deleted successfully!")    
        
def main():
    todos = file_loader()
    
    print("\nTodo Create app")
    print("1: Create a new Todo")
    print("2: List all Todos")
    print("3: Update a Todo")
    print("4: Delete a Todo")
    print("5: Exit")
    
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            create_todo(todos)
        case "2":
            list_todos(todos)    
        case "3":
            update_todo(todos)     
        case "4":
            delete_todo(todos)    
        case "5":
            print("Exiting...")   
        case _:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
