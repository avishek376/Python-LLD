def singleton(class_instance):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_instance not in instances:
            instances[class_instance] = class_instance(*args, **kwargs)
        return instances[class_instance]

    return get_instance


@singleton
class MongoDB:
    def __init__(self, instance_number) -> None:
        print(f"Mongo DB instance number {instance_number} created")

    @classmethod
    def mongo_db_class_method(cls, data):
        print(f"class method calls {data}")


if __name__ == "__main__":
    mongo_db_conn1 = MongoDB(1)
    mongo_db_conn2 = MongoDB(2)
    # MongoDB.mongo_db_class_method(5)

    print(mongo_db_conn1 == mongo_db_conn2)
