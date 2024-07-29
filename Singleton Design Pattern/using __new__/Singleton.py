class MongoDB:
    """This class is the implementation of Singleton class"""

    _instances = None

    def __new__(cls):
        if cls._instances is None:
            # If the instance is not created then create the instance
            # call the __new__ method of the super class
            cls._instances = super().__new__(cls)
        return cls._instances

    def business_logic(self, data):
        return f"MongoDB business logic by {data}"


if __name__ == "__main__":
    mongoDB_conn1 = MongoDB()
    mongoDB_conn2 = MongoDB()

    print(id(mongoDB_conn1) == id(mongoDB_conn2))

    # Business Logic won't get called by single instance instead it will get called by
    # 2 different instances
    print(mongoDB_conn1.business_logic("Ayan"))
    print(mongoDB_conn2.business_logic("Pavan"))
