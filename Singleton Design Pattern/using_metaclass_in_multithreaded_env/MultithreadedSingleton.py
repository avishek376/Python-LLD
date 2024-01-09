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


class Student(metaclass=SingletonMetaClass):
    """This is a singleton class for student instances"""

    def __init__(self, *args, **kwargs):
        self.first_name = args[0]
        self.last_name = args[1]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def business_logic(self):
        print(f"This is the business logic of the singleton class {self.first_name} {self.last_name}")


student1 = Student("Ajay", "Biswas")
student2 = Student("Amit", "Roy")

if id(student1) == id(student2):
    print("Singleton worked,Both the instances are same")
else:
    print("Singleton failed,Both the instances are different")

thread1 = threading.Thread(target=student1.business_logic)
thread2 = threading.Thread(target=student2.business_logic)

thread1.start()
thread2.start()
