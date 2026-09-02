from .findings import Finding


SECRET_RULES = {
    "password": ("HIGH", "Possible password leak"),
    "secret": ("HIGH", "Possible secret leak"),
    "api_key": ("CRITICAL", "Possible API key leak"),
    "token": ("CRITICAL", "Possible token leak"),
    "private_key": ("CRITICAL", "Possible private key leak"),
}

DANGEROUS_RULES = {
    "eval(": ("HIGH", "Possible dangerous eval usage"),
    "exec(": ("HIGH", "Possible dangerous exec usage"),
    "os.system(": ("HIGH", "Possible dangerous os.system usage"),
    "shell=True": ("CRITICAL", "Possible dangerous shell execution"),
}

DESERIALIZATION_RULES = {
    "pickle.load(": ("HIGH", "Possible unsafe pickle deserialization"),
    "pickle.loads(": ("HIGH", "Possible unsafe pickle deserialization"),
    "subprocess.call(": ("MEDIUM", "Possible dangerous subprocess usage"),
    "subprocess.Popen(": ("MEDIUM", "Possible dangerous subprocess usage"),
}

INSECURE_RULES = {
    "debug=True": ("HIGH", "Possible insecure debug configuration"),
    "verify=False": ("HIGH", "TLS certificate verification disabled"),
    "hashlib.md5(": ("MEDIUM", "MD5 is cryptographically weak"),
    "hashlib.sha1(": ("MEDIUM", "SHA-1 is cryptographically weak"),
}


def check_line(file_path, line_number, line):
    findings = []
    lower = line.lower()

    for keyword, (severity, message) in SECRET_RULES.items():
        if keyword in lower and "=" in lower:
            findings.append(Finding(file_path, line_number, "secret", severity, message, keyword))

    for keyword, (severity, message) in DANGEROUS_RULES.items():
        if keyword in lower:
            findings.append(Finding(file_path, line_number, "dangerous-code", severity, message, keyword))

    for keyword, (severity, message) in DESERIALIZATION_RULES.items():
        if keyword in lower:
            findings.append(Finding(file_path, line_number, "dangerous-code", severity, message, keyword))

    for keyword, (severity, message) in INSECURE_RULES.items():
        if keyword in lower:
            findings.append(Finding(file_path, line_number, "insecure-config", severity, message, keyword))

    return findings
