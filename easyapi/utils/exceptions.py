# exceptions.py

class ColoredException(Exception):
    """Base class for colored exceptions."""
    color_code = "\033[91m"  # Default red
    reset_code = "\033[0m"

    def __init__(self, message):
        super().__init__(f"{self.color_code}{message}{self.reset_code}")


class AppError(ColoredException):
    """Generic application error."""
    color_code = "\033[91m"  # Red


class AppWarning(Warning):
    """Generic application warning (with yellow print support)."""
    color_code = "\033[93m"  # Yellow
    reset_code = "\033[0m"

    def __init__(self, message):
        # Warnings don't use raise by default, so we just color the message.
        self.message = f"{self.color_code}{message}{self.reset_code}"
        super().__init__(self.message)


class RouteAlreadyExistsError(AppError):
    pass