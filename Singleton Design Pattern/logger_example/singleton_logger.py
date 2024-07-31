import threading

class SingletonLogger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Ensure initialization only happens once
            self.initialized = True
            self._log_file = "application.log"
            self._log_lock = threading.Lock()

    def log(self, message):
        with self._log_lock:
            with open(self._log_file, "a") as f:
                f.write(message + "\n")

# Example usage
logger1 = SingletonLogger()
logger2 = SingletonLogger()

print(logger1 is logger2)  # True, proving both are the same instance

# Log some messages
logger1.log("This is a log message.")
logger2.log("This is another log message...")
