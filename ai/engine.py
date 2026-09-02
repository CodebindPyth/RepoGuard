class AIEngine:
    """Interface for RepoGuard's future local AI security engine."""

    def __init__(self, model_path=None):
        self.model_path = model_path
        self.loaded = False

    def load(self):
        # Model loading will be implemented after the scanner refactor.
        self.loaded = False

    def analyze(self, code, file_path=None, line_number=None):
        """Return AI findings using the same structure as scanner findings."""
        return []
