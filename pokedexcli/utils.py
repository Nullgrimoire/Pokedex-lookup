import os

def clear_console() -> None:
    """
    Clears the console screen on Windows, macOS, and Linux.
    Note: Has no effect in some IDEs or notebook environments.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
