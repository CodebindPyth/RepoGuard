from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    file: Path
    line: int
    rule: str
    severity: str
    message: str
    matched: str
    source: str = "rule"
    confidence: float = 1.0
