import os
import sys
import unittest
from pathlib import Path


class TestEnvironment(unittest.TestCase):
    def test_using_anaconda_python(self):
        # The grader isn't Anaconda; this check is only for your computer.
        if os.environ.get("GITHUB_ACTIONS"):
            return
        is_anaconda = (Path(sys.prefix) / "conda-meta").is_dir()
        self.assertTrue(
            is_anaconda,
            "\n\nYou're not using Anaconda Python.\n"
            "VS Code is running: " + sys.executable + "\n"
            "Fix: press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows), "
            "choose 'Python: Select Interpreter', "
            "and pick the one that says 'anaconda3' (base).\n",
        )


if __name__ == "__main__":
    unittest.main()
