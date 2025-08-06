from tabulate import tabulate
from colorama import Fore, Style

menu = ("1.Add Task", "2.Edit Task", "3.Remove Task", "4.Show All Task", "5.Exit")
data_list = []

while True:
    
    for data in menu:
        print(data)
        
    menu_num = int(input("\nEnter Number of Options: "))
    
    match menu_num:
        case 1:
            while True:
                temp_tuple = ()
                temp = int(input("\nEnter The ID of Task: "))
                temp_tuple += (temp,)
                temp = input("\nEnter The Text of Task: ")
                temp_tuple += (temp,)
                temp = input("\nEnter The Privilege of Task (1-3): ")
                temp_tuple += (temp,)
                dic_task = {
                    "ID": temp_tuple[0],
                    "Text": temp_tuple[1],
                    "Privilege": temp_tuple[2]
                }

                data_list.append(dic_task)
                print("\n''' Task Added Successfully! '''")
                
                more = input("\nDo You Want to Add Another? (y/n): ")
                if more.lower() != 'y':
                    break
        
        case 2:
            task_id = int(input("Enter ID of Task to Edit: "))
            found = False

            for task in data_list:
                if task['ID'] == task_id:
                    print("''' Leave blank if you don't want to change a field. '''")

                    new_text = input(f"\nEnter new Text (current: {task['Text']}): ")
                    new_privilege = input(f"\nEnter new Privilege (current: {task['Privilege']}): ")

                    if new_text.strip() != "":
                        task['Text'] = new_text
                    if new_privilege.strip() != "":
                        task['Privilege'] = new_privilege

                    print("''' Task Updated Successfully! '''")
                    found = True
                    break

                if not found:
                    print("''' Task With This ID Not Found. '''")
        case 3:
            task_id = int(input("Enter ID of Task to Remove: "))
            found = False

            for index, task in enumerate(data_list):
                if task['ID'] == task_id:
                    del data_list[index]
                    print("Task Removed Successfully!")
                    found = True
                    break
                
            if not found:
                print("Task with this ID not found.")
            break
        
        case 4:
            if not data_list:
                print(Fore.RED + "No tasks available." + Style.RESET_ALL)
            else:
                table = []
                for task in data_list:
                    table.append([task['ID'], task['Text'], task['Privilege']])

                headers = [Fore.CYAN + "ID" + Style.RESET_ALL, 
                           Fore.CYAN + "Text" + Style.RESET_ALL, 
                           Fore.CYAN + "Privilege" + Style.RESET_ALL]

                print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

        case 5:
            break