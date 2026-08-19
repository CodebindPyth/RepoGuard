from pathlib import Path
from colorama import Fore, Style, init



init()





print("##########################################################################")
print("                               REPO GUARD")
print("##########################################################################")



insecure_patterns = [
    "debug=True",
    "verify=False",
    "hashlib.md5(",
    "hashlib.sha1("
]
kewwords_1 = ["password", "api_key", "secret", "token", "private_key"]
dangerous = ['eval(', 'exec(', 'os.system(', 'shell=True']
dangerous_patterns = [
    "pickle.load(",
    "pickle.loads(",
    "subprocess.call(",
    "subprocess.Popen("
]
counter_files_cant_read = 0
counter_files = 0
high = critical = medium = 0
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
                        print(i)   
                        try:
                            with open(i, 'r') as file:
                                counter_files += 1
                                for number, line in enumerate(file, start=1):
                                    #check for passwords inside of file
                                    for test in kewwords_1:
                                        if (test.lower() in line.lower() and "=" in line.lower()):
                                            if test == "password" or test == "secret":
                                                print(f"{Fore.RED} [WARNING][HIGH] Possible leaks {test} found {Style.RESET_ALL}")
                                                print(f"{Fore.RED}file: {i} \n in line: {number} {Style.RESET_ALL}")
                                                high += 1
                                                counter_warning += 1
                                            elif test == "api_key" or test == "token" or test == "private_key":
                                                print(f"{Fore.RED} [WARNING][CRITICAL] Possible leaks {test} found {Style.RESET_ALL}")
                                                print(f"{Fore.RED}file: {i} \n in line: {number} {Style.RESET_ALL}")
                                                critical += 1
                                                counter_warning += 1
                                    for test in dangerous:
                                        if (test.lower() in line.lower()):
                                            if test == "eval(" or test == "exec(" or test == "os.system(":
                                                print(f"{Fore.RED} [WARNING][HIGH] Possible dangerous-code {test} found {Style.RESET_ALL}")
                                                print(f"{Fore.RED}file: {i} \n in line: {number} {Style.RESET_ALL}")
                                                high += 1
                                                counter_warning += 1
                                            elif test == "shell=True":
                                                print(f"{Fore.RED} [WARNING][CRITICAL] Possible dangerous-code {test} found {Style.RESET_ALL}")
                                                print(f"{Fore.RED}file: {i} \n in line: {number} {Style.RESET_ALL}")
                                                critical += 1
                                                counter_warning += 1
                                    for test in dangerous_patterns:
                                        if (test.lower() in line.lower()):
                                            if test == "pickle.load(" or test == "pickle.loads(":
                                                print(f"{Fore.RED} [WARNING][HIGH] Possible dangerous code Found {test} found {Style.RESET_ALL}")
                                                print(f"{Fore.RED}file: {i} \n in line: {number} {Style.RESET_ALL}")
                                                high += 1
                                                counter_warning += 1
                                            elif test == "subprocess.call(" or test == "subprocess.Popen(":
                                                print(f"{Fore.BLUE} [WARNING][MEDIUM] Possible dangerous code Found {test} found {Style.RESET_ALL}")
                                                print(f"{Fore.BLUE}file: {i} \n in line: {number} {Style.RESET_ALL}")
                                                medium += 1
                                                counter_warning += 1
                                    for test in insecure_patterns:
                                        if (test.lower() in line.lower()):
                                            if test == "debug=True" or test == "verify=False":
                                                print(f"{Fore.RED} [WARNING][HIGH] Possible INSECURE CONFIG {test} found {Style.RESET_ALL}")
                                                print(f"{Fore.RED}file: {i} \n in line: {number} {Style.RESET_ALL}")
                                                high += 1
                                                counter_warning += 1
                                            elif test == "hashlib.md5(" or test == "hashlib.sha1(":
                                                print(f"{Fore.BLUE} [WARNING][MEDIUM] Possible INSECURE CONFIG {test} found {Style.RESET_ALL}")
                                                print(f"{Fore.BLUE}file: {i} \n in line: {number} {Style.RESET_ALL}")
                                                medium += 1
                                                counter_warning += 1

                                        

                        except OSError:
                            counter_files_cant_read += 1
                            print(f"{i} [FILE SKIPPED]")
                        except UnicodeDecodeError:
                            counter_files_cant_read += 1
                            print(f"{i} [FILE SKIPPED]")
        print("######################################################")
        print("scan completed!")
        if counter_warning == 0:
            print("No security issues detected.")
        elif (critical > 0):
            print(f"{Fore.RED}CRITICAL SECURITY ISSUES DETECTED {Style.RESET_ALL}")
        
        print(f"{Fore.RED} CRITICAL Found: {critical} {Style.RESET_ALL}")
        print(f"{Fore.RED} HIGH Found: {high} {Style.RESET_ALL}")
        print(f"{Fore.BLUE} Medium Found: {medium} {Style.RESET_ALL}")
        print(f"Total warnings: {counter_warning}")
        print(f"Files Scanned: {counter_files}")
        print("######################################################")







    elif path.exists() != True:
        print("ERROR: This path dont exist!")
    if path.exists() == True and path.is_file():
        print("ERROR: this is a file not directory!")


