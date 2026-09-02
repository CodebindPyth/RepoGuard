from scanner.scanner import scan_repository
from reporter.reporter import print_banner, print_results


def main():
    print_banner()
    project_path = input("Enter the project path: ").strip()

    if not project_path:
        print("ERROR: path can't be empty!")
        return

    try:
        print("------------------------------------------------------")
        print(f"scanning: {project_path}")
        print("------------------------------------------------------")
        result = scan_repository(project_path)
        print_results(result)
    except FileNotFoundError as error:
        print(f"ERROR: {error}")
    except NotADirectoryError as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()
