from colorama import Fore, Style


def print_banner():
    print("##########################################################################")
    print("                               REPO GUARD")
    print("##########################################################################")


def print_results(result):
    print("\n######################################################")
    print("scan completed!")

    if result.warnings == 0:
        print("No security issues detected.")
    elif result.critical > 0:
        print(f"{Fore.RED}CRITICAL SECURITY ISSUES DETECTED{Style.RESET_ALL}")

    for finding in result.findings:
        color = Fore.RED if finding.severity in ("CRITICAL", "HIGH") else Fore.BLUE
        print(f"{color}[WARNING][{finding.severity}] {finding.message}{Style.RESET_ALL}")
        print(f"{color}file: {finding.file}\nline: {finding.line}\nmatched: {finding.matched}{Style.RESET_ALL}")

    print(f"{Fore.RED} CRITICAL Found: {result.critical} {Style.RESET_ALL}")
    print(f"{Fore.RED} HIGH Found: {result.high} {Style.RESET_ALL}")
    print(f"{Fore.BLUE} MEDIUM Found: {result.medium} {Style.RESET_ALL}")
    print(f"Total warnings: {result.warnings}")
    print(f"Files Scanned: {result.files_scanned}")
    print(f"Files Skipped: {result.files_skipped}")
    print("######################################################")
