Todo = [] 
add = input("Enter your first task: ")
Todo.append(add)
print("Your todo list: ", Todo)

#Asking the user if they want to add until they say no
update = input("Would you like to add something else? Yes or No? ")
while update.lower() not in ("yes", "no"): #To enforce the user to say yes or no 
    print("Please enter Yes or No.")
    update = input("Would you like to add something else? Yes or No? ") 
while update.lower() == "yes": #If yes, prompts to add another task to end of list + enforce the user to say yes or no again, and proceeds until they say no
    add_more = input("What's next? ")
    Todo.append(add_more)
    print("Your todo list: ", Todo)
    update = input("Would you like to add something else? Yes or No? ") 
    while update.lower() not in ("yes", "no"): #
        print("Please enter Yes or No.")
        update = input("Would you like to add something else? Yes or No? ")
if update.lower() == "no": #after no, moves onto the next question
    print("No problem!")

#Asking the user if they want to delete until they say no
delete = input("Would you like to delete something from your todo list? Yes or No? ")
while delete.lower() not in ("yes", "no"): #To enforce the user to say yes or no
    print("Please enter Yes or No.")
    delete = input("Would you like to delete something from your todo list? Yes or No? ")   
while delete.lower() == "yes": #If yes, prompts to delete a task from the list + enforce the user to say yes or no again, and proceeds until they say no
    which_one = input("Which one? ")
    if which_one in Todo: #specifically deletes a task from list and checksif empty
        Todo.remove(which_one)
        print(which_one, "has been removed from your todo list.")
        print("Your todo list: ", Todo)
        if len(Todo) == 0:
            print("Your todo list is now empty.")
            break
    else:  #checks is task is not in list
        print(which_one, "is not in your todo list.")
    delete = input("Would you like to delete something else from your todo list? Yes or No? ")
    while delete.lower() not in ("yes", "no"):
        print("Please enter Yes or No.")
        delete = input("Would you like to delete something else from your todo list? Yes or No? ")

#Ask the user if they want to review their list
show = input ("Do you want to review your todo list? Yes or No? ")
while show.lower() not in ("yes", "no"): #To enforce the user to say yes or no
    print("Please enter Yes or No.")
    show = input ("Do you want to review your todo list? Yes or No? ")
if show.lower() == "yes": #If yes, shows the list
    print("Your todo list: ", Todo)
else: #If no, ends the program
    print("Okay!")

#Asking the user if they want to add or delete until they say no
add_delete = input("Do you need to add or delete something else on your todo list?  Add, Delete, or Done? ")
add_delete = add_delete.lower()
while add_delete not in ("add", "delete", "no"): #To enforce the user to say add, delete, or no
    print("Please enter Add, Delete, or No.")
    add_delete = input("Do you need to add or delete something else on your todo list?  Add, Delete, or No? ")
while add_delete == "add": #If add, prompts to add another task to end of list + enforce the user to say add, delete, or no again, and proceeds until they say no
    add_more = input("What's next? ")
    Todo.append(add_more)
    print("Your todo list: ", Todo)
    add_delete = input("Do you need to add or delete something else on your todo list?  Add, Delete, or No? ")
    while add_delete not in ("add", "delete", "no"):
        print("Please enter Add, Delete, or No.")
        add_delete = input("Do you need to add or delete something else on your todo list?  Add, Delete, or No? ")
while add_delete == "delete": #If delete, prompts to delete a task from the list + enforce the user to say add, delete, or no again, and proceeds until they say no
    which_one = input("Which one? ")
    if which_one in Todo: #specifically deletes a task from list and checks if empty
        Todo.remove(which_one)
        print(which_one, "has been removed from your todo list.")
        print("Your todo list: ", Todo)
        if len(Todo) == 0:
            print("Your todo list is now empty.")
            break
    else:  #checks is task is not in list
        print(which_one, "is not in your todo list.")
    add_delete = input("Do you need to add or delete something else on your todo list?  Add, Delete, or Done? ").lower()
    while add_delete not in ("add", "delete", "done"):
        print("Please enter Add, Delete, or Done")
        add_delete = input("Do you need to add or delete something else on your todo list?  Add, Delete, or Done? ").lower()
if add_delete.lower() == "done": #If done, show their entire list and end the program
    print("Okay, Here is your final todo list: ", Todo)


