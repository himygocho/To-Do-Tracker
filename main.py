

"""
Variables
"""
tasks = []


def main_menu():
    """
    Purpose: to display menu
    """
    while True:

        print("====MAIN MENU====")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Delete Tasks")
        print("4. Exit")   
        print("Choose an Option") 

        user_input = input()
        if user_input == "4":
            print("Exiting...")
            break
        elif user_input == "2":
            task = input("what task would you like to add? ")
            tasks.append(task)
            print(tasks)


    

        
    
    
main_menu()


