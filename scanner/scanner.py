from pathlib import Path
from .rules import check_line


SKIP_DIRECTORIES = {
    ".git", ".venv", "venv", "env", "node_modules",
    "__pycache__", ".idea", ".vscode"
}


class ScanResult:
    def __init__(self):
        self.findings = []
        self.files_scanned = 0
        self.files_skipped = 0

    @property
    def critical(self):
        return sum(f.severity == "CRITICAL" for f in self.findings)

    @property
    def high(self):
        return sum(f.severity == "HIGH" for f in self.findings)

    @property
    def medium(self):
        return sum(f.severity == "MEDIUM" for f in self.findings)

    @property
    def warnings(self):
        return len(self.findings)


def scan_repository(project_path):
    path = Path(project_path)

    if not path.exists():
        raise FileNotFoundError("This path does not exist!")
    if not path.is_dir():
        raise NotADirectoryError("This path is a file, not a directory!")

    result = ScanResult()

    for file_path in path.rglob("*"):
        if not file_path.is_file():
            continue
        if any(part in SKIP_DIRECTORIES for part in file_path.parts):
            continue

        try:
            with file_path.open("r", encoding="utf-8") as file:
                result.files_scanned += 1
                for line_number, line in enumerate(file, start=1):
                    result.findings.extend(check_line(file_path, line_number, line))
        except (OSError, UnicodeDecodeError):
            result.files_skipped += 1

    return result
