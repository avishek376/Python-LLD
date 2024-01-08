class StudentSingletonMeta(type):
    """This is a metaclass that will be used to create singleton classes"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """This method will be called when we try to create an instance of the class"""
        if cls not in cls._instances:
            cls._instances[cls] = super(StudentSingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class StudentSingleton(metaclass=StudentSingletonMeta):
    """This is a singleton class"""

    def __init__(self, *args, **kwargs):
        self.first_name = args[0]
        self.last_name = args[1]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


student1 = StudentSingleton("Ajay", "Biswas")
student2 = StudentSingleton("Amit", "Roy")

print((student1))
print((student2))

if id(student1) == id(student2):
    print("Singleton worked,Both the instances are same")
else:
    print("Singleton failed,Both the instances are different")
