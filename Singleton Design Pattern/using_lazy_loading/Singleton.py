class MongoDB:
    __instances = None

    def __init__(self):
        raise RuntimeError("create instance by get_instance() method")

    @classmethod
    def get_instance(cls):
        if cls.__instances is None:
            cls.__instances = cls.__new__(cls)
        return cls.__instances

    def business_logic(self, number):
        return f"MongoDB connection number {number}"


if __name__ == "__main__":
    mongoDB_conn1 = MongoDB.get_instance()
    mongoDB_conn2 = MongoDB.get_instance()

    print(id(mongoDB_conn1) == id(mongoDB_conn2))

    # Business Logic won't get called by single instance instead it will get called by
    # 2 different instances

    print(mongoDB_conn1.business_logic(11))
    print(mongoDB_conn2.business_logic(22))
