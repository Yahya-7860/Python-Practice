def add(todo):
    with open('todo.txt', 'a') as file:
        file.write('--> ' + todo + '\n')


def see():
    with open('todo.txt', 'r') as file:
        for todo in file:
            print(todo)

while True:    
    choice = input("Do you want to add todo or want to see todo list or quite (add,see,q): ")
    if choice == 'q':
        exit()
    elif choice == 'add':
        todo = input("Enter you todo : ").capitalize()
        add(todo)
    elif choice == 'see':
        see()
    else:
        print("invalid choice")


# if __name__ == "__main__":
#     main()
