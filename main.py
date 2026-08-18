from pathlib import Path
from colorama import Fore, Back, Style, init



init()





print("##########################################################################")
print("                               REPO GUARD")
print("##########################################################################")


kewwords_1 = ["password", "api_key", "secret", "token"]
counter_files = 0
counter_warning = 0
project_path = input("Enter the project path: ")
if len(project_path) == 0:
    print("ERROR: path cant be empty!")

if len(project_path) > 0: 
    path = Path(project_path)
    if path.exists() and path.is_file() != True:
        print("------------------------------------------------------")
        print(f"scanning: {project_path}")
        print("------------------------------------------------------")
        for i in path.rglob("*"):
            if i.is_file():
                counter_files += 1
                print(i)
                with open(i, 'r') as file:
                    for number, line in enumerate(file, start=1):
                        #check for passwords inside of file
                        for test in kewwords_1:
                            if (test.lower() in line.lower() and "=" in line.lower()):
                                print(f"{Fore.RED} [WARNING] Possible {test} found {Style.RESET_ALL}")
                                print(f"{Fore.RED}file: {i} in line: {number} {Style.RESET_ALL}")
                                counter_warning += 1
        print("######################################################")
        print("scan completed!")
        print(f"Warnings Found: {counter_warning}")
        print(f"Files Scanned: {counter_files}")
        print("######################################################")







    elif path.exists() != True:
        print("ERROR: This path dont exist!")
    if path.exists() == True and path.is_file():
        print("ERROR: this is a file not directory!")



