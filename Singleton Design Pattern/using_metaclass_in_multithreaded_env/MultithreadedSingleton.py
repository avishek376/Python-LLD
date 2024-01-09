import threading


class SingletonMetaClass(type):
    """This is a metaclass that will be used to create singleton classes for student instances"""

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """This method will get called when an instance will get created"""
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MongoDB(metaclass=SingletonMetaClass):
    """This is a MongoDB db conn singleton class"""

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"MongoDB connection no {self.number}"

    def business_logic(self):
        print(f"MongoDB connection no {self.number}")


mongoDB_conn1 = MongoDB(23)
mongoDB_conn2 = MongoDB(47)

thread1 = threading.Thread(target=mongoDB_conn1.business_logic)
thread2 = threading.Thread(target=mongoDB_conn2.business_logic)

thread1.start()
thread2.start()

print(id(mongoDB_conn1) == id(mongoDB_conn2))
