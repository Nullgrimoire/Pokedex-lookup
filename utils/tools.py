import os

def clear_console():
    """Clears the console screen on Windows, macOS, and Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')
