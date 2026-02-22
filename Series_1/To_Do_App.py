def task():
    tasks = [] # empty list
    print("-----Welcome To The Task Menagement App-----")

    total_task = int(input("Enter how many task you want to add = ")) #5
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ") # enter task 3
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter task you want to add =  ")
            task.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
                update_val = input("Enter the task name you want to update = ")
                if updated_val in tasks:
                    up = input("Enter new task = ")
                    ind = tasks.index(updated_val) #2
                    tasks[ind] = up
                    print("Updated task {up}")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task {del_val} has been deleted...")

        elif operation == 4:
                print(f"Total tasks = {tasks}")

        elif operation == 5:
                print("Closing the program...")
                break

        else:
                print("Invalid Input")

task()

                

            
                
                
